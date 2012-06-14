
class Record:
    def __init__(self, name, desc = ''):
        self.valid_parents = []
        self.name = ''
        self.desc = desc
        self.sub_records = []

GROUPS = []

def read_snipconf(path):
    from xml.etree.ElementTree import ElementTree
    tree = ElementTree()
    tree.parse(path)
    tags = {}
    generate_root(tree.getroot())


def generate_root(el):
    for sub_el in el:
        if sub_el.tag == 'Record':
            generate_record_class(sub_el, parents = [])

def generate_record_class(el, parents):
    print "class %s(Record):" % el.attrib['name']
    print "    __fields__ = ", repr([sub_el.attrib['name'] for sub_el in el if sub_el.get('name')])
    for sub_el in el:
        if sub_el.tag == 'Subrecord':
            pass
        else:
            print "    #", sub_el.tag
    print

    for sub_el in el:
        if sub_el.tag == 'Subrecord':
            generate_subrecord_class(sub_el, parents + [el])

field_name_count = 0

def generate_subrecord_class(el, parents):
    global field_name_count
    name = el.attrib["name"]
    if not name.isalnum():
        class_name = "F_%d" % field_name_count
        field_name_count += 1
    else:
        class_name = name

    print "@field_type(%s)" % repr(name)
    print "class F_%s(Field):" % class_name
    if el.get("desc"):
        print "    '''%s'''" % el.get("desc")
        for a,v in el.items():
            if a in ['name', 'desc']: continue
            print "    #", a, "=", repr(v)
        print


if __name__ == '__main__':
    read_snipconf("snipconf/RecordStructure.xml")
