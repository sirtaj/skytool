
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
    return ''.join(c for c in str(word) if c.isalnum() or c.isspace() or c == '_')

def to_ident(word):
    return ''.join(w.capitalize() for w in strip_non_ident(word).split())

def to_attr_ident(word):
    ident = to_ident(word)
    if ident:
        ident = ident[0].lower() + ident[1:]
    return ident

ident_re = re.compile("^[a-zA-Z_][a-zA-Z0-9_]*$").match

def is_ident(word): return ident_re(word) is not None

def to_class_ident(desc, fallback):
    if not desc: return fallback
    ident = to_ident(desc)
    if not ident or not is_ident(ident) or ident in IDENTS:
        ident = fallback
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
        pf.write('from esp import *')
        pf.blank()

        pf.assign('RECORD_ORDER', [str(n) for (n, r) in group_order])
        pf.blank()

        for child in records:
            write_class(pf, child)


def create_ident(obj, pfx = '', parent_idx = 0):
    if isinstance(obj, Record):
        name = to_class_ident(obj.desc, obj.name)
    elif isinstance(obj, Group):
        name = "%s%d" % (pfx, parent_idx) if not obj.id else obj.id
    elif isinstance(obj, Subrecord):
        name = to_ident(obj.desc or obj.name)
        if not name:
            name = "%s%d" % (pfx, parent_idx)
        if name in IDENTS:
            name = pfx + name
        else:
            IDENTS[name] = 1
    elif isinstance(obj, Element):
        name = "%s%s%s" % (pfx, obj.name, parent_idx)

    IDENT_BY_OBJ[ obj ] = name

    child_ctr = 0
    child_pfx = "%s_" % (name)
    for child in obj:
        create_ident(child, child_pfx, child_ctr)
        child_ctr += 1


def write_class(py, record):
    '''Generate a python class for a snip element.
    '''
    if isinstance(record, Record):
        py.blank()
        py.write("########################")
        py.write('@record_type(%s)' % repr(str(record.name)))
        with py.python_class(IDENT_BY_OBJ[record], ['Record']) as subcls:
            write_attributes(py, record)
    elif isinstance(record, Group):
        with py.python_class(IDENT_BY_OBJ[record], ['SubrecordGroup']) as subcls:
            write_attributes(py, record)
    elif isinstance(record, Subrecord):
        with py.python_class(IDENT_BY_OBJ[record], ['Subrecord']) as subcls:
            write_attributes(py, record)

    for child in record:
        write_class(py, child)


def write_attributes(py, rec):
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
                                repr(str(IDENT_BY_OBJ[child])),
                                ('tag', repr(str(child.name))),
                                ('size', child.size) if child.size else None,
                                ('nullable', 'True') if child.optional else None)))

        else:
            ident = to_attr_ident(child.id or IDENT_BY_OBJ[child])
            cls = 'subrecord_group_set' if child.repeat else 'subrecord_group'
            py.assign(ident, '%s( %s )' % ( cls,
                            arg_list(
                                repr(str(IDENT_BY_OBJ[child])),
                                ('nullable', 'True') if child.optional else None)))

        order.append(str(ident))
    else:
        py.blank()

    # TODO We can probably get away with a counter hack here
    #py.assign( '__order__', repr(order))


if __name__ == '__main__':
    import sys
    generate_python(sys.argv[1], sys.argv[2])
