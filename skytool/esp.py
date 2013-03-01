
__doc__=\
'''Core object model for ESP/ESM files.
'''

import game as game_
import struct
from struct import unpack as st_unpack

RECORD_TYPES = {}
KNOWN_SUBGROUPS = '''REFR ACHR NAVM PGRE PHZD LAND INFO'''.strip().split()
EMPTY_GROUP_RECORDS = '''CLDC HAIR RGDL SCPT SCOL PWAT'''.strip().split()

def record_type(rec_tag):
    def tag_record_class(klazz):
        if rec_tag in RECORD_TYPES:
            print AssertionError,  \
                ("trying to register %s for existing tag %s, mapped to %s" %
                            (rec_tag, klazz, RECORD_TYPES[rec_tag]))
        else:
            RECORD_TYPES[rec_tag] = klazz
            klazz.___REC___ = rec_tag

        return klazz
    return tag_record_class


##########################################
DEFINITION_COUNTER = 0

class OrderedDescriptor(object):
    def __init__(self):
        global DEFINITION_COUNTER
        self.declaration_order = DEFINITION_COUNTER     # will be used by __new__ to get order
        DEFINITION_COUNTER += 1
        self.attribute_name = None          # will be set by __new__

    def __set__(self, obj, value):
        raise NotImplementedError

    def __get__(self, obj):
        raise NotImplementedError

    @classmethod
    def lookup_type(cls, type_name):
        '''Helps to resolve text type name to class once everything is defined.
        '''
        raise NotImplementedError


class OrderedAttributes(object):
    def __new__(cls, name, supers, class_dict):
        '''When new subclasses of BaseRecord are created, any declared OrderedDescriptor
        subclasses are ordered into a "__order__" class attribute, based on the
        "declaration_order" attribute, which is expected to be an integer set by the
        descriptor's constructor.
        '''
        print name, supers
        sub_cls = type(name, supers, class_dict)

        # configure __order__ class attribute to match declaration order of descriptors.
        attr_order = []
        for attr_name, attr_descriptor in class_dict.iteritems():
            if isinstance(attr_descriptor, OrderedDescriptor):
                attr_order.append((attr_descriptor.declaration_order, attr_descriptor))
                attr_descriptor.attribute_name = attr_name

        attr_order.sort()

        old_order = getattr(sub_cls, '__order__', [])
        sub_cls.__order__ = tuple(list(old_order) + [desc for (n, desc) in attr_order])

        return sub_cls


class BaseRecord(object):
    '''Core superclass for TES ESP/ESM records and subrecords.

    There's a great deal of magic going on in here.

    Descriptors of type OrderedDescriptor get registered by their declaration order
    in the class, so that the __order__ class tuple can be used for reading and writing
    to the plugin file.

    Subclass descriptors get ordered AFTER their superclass descriptors.
    '''
    def __init__(self, *args, **kwargs):
        pass

    __metaclass__ = OrderedAttributes

    # Read constructor for all record subclasses
    @staticmethod
    def read_from(fd):
        record_offset = fd.tell()
        typed = fd.read(4)
        if not typed: return None

        try:
            rec_type, = st_unpack("4s", typed)
        except:
            print "Fail read header at:", repr(typed)
            raise

        rc_class = RECORD_TYPES[rec_type]
        rec = rc_class()
        rec.type = rec_type
        rec.file_offset = record_offset
        rec.read_header(fd)
        return rec

    ## Concrete subclasses should override
    def read_header(self, fd):  raise NotImplementedError
    def has_subrecords(self):   return False
    def record_size(self):      return self.HEADER_SIZE + self.dataSize
    def data_size(self):        return self.dataSize
    def data_offset(self):      return self.file_offset + self.HEADER_SIZE
    def data_end_offset(self):  return self.file_offset + self.record_size()

    ## Convenience functions - common

    def seek_data(self, fd):
        fd.seek(self.data_offset())
        return self.data_size()

    def read_data(self, fd):
        self.seek_data(fd)
        return fd.read(self.data_size())

    def skip(self, fd):
        fd.seek(self.data_end_offset())



##########################################


