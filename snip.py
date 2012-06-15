
'''
    snip.py -- Read TESVSnip RecordStructure.xml file and generate a Python model for ESP/ESM files.

    Element types:
        Record
            Contains Groups, Subrecords
        Group
            Contains Records, Subrecords
        Subrecord
            Contains Elements
        Element
            Typed scalar (field)

if a subrecord has more than one child, we need to create a new object
otherwise an attr will do

'''

SUBRECORD_USE_COUNT = {}
RECORDS = {}
SUBRECORDS = {}
GROUPS = {}
ELEMENT_ATTRS = {}
ELEMENT_SUBS = {}
field_name_count = 0

def read_snipconf(path):
    from xml.etree.ElementTree import ElementTree
    tree = ElementTree()
    tree.parse(path)

    generate_types(tree)

    for e_group in tree.findall("Group"):
        generate_global_group(tree, e_group)

    for e_record in tree.findall("Record"):
        generate_global_record(tree, e_record)


def generate_global_group(tree, e_group):
    print "class", e_group.attrib["id"], "(Group):"
    optional = True if e_group.get("optional", 0) in [1, "1"] else False
    print "\t__optional__ =", optional
    print

def generate_global_record(tree, e_record):
    print "class", e_record.attrib["name"], "(Record): pass"
    #optional = True if e_record.get("optional", 0) in [1, "1"] else False
    #print "\t__optional__ =", optional
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

    print "# ========== ATTRS ==============="
    pprint.pprint(ELEMENT_ATTRS)
    print
    print "# ========== TREE ==============="
    pprint.pprint(ELEMENT_SUBS)
    print

if __name__ == '__main__':
    import pprint
    read_snipconf("snipconf/RecordStructure.xml")
