
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


IDENTS = {}
IDENT_BY_OBJ = {}

def strip_non_ident(word):
    return ''.join(c for c in word if c.isalnum() or c.isspace())

def to_attr_ident(word):
    ident = ''.join(w.capitalize() for w in strip_non_ident(word).split())
    if ident:
        ident = ident[0].lower() + ident[1:]
    return ident

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

def arg_list(*seq):
    return ', '.join((s if not isinstance(s, tuple) else ("%s = %s" % s))
                        for s in seq if s)


#############
# Code gen

def generate_python(snip_file, py_file):
    import xrev, pytext
    records = xrev.parse_xreved(snip_file, tessnip)
    group_order = [(r.name, r) for r in records if isinstance(r, Record)]

    child_ctr = 0
    for c in records:
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

        for child in records:
            write_class(pf, child)


def create_ident(obj, pfx = '', parent_idx = 0):
    if isinstance(obj, Record):
        name = to_class_ident(obj.desc, obj.name)
    elif isinstance(obj, Group):
        name = "%sSubGroup%d" % (pfx, parent_idx) if not obj.id else obj.id
    elif isinstance(obj, Subrecord):
        name = to_class_ident(obj.desc, "%sSubRecord%d" % (pfx, parent_idx))
    elif isinstance(obj, Element):
        name = "%s%s%s" % (pfx, obj.name, parent_idx)

    IDENT_BY_OBJ[ obj ] = name

    child_ctr = 0
    child_pfx = "%s_" % (name)
    for child in obj:
        create_ident(child, child_pfx, child_ctr)
        child_ctr += 1


def write_class(py, record):
    if isinstance(record, Record):
        py.blank()
        py.write("########################")
        py.write('@record_type(%s)' % repr(str(record.name)))
        with py.python_class(IDENT_BY_OBJ[record], ['Record']) as subcls:
            write_attributes(py, record)
    elif isinstance(record, Group):
        with py.python_class(IDENT_BY_OBJ[record], ['AttributeGroup']) as subcls:
            write_attributes(py, record)
    elif isinstance(record, Subrecord):
        with py.python_class(IDENT_BY_OBJ[record], ['Subrecord']) as subcls:
            write_attributes(py, record)

    for child in record:
        write_class(py, child)


def write_attributes(py, rec):
    order = []

    for child in rec:
        if isinstance(child, Element):
            ident = to_attr_ident(child.name)
            base = 'Attribute' if not child.reftype else 'Reference'
            cls = '%sSequence' if child.repeat else '%s'
            py.assign(ident, '%s(%s)' 
                        % (cls % base,
                            arg_list(
                                repr(str(child.type)),
                                ('reftype', repr(str(child.reftype)))
                                    if child.reftype else None,
                                ('nullable', 'True') if child.optional else None)))

        elif isinstance(child, Subrecord):
            cls = 'SubrecordSequence' if child.repeat else 'Subrecord'
            ident = to_attr_ident(child.desc or child.name)
            py.assign(ident, '%s(%s)' % (cls,
                            arg_list(
                                repr(str(IDENT_BY_OBJ[child])),
                                ('field', repr(str(child.name))),
                                ('size', child.size) if child.size else None,
                                ('nullable', 'True') if child.optional else None)))

        else:
            ident = to_attr_ident(child.id or IDENT_BY_OBJ[child])
            py.assign(ident, 'ChildGroup(%s)' % repr(str(IDENT_BY_OBJ[child])) )

        order.append(str(ident))

    py.blank()
    py.assign( '__order__', repr(order))


if __name__ == '__main__':
    import sys
    generate_python(sys.argv[1], sys.argv[2])