class Record(BaseRecord):
    HEADER_STRUCT = struct.Struct("<4I2H")
    HEADER_SIZE = HEADER_STRUCT.size + 4

    def read_header(self, fd):
        (self.dataSize,
         self.flags,
         self.record_id,
         self.revision,
         self.version,
         self.unknown) = self.HEADER_STRUCT.unpack(
                fd.read(self.HEADER_STRUCT.size))

    def has_subrecords(self):   return True

    def read_subrecords(self, fd):
        if self.flags & self.F_COMPRESSED:
            raise Warning, "No reading of compressed data yet."
            self.skip(fd)
            return

        end_offset = self.data_end_offset()
        fd.seek(self.data_offset())

        prev_subrecord = None
        while fd.tell() < end_offset:
            subrecord = Subrecord.read(fd)
            #if prev_subrecord
            yield subrecord
            prev_subrecord = subrecord
            subrecord.skip(fd)

    F_MASTER    = 0x01
    F_DELETED   = 0x20
    F_SHIELDS   = 0x40
    F_LOCALIZED = 0x80
    F_HIDDEN    = 0x200 # REFR
    F_DEAD      = 0x200 # ACHR
    F_QUEST_ITEM= 0x400
    F_MAIN_MENU_DISPLAY= F_QUEST_ITEM # # LSCR
    F_INITIALLY_DISABLED = 0x800
    F_IGNORED   = 0x1000
    F_DANGEROUS = 0x20000 # CELL
    F_COMPRESSED =0x40000
    F_NO_WAIT   = 0x80000

    def __repr__(self):
        return "<%s %s at %08X>" % (self.__class__.__name__,
                                getattr(self, "type", "None"),
                                getattr(self, "record_id", 0))

    def flag_list(self):
        return [fname for (fname, mask) in self.__FLAGS__.items()
                        if self.flags & mask]


Record.__FLAGS__ = dict((fk,fv) for (fk,fv) in Record.__dict__.items() if fk.startswith('F_'))


@record_type('TES4')
class PluginHeader(Record): pass

@record_type('GRUP')
class Group(BaseRecord):
    HEADER_STRUCT = struct.Struct("<I4BI4H")
    HEADER_SIZE = HEADER_STRUCT.size + 4

    def read_header(self, fd):
        self.label = [0, 0, 0, 0]
        (self.groupSize,
        self.label[0], self.label[1], self.label[2], self.label[3],
        self.groupType,
        self.stamp,
        self.unknown1,
        self.version,
        self.unknown2) = self.HEADER_STRUCT.unpack(fd.read(self.HEADER_STRUCT.size))

    def record_size(self):  return self.groupSize
    def data_size(self):    return self.groupSize - self.HEADER_SIZE
    def flag_list(self):    return [] # TODO
    def has_subrecords(self): return True
    def has_subrecords(self): return False
    def read_subrecords(self, fd): return []

    def __repr__(self):
        return "<Group %s>" % (''.join(chr(c) for c in getattr(self, "label", [])))



############################################################

class Subrecord(BaseRecord):
    HEADER_STRUCT = struct.Struct("<H")
    HEADER_SIZE = HEADER_STRUCT.size + 4

    @classmethod
    def read(cls, fd):
        rec = cls()
        rec.file_offset = fd.tell()
        rec.type, = st_unpack("4s", fd.read(4))
        rec.read_header(fd)
        return rec

    def read_header(self, fd):
        self.dataSize, = self.HEADER_STRUCT.unpack(
            fd.read(self.HEADER_STRUCT.size))

    def __repr__(self):
        return "<Subrecord %s>" % (getattr(self, "type", "None"))


class SubrecordGroup:
    '''These are abstract groups of Subrecords.

    They are not themselves rendered as subrecords themselves, but their children
    are rendered, in the declared order.
    '''
    pass


###########################################################

class Scalar(Subrecord):
    # single data value
    pass

class Struct(Subrecord):
    # named sequence of data values of individual type
    pass

class Sequence(Subrecord):
    # sequence of homogenuous data values
    pass

## Data types
class DataValue(object): pass
class Blob(DataValue): pass

class NoValue(DataValue): pass # Null/zero size data

class CharSequence(DataValue): pass
class Str4(CharSequence): pass
class String(CharSequence): pass
class LString(CharSequence): pass
class Text(String): pass

### Numbers
class Number(DataValue):
    pass

class Byte(Number):
    size = 8
    python_type = int
    binary_format = '<b'

class UnsignedByte(Number):
    size = 8
    python_type = int
    binary_format = '<B'

