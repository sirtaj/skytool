
'''
Reverse-engineer structure of an unknown XML file.

Ideal output is something resembling a RELAX NG schema.


pcode:

    maintain a stack of element context

Element
    name
    attribute *
        

'''

import sys, pprint

class Schema(object):
    '''
    '''
    def __init__(self):
        self.all_elements = {} # element name -> element defs
        self.root = None

    def element(self, name):
        if name in self.all_elements:
            return self.all_elements[name]

        return self.all_elements.setdefault(name, Element(name))

    def parse(self, doc):
        from xml.etree.ElementTree import ElementTree
        tree = ElementTree()
        tree.parse(doc)
        self.read_doc(tree)

    def read_doc(self, tree):
        element_stack = []

        el_iter = tree.getroot().iter()

        e_root = el_iter.next()
        self.root = Root(e_root.tag)
        self.all_elements[self.root.name] = self.root

        self.read_element(self.root, e_root, None)

    def read_element(self, obj, el, parent):
        obj.add_el(el, parent)
        for sub_el in el:
            self.read_element(self.element(sub_el.tag), sub_el, obj)

    def dump(self):
        for el in sorted(self.all_elements.keys()):
            obj = self.all_elements[el]
            obj.dump()

class Element(object):
    '''
    '''
    def __init__(self, name):
        self.name = name
        self.attrs = {}
        self.attr_sets = {} # parent -> [tuple of attr names that appear together]
        self.has_cdata = False
        self.has_text = False

        self.sub_elements = {}
        self.sub_element_order = []
        self.children_ordered = True
        self.containers = {}

    def add_child(self, child):
        child.containers.setdefault(self.name, self)
        self.sub_elements.setdefault(child.name, child)

        if child.name in self.sub_element_order:
            if self.sub_element_order[-1] != child.name:
                self.children_ordered = False
        else:
            self.sub_element_order.append(child.name)

    def add_el(self, el, parent):
        if not self.has_text and el.text and el.text.strip():
            self.has_text = True

        for el_attr, el_value in el.attrib.items():
            attr = self.attrs.get(el_attr)
            if not attr:
                attr = self.attrs.setdefault(el_attr, Attribute(el_attr))
            attr.add_value(el_value)

        attr_set = tuple(sorted(el.attrib.keys()))
        attr_par = self.attr_sets.setdefault(parent, [])

        if attr_set not in attr_par:
            attr_par.append(attr_set)

        if parent is not None:
            parent.add_child(self)

    def required_attrs(self):
        ''' seq of attrs that are never optional
        '''
        for attr_name in self.attrs.keys():
            try:
                for attr_sets in self.attr_sets.itervalues():
                    for aset in attr_sets:
                        if attr_name not in aset:
                            raise AttrOptional
            except AttrOptional:
                continue

            yield attr_name

    def optional_sets(self):
        '''Seq of (container, attr sets) containing no required attrs
        '''
        req = dict((a, True) for a in self.required_attrs())

        for container, attr_sets in self.attr_sets.iteritems():
            yield (container, [tuple(a for a in aset if a not in req) for aset in attr_sets])


    def separate_attr_sets(self):
        '''Separates attribute sets into groups of
            common to all containers
            specific to a subset of containers
            specific to one container
        '''
        rev_map = {} # set -> [container type]
        required = list(self.required_attrs())

        for container, attr_set in self.attr_sets.iteritems():
            for aset in attr_set:
                filtered_set = tuple(at for at in aset if at not in required)
                if len(filtered_set):
                    l = rev_map.setdefault(filtered_set, [])
                    if container not in l:
                        l.append(container)

        groups = [(len(group), sorted(group), attrs) for attrs, group in rev_map.iteritems()]
        groups.sort()
        groups.reverse()
        for ln, group, attrs in groups:
            yield (group, attrs)

    def is_root(self):
        return False

    def is_leaf(self):
        return len(self.sub_elements.keys()) == 0

    ####
    def dump(self):
        req_attr = "(%s)" % ', '.join(self.required_attrs())

        if self.is_root():
            print "ROOT", self.name, req_attr
        elif self.is_leaf():
            print "Leaf", self.name, req_attr
        else:
            print self.name, req_attr
        
        if not self.is_root():
            parents = ', '.join(sorted(self.containers.keys()))
            print "\tContained by:", parents

        if not self.is_leaf():
            print "\tCan contain:", self.sub_element_order, \
                    ("(ordered)" if self.children_ordered else "(any order)")

        if self.has_text: print "\tContains CDATA"

        if len(self.attrs):
            print "attr types:"
            for a_name, attr in self.attrs.iteritems():
                guess = attr.best_guess_type()
                possible = ('(%s)' % ', '.join(attr.possible_types.keys()) 
                                if len(attr.possible_types) > 1 else '')
                vals = ("(%s)" % ', '.join(repr(v[:7]) for v in attr.possible_values.keys()[:7]))
                print ("\t%s:" % a_name), guess, possible, vals

            print
            print "attr sets:"
            #pprint.pprint(list(self.optional_sets()))
            pprint.pprint(list(self.separate_attr_sets()))

        print
        print

    def __repr__(self):
        return self.name

