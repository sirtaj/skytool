
import esp
import tessnip
from tessnip import *
import re

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


IDENTS = {}
IDENT_BY_OBJ = {}

def strip_non_ident(word):
    return ''.join(c for c in word if c.isalnum() or c.isspace())

def to_attr_ident(word):
    return ''.join(w.capitalize() for w in strip_non_ident(word).split())

ident_re = re.compile("^[a-zA-Z_][a-zA-Z0-9_]*$").match

def is_ident(word): return ident_re(word) is not None

def to_class_ident(desc, fallback):
    if not desc: return fallback
    words = [w.capitalize() for w in desc.strip().split() if w.isalnum()]
    ident = ''.join(words)
    if not ident or not is_ident(ident) or ident in IDENTS:
        return fallback
    IDENTS[ident] = 1
    return ident


#############

def generate_python(snip_file, py_file):
    import xrev, pytext
    records = xrev.parse_xreved(snip_file, tessnip)
    group_order = [(r.name, r) for r in records.children if isinstance(r, Record)]

    child_ctr = 0
    for c in records.children:
        try:
            create_ident(c, '', child_ctr)
            child_ctr += 1
        except Exception, e:
            print "FAIL:", c
            raise

    #
    with pytext.PythonFile.do(py_file) as pf:
        pf.write('from esp import Record, AttributeGroup, Field, record_type')
        pf.blank()

        pf.assign('RECORD_ORDER', [str(n) for (n, r) in group_order])
        pf.blank()

        for child in records.children:
            write_subrecord_classes(pf, child)


def create_ident(obj, pfx = '', parent_idx = 0):
    if isinstance(obj, Record):
        name = to_class_ident(obj.desc, obj.name)
        children = obj.children
    elif isinstance(obj, Group):
        if obj.id:
            name = obj.id
        else:
            name = "%sSubGroup%d" % (pfx, parent_idx)
        children = obj.children
    elif isinstance(obj, Subrecord):
        name = to_class_ident(obj.desc, "%sSubRecord%d" % (pfx, parent_idx))
        children = obj.elements
    elif isinstance(obj, Element):
        name = "%s%s%s" % (pfx, obj.name, parent_idx)
        children = None

    IDENT_BY_OBJ[ obj ] = name
    if not children: return

    child_ctr = 0
    child_pfx = "%s_" % (name)
    for child in children:
        create_ident(child, child_pfx, child_ctr)
        child_ctr += 1


def write_subrecord_classes(py, record):
    if isinstance(record, Record):
        py.write("########################")
        py.write('@record_type(%s)' % repr(str(record.name)))
        with py.python_class(IDENT_BY_OBJ[record], ['Record']) as subcls:
            write_attributes(py, record)
        children = record.children
    if isinstance(record, Group):
        with py.python_class(IDENT_BY_OBJ[record], ['AttributeGroup']) as subcls:
            write_attributes(py, record)
        children = record.children
    elif isinstance(record, Subrecord):
        with py.python_class(IDENT_BY_OBJ[record], ['Subrecord']) as subcls:
            write_attributes(py, record)
        return

    for child in children:
        write_subrecord_classes(py, child)


def write_attributes(py, rec):
    if isinstance(rec, Subrecord):
        children = rec.elements
    else:
        children = rec.children

    for child in children:
        if isinstance(child, Element):
            py.assign(to_attr_ident(child.name), 'Attribute(%s)' % (repr(str(child.type))))
        elif isinstance(child, Subrecord):
            py.assign(to_attr_ident(child.desc or child.name),
                    'Subrecord(%s, field = "%s")' % (IDENT_BY_OBJ[child], child.name) )
        else:
            py.assign(to_attr_ident(child.id or IDENT_BY_OBJ[child]),
                    'ChildGroup(%s)' % IDENT_BY_OBJ[child] )


if __name__ == '__main__':
    import sys
    generate_python(sys.argv[1], sys.argv[2])