class UnsignedInteger(Number):
    size = 32
    python_type = int
    binary_format = '<I'


class Integer(Number):
    size = 32
    python_type = int
    binary_format = '<i'


class UnsignedShort(Number):
    size = 16
    python_type = int
    binary_format = '<H'

class Short(Number):
    size = 16
    python_type = int
    binary_format = '<h'

class Float(Number):
    size = 32
    python_type = float
    binary_format = 'f'

class Long(Number):
    size = 64
    python_type = int
    binary_format = '<q'

class UnsignedLong(Number):
    size = 64
    python_type = int
    binary_format = '<Q'

class FormId(DataValue):
    size = 32
    python_type = 'int'
    binary_format = '<I'

class Reference(FormId): pass
class OwnedReference(FormId): pass


#########

class FilePath(String): pass

class Color: pass # RGBA
class Point3D: pass
class Line3D: pass
class Box3D: pass

#########


class AttributeBase(object):
    def __init__(self, field_tag, desc, data_type, size,
                    null = False): pass

class Attribute(AttributeBase): pass

class SingleSelect(Attribute): pass
class MultiSelect(Attribute): pass

class AttributeSequence(AttributeBase): pass

class SingleSelectSequence(AttributeSequence): pass
class MultiSelectSequence(AttributeSequence): pass

class ReferenceBase(AttributeBase): pass
class Reference(ReferenceBase): pass
class ReferenceSequence(ReferenceBase): pass


####################
# Descriptors - TODO

# this should be incremented by 1 and assigned to each new descriptor so that we
# can define field order when the enclosing class is finally created (in __new__)


class subrecord(OrderedDescriptor):
    def __init__(self,
                class_name,
                tag,
                null = False,
                size = None,
                default_value = None,
                fixed_value = None):

        super(subrecord, self).__init__()
        self.class_name = class_name
        self.tag = tag
        self.null = null
        self.size = size
        self.default_value = None
        self.fixed_value = None

subrecord_set = subrecord

class scalar(OrderedDescriptor):
    def __init__(self,
                tag,
                data_type,
                null = False,
                size = None,
                default_value = None,
                fixed_value = None):

        super(scalar, self).__init__()
        self.tag = tag
        self.data_type = data_type
        self.null = null
        self.size = size
        self.default_value = None
        self.fixed_value = None

scalar_set = scalar

class structure(OrderedDescriptor):
    def __init__(self,
                struct_type,
                tag,
                null = False,
                size = None,
                default_value = None,
                fixed_value = None):

        super(structure, self).__init__()
        self.struct_type = struct_type
        self.tag = tag
        self.null = null
        self.size = size
        self.default_value = None
        self.fixed_value = None

structure_set = structure


class field(OrderedDescriptor):
    def __init__(self,
            data_type,
            null = False,
            default_value = True,
            fixed_value = True):
        super(field, self).__init__()
        self.data_type = data_type
        self.null = null
        self.default_value = None
        self.fixed_value = None


field_set = field

class reference_field(OrderedDescriptor):
    def __init__(self,
            refers_to,
            null = False):
        super(reference_field, self).__init__()
        self.refers_to = refers_to
        self.null = null

reference_field_set = reference_field


class reference(OrderedDescriptor):
    def __init__(self, tag, refers_to, null = True):
        super(reference, self).__init__()

        self.refers_to = refers_to
        self.tag = tag
        self.null = null

reference_set = reference


class subrecord_group(OrderedDescriptor):
    def __init__(self, subrecord_type, null = True):
        super(subrecord_group, self).__init__()
        self.subrecord_type = subrecord_type
        self.null = null

subrecord_group_set = subrecord_group


def test_read(plugin):
    import estest
    with plugin.open() as fd:
        while True:
            rec = Record.read_from(fd)
            if rec is None: break

            print "=== %s: size %s ===" % (rec, rec.record_size())
            flag_list = rec.flag_list()
            if flag_list:
                print "flags:", ", ".join(flag_list)
            for f in rec.read_subrecords(fd):
                print "F:", f.type, repr(f.read_data(fd))
            if not rec.has_subrecords():
                rec.skip(fd)

if __name__ == '__main__':
    game = game_.Skyrim()
    plugin = game.plugins.get(game.MASTER_PLUGIN)
    #plugin = game.plugins.get("Skyrim.esm")
    test_read(plugin)