class AttrOptional(Exception): pass

class Root(Element):
    '''
    '''
    def is_root(self):
        return True


class Attribute(object):
    '''

    possibly detectable types:
        empty/null?
        int
        float
        strings:
            ident
            text
            comma-separated
    '''
    def __init__(self, name):
        self.name = name
        self.possible_values = {} # val
        self.possible_types = {} # type -> count

    def add_value(self, v):
        self.possible_values[v] = self.possible_values.get(v, 0) + 1

        atype = match_attr_type(v)
        if atype not in self.possible_types:
            self.possible_types[atype] = 0

        self.possible_types[atype] += 1

    def best_guess_type(self):
        types = list(self.possible_types.keys())
        if len(types) == 1:
            return types[0]

        if 'text' in types:
            return 'text'

        if 'csv' in types:
            return 'csv'

        if 'ident' in types:
            return 'ident'

        if 'int' in types and 'float' not in types:
            return 'int'

        if 'float' in types:
            return 'float'

        return ', '.join(types)


############################################################################
# try to identify type of attribute value

def match_csv(v):
    return 'csv' if ',' in v else None

def match_text(v):
    return 'text' if ' ' in v else None

def match_ident(v):
    try:
        if not v: return None
        float(v)
        int(v)
    except ValueError:
        return 'ident'

def match_int(v):
    try:
        int(v)
    except ValueError:
        return None

    return 'int'

def match_float(v):
    try:
       float(v)
    except ValueError:
        return None

    try:
        int(v)
        return None
    except ValueError:
        return 'float'

    return 'float'


def match_attr_type(v, matchers = [match_float, match_int, match_csv, match_text, match_ident]):
    if not v: return 'empty'

    for m in matchers:
        t = m(v)
        if t is not None:
            return t

    return 'text'


########################################################
# Python gen



def generate_classes(el):
    ctor_args_self = ['self']
    ctor_args_required = [a for a in el.required_attrs()]
    ctor_args_optional = [("%s = None" % a) for a in el.attrs.keys() if a not in ctor_args_required]

    ctor_args = ', '.join(ctor_args_self + ctor_args_required + ctor_args_optional)

    print
    print "class %s(object):" % (el.name)
    print "    ''''"


    print "    ''''"
    print "    def __init__(%s):" % ctor_args
    print "        pass"

    slots = [repr(a) for a in el.attrs.iterkeys()]

    if not el.is_leaf():
        if len(el.sub_elements.keys()) == 1:
            collection_name = repr(el.sub_elements.keys()[0].lower() + 's')
        else:
            collection_name = repr('children')

        slots.append(collection_name)

    print
    print "    __slots__ = (%s,)" % ', '.join(slots)
    print

    for attr in el.attrs.itervalues():
        print "    %s = typed_property(%s)" % (attr.name, repr(attr.best_guess_type()))



if __name__ == '__main__':
    schema = Schema()
    schema.parse(sys.argv[1])
    schema.dump()

    print "##################"
    for c in schema.all_elements.itervalues():
        generate_classes(c)
