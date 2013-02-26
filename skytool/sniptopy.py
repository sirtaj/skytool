
import esp
import tessnip
from tessnip import *
import re


###################################
# Type and identifier mapping

DATA_TYPES = {
    'blob':	esp.Blob,

    'sbyte':	esp.Byte,
    'byte':     esp.UnsignedByte,

    'int':      esp.Integer,
    'uint':	    esp.UnsignedInteger,
    'short':	esp.Short,
    'ushort':	esp.UnsignedShort,
    'float':	esp.Float,

    'str4':	    esp.Str4,
    'string':	esp.String,
    'lstring':	esp.LString,

    'formid':	esp.Reference, # TODO OwnedReference, use reftype
}

def map_type(snip_type):
    return "esp." + DATA_TYPES[snip_type.lower()].__name__


class Linker:
    def __init__(self):
        self.obj_by_ident = {}
        self.ident_by_obj = {}

    def add(self, obj, *ident_choices):
        '''Adds obj to registered objects. Registers first acceptable object
        identity from the list of choices. If object is already registered, raise an error.
        '''
        if obj in self.ident_by_obj:
            raise KeyError, ("Linker: object %s already has identity %s"
                                    % (obj, self.ident_by_obj[obj]))

        for ident in ident_choices:
            if ident and is_ident(ident) and ident not in self.obj_by_ident:
                self.obj_by_ident[str(ident)] = obj
                self.ident_by_obj[obj] = str(ident)
                return ident

        raise AssertionError, ("No acceptable identity for object %s, tried %s"
                                    % (obj, ident_choices))

    def has_object(self, obj):
        return obj in self.ident_by_obj

    def ref(self, obj):
        return self.ident_by_obj[obj]

    def has_ident(self, ident):
        return ident in self.obj_by_ident


ident_re = re.compile("^[a-zA-Z_][a-zA-Z0-9_]*$").match

def is_ident(word): return (word is not None) and (ident_re(word) is not None)

def strip_non_ident(word):
    return ''.join(c for c in str(word) if c.isalnum() or c.isspace() or c == '_')

def to_ident(word):
    return ''.join(w.capitalize() for w in strip_non_ident(word).split())

def to_attr_ident(word):
    ident = to_ident(word)
    if ident:
        ident = ident[0].lower() + ident[1:]
    return ident

def arg_list(*seq):
    return ', '.join((s if not isinstance(s, tuple) else ("%s = %s" % s))
                        for s in seq if s)


#############
# Code gen

def generate_python(snip_file, py_file):
    import xrev, pytext
    records = xrev.parse_xreved(snip_file, tessnip)
    group_order = [(r.name, r) for r in records if isinstance(r, Record)]

    linker = Linker()

    child_ctr = 0
    for c in records:
        try:
            create_ident(c, linker, '', child_ctr)
            child_ctr += 1
        except Exception, e:
            print "FAIL:", c
            raise

    #
    with pytext.PythonFile.do(py_file) as pf:
        pf.write('from esp import *')
        pf.blank()

        pf.assign('RECORD_ORDER', [str(n) for (n, r) in group_order])
        pf.blank()

        for child in records:
            write_class(pf, child, linker)


def create_ident(obj, linker, pfx = '', parent_idx = 0):
    '''Generate a python identifier for a snip element recursively.
    '''
    parent_pfx = "%s%d" % (pfx, parent_idx)

    if isinstance(obj, Record):
        name = linker.add(obj, to_ident(obj.desc), obj.name)
    elif isinstance(obj, Group):
        if obj.id and (len(obj.children) == 0):
            # this is probably a reference to an existing group, skip it
            return
        name = linker.add(obj, "%s%d" % (pfx, parent_idx) if not obj.id else obj.id)
    elif isinstance(obj, Subrecord):
        name = to_ident(obj.desc or obj.name)
        typed_name = to_ident( obj.desc + " " + obj.name )
        prefixed_name = parent_pfx + '_' + to_ident(obj.desc + " " + obj.name)
        name = linker.add(obj, name, typed_name, prefixed_name)
    elif isinstance(obj, Element):
        name = linker.add(obj, "%s%s%s" % (pfx, to_ident(obj.name), parent_idx) )

    child_ctr = 0
    child_pfx = "%s_" % (name)
    for child in obj:
        create_ident(child, linker, child_pfx, child_ctr)
        child_ctr += 1


def write_class(py, record, linker):
    '''Generate a python class for a snip element.
    '''
    print "write_class", record
    if isinstance(record, Record):
        superclass = 'Record'

        py.blank()
        py.write("########################")
        py.write('@record_type(%s)' % repr(str(record.name)))

    elif isinstance(record, Group):
        if record.id and (len(record.children) == 0):
            # this is a reference to an existing group, skip it
            return
        superclass = 'SubrecordGroup'
    elif isinstance(record, Subrecord): superclass = 'Subrecord'
    else: return

    with py.python_class(linker.ref(record), [superclass]) as subcls:
        write_attributes(py, record, linker)

    for child in record:
        write_class(py, child, linker)


def write_attributes(py, rec, linker):
    '''Generate properties for each attribute of a snip element's generated python class.

    Types and flags are mapped to esp.py types and helpers.
    '''
    order = []

    for child in rec:
        if isinstance(child, Element):
            ident = to_attr_ident(child.name)
            if child.reftype:
                type_str = repr(str(child.reftype))
                base = 'reference'
            else:
                type_str = ('data_type', map_type(child.type))
                base = 'field'

            py.assign(ident, '%s( %s )' 
                        % ((base + "_set") if child.repeat else base,
                            arg_list(
                                type_str,
                                ('nullable', 'True') if child.optional else None)))

        elif isinstance(child, Subrecord):
            ident = to_attr_ident(child.desc or child.name)
            cls = 'subrecord_set' if child.repeat else 'subrecord'

            py.assign(ident, '%s( %s )' % (cls,
                            arg_list(
                                repr(linker.ref(child)),
                                ('tag', repr(str(child.name))),
                                ('size', child.size) if child.size else None,
                                ('nullable', 'True') if child.optional else None)))

        elif isinstance(child, Group):
            ident = to_attr_ident(child.id or linker.ref(child))
            if linker.has_object(child):
                ref = repr(linker.ref(child))
            else:
                ref = repr(child.id)
            cls = 'subrecord_group_set' if child.repeat else 'subrecord_group'
            py.assign(ident, '%s( %s )' % ( cls,
                            arg_list( ref,
                                ('nullable', 'True') if child.optional else None)))

        order.append(str(ident))

    if not len(order):
        py.write('pass')


if __name__ == '__main__':
    import sys
    generate_python(sys.argv[1], sys.argv[2])
