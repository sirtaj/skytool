
'''
    snip.py -- Read TESVSnip RecordStructure.xml file and generate a Python model for ESP/ESM files.

    Element types:
        Records: Group, Record
        Group: Subrecord, Group
        Record: Subrecord, Group
        Subrecord: Element
        Element

        {'Element': ['flags',
                     'type',
                     'name',
                     'options',
                     'hexview',
                     'notininfo',
                     'reftype',
                     'optional',
                     'repeat',
                     'multiline',
                     'condid',
                     'desc'],
         'Group': ['repeat', 'optional', 'id'],
         'Record': ['name', 'desc'],
         'Records': [],
         'Subrecord': ['repeat',
                       'optional',
                       'name',
                       'desc',
                       'size',
                       'notininfo',
                       'condid',
                       'condvalue',
                       'condition']}


    Generate Step:
        Record becomes a Record subclass
            Each subrecord becomes an attribute mapping to a field subclass
            Each deep element becomes 

        Subrecord becomes a field subclass

        Group becomes an internal group object (associated with parent object, usually a record)

        Types:
            Found: ['STR4', 'blob', 'byte', 'float', 'formid', 'int', 'lstring', 'sbyte', 'short', 
                    'str4', 'string', 'uint', 'ushort']
            Domain:
                filename
                formid type


    TODO:
        Identify childgroup refs by 
'''

#####
IDENTS = {}
CHILD_GROUPS = {}

def to_ident(desc, fallback):
    if not desc: return fallback
    words = [w.capitalize() for w in desc.strip().split() if w.isalnum()]
    ident = ''.join(words)
    if not ident or ident in IDENTS:
        return fallback
    IDENTS[ident] = 1
    return ident

#####

def read_snipconf(path):
    from xml.etree.ElementTree import ElementTree
    tree = ElementTree()
    tree.parse(path)
    return tree


def generate_python(tree):
    print '''

### WARNING: THIS IS A GENERATED FILE. HAND EDITS WILL BE LOST.

__doc__=\\
"""Generated Python Model for TESVSnip RecordStructure.xml.
"""

from esp import Record, ChildGroup, Field, record_type
'''

    print
    print "#### Top-level Subrecord groups ####"
    print

    for grp in tree.findall("Group"):
        if len(grp) > 0:
            CHILD_GROUPS[grp.get("id")] = grp

    RECORD_ORDER = list(tree.findall("Record"))

    for e_group in tree.findall("Group"):
        generate_global_group(tree, e_group)

    print
    print "#### Record Types (non-group) ####"
    print
    GROUP_ORDER = list(tree.findall("Record"))
    print "GROUP_ORDER =", repr([e.attrib["name"] for e in GROUP_ORDER])
    print

    for e_record in RECORD_ORDER:
        generate_global_record(tree, e_record)
    print


def generate_global_group(tree, e_group):
    if len(e_group) == 0:
        # this is a ref
        print "# ChildGroup Reference: ", e_group.get("id")
    
    print "class", e_group.attrib["id"], "(ChildGroup):"
    optional = True if e_group.get("optional", 0) in [1, "1"] else False
    print "\t__optional__ =", optional
    repeatable = True if e_group.get("repeat", 1) in [1, "1"] else False
    print "\t__repeat__ =", repeatable
    print

def expand_group(egrp, depth=0):
    if len(egrp) == 0:
        egrp = CHILD_GROUPS[egrp.attrib["id"]]
    for e in egrp:
        if e.tag == "Subrecord":
            print "    "*depth, "#", e.get("name"), e.get("desc", "")
        elif e.tag == "Group":
            if len(e) == 0:
                e = CHILD_GROUPS[e.attrib["id"]]
            print "    "*depth, "# ChildGroup", e.get("id")
            expand_group(e, depth+1)

def generate_global_record(tree, e_record):
    rec_tag = e_record.attrib["name"]
    desc = e_record.get("desc")
    cname = to_ident(desc, rec_tag)

    print "@record_type('%s')" % rec_tag
    print "class %s(Record):" % cname

    print "    '''%s'''" % (desc or "")
    for child in e_record:
        if child.tag == "Subrecord":
            print "    # ", child.attrib["name"], child.get("desc", "")
        elif child.tag == "Group":
            print "    # ChildGroup ", child.get("id")
            expand_group(child, 1)

    print

def generate_types(el):
    types = {}
    global ELEMENT_ATTRS, ELEMENT_SUBS

    for sub_el in el.getroot().getiterator():
        sub_info = ELEMENT_SUBS.setdefault(sub_el.tag, [])
        for attr in sub_el.attrib.keys():
            if attr not in sub_info:
                sub_info.append(attr)

        el_info = ELEMENT_ATTRS.setdefault(sub_el.tag, [])
        for child in sub_el:
            if child.tag not in el_info:
                el_info.append(child.tag)

        if sub_el.get("type"):
            types[sub_el.get("type")] = 1
    print "# TYPES:", sorted(types.keys())
    import pprint

if __name__ == '__main__':
    import pprint
    tree = read_snipconf("snipconf/RecordStructure.xml")
    generate_python(tree)
