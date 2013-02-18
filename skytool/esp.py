
import game as game_
import struct
from struct import unpack as st_unpack

RECORD_TYPES = {}
KNOWN_SUBGROUPS = '''REFR ACHR NAVM PGRE PHZD LAND INFO'''.strip().split()
EMPTY_GROUP_RECORDS = '''CLDC HAIR RGDL SCPT SCOL PWAT'''.strip().split()

def record_type(rec_tag):
    def tag_record_class(klazz):
        if rec_tag in RECORD_TYPES:
            raise AssertionError,  \
                ("trying to register %s for existing tag %s, mapped to %s" %
                            (rec_tag, klazz, RECORD_TYPES[rec_tag]))
        RECORD_TYPES[rec_tag] = klazz
        klazz.___REC___ = rec_tag

        return klazz
    return tag_record_class


class BaseRecord(object):
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
    def has_subrecords(self):       return False
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
    def has_subrecords(self):   return True

    def read_subrecords(self, fd):
        if self.flags & self.F_COMPRESSED:
            #raise Warning, "No reading of compressed data yet."
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

class AttributeGroup: pass

class Subrecord(BaseRecord):
    HEADER_STRUCT = struct.Struct("<H")
    HEADER_SIZE = HEADER_STRUCT.size + 4

    @staticmethod
    def read(fd):
        rec = Subrecord()
        rec.file_offset = fd.tell()
        rec.type, = st_unpack("4s", fd.read(4))
        rec.read_header(fd)
        return rec

    def read_header(self, fd):
        self.dataSize, = self.HEADER_STRUCT.unpack(
            fd.read(self.HEADER_STRUCT.size))

    def __repr__(self):
        return "<Subrecord %s>" % (getattr(self, "type", "None"))

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
class DataValue: pass
class Blob(DataValue): pass

class NoValue(DataValue): pass # Null/zero size data

class CharSequence(DataValue): pass
class Str4(CharSequence): pass
class String(CharSequence): pass
class LString(CharSequence): pass

class Number(DataValue): pass
class Byte(Number): pass
class UnsignedByte(Number): pass
class UnsignedInteger(Number): pass
class Integer(Number): pass
class UnsignedShort(Number): pass
class Short(Number): pass
class Float(Number): pass

class FormId(DataValue): pass
class Reference(FormId): pass
class OwnedReference(FormId): pass


class FilePath: pass
class Color: pass
class Point3D: pass
class Line3D: pass
class Box3D: pass
class Text(String): pass

#########


class AttributeBase(object):
    def __init__(self, record_tag, desc, data_type, size,
                    nullable = False): pass
class Attribute(AttributeBase): pass

class SingleSelect(Attribute): pass
class MultiSelect(Attribute): pass

class AttributeSequence(AttributeBase): pass

class SingleSelectSequence(AttributeSequence): pass
class MultiSelectSequence(AttributeSequence): pass


class ReferenceAttributeBase(AttributeBase): pass
class Reference(ReferenceAttributeBase): pass
class ReferenceSequence(ReferenceAttributeBase): pass



def test_read(plugin):
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
    #plugin = game.plugins.get(game.MASTER_PLUGIN)
    plugin = game.plugins.get("LevelersTower.esm")
    test_read(plugin)
