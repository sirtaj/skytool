
import game as game_
import struct
from struct import unpack as st_unpack

RECORD_TYPES = {}
KNOWN_RECORDS = '''
'''.strip().split()

KNOWN_GROUPS = '''GMST KYWD LCRT AACT TXST GLOB CLAS FACT HDPT HAIR EYES RACE
SOUN ASPC MGEF SCPT LTEX ENCH SPEL SCRL ACTI TACT ARMO BOOK CONT DOOR INGR LIGH
MISC APPA STAT SCOL MSTT PWAT GRAS TREE CLDC FLOR FURN WEAP AMMO NPC_ LVLN KEYM
ALCH IDLM COBJ PROJ HAZD SLGM LVLI WTHR CLMT SPGD RFCT REGN NAVI CELL WRLD DIAL
QUST IDLE PACK CSTY LSCR LVSP ANIO WATR EFSH EXPL DEBR IMGS IMAD FLST PERK BPTD
ADDN AVIF CAMS CPTH VTYP MATT IPCT IPDS ARMA ECZN LCTN MESG RGDL DOBJ LGTM MUSC
FSTP FSTS SMBN SMQN SMEN DLBR MUST DLVW WOOP SHOU EQUP RELA SCEN ASTP OTFT ARTO
MATO MOVT HAZD SNDR DUAL SNCT SOPM COLL CLFM REVB'''.strip().split()
KNOWN_SUBGROUPS = '''REFR ACHR NAVM PGRE PHZD LAND INFO'''.strip().split()
EMPTY_GROUP_RECORDS = '''CLDC HAIR RGDL SCPT SCOL PWAT'''.strip().split()

def record_type(rec_tag):
    def tag_record_class(klazz):
        if rec_tag in RECORD_TYPES:
            raise AssertionError, ("trying to register %s for existing tag %s, mapped to %s" %
                            (rec_tag, klazz, RECORD_TYPES[rec_tag]))
        RECORD_TYPES[rec_tag] = klazz
        #if rec_tag not in KNOWN_TAGS:
        #    raise Warning, "Setting %s to unknown record tag %s" % (klazz, rec_tag)
        klazz.___REC___ = rec_tag

        return klazz
    return tag_record_class

HEADER_STRUCT = struct.Struct("4s4I2H")

class Record(object):
    @staticmethod
    def read_from(fd):
        rec = Record()
        rec.file_offset = fd.tell()
        (rec.type,
         rec.dataSize,
         rec.flags,
         rec.id,
         rec.revision,
         rec.version,
         rec.unknown) = HEADER_STRUCT.unpack(fd.read(HEADER_STRUCT.size))

        return rec

    def data_offset(self):
        return self.file_offset + HEADER_STRUCT.size

    def data_end_offset(self):
        return self.file_offset + HEADER_STRUCT.size + self.dataSize - 1

    def go_data(self, fd):
        '''Jump the fd to the data offset.
        Returns data length.
        '''
        fd.seek(self.file_offset + HEADER_STRUCT.size)
        return self.dataSize

    def read_data(self, fd):
        fd.seek(self.file_offset + HEADER_STRUCT.size)
        return fd.read(self.dataSize)

    def skip_past(self, fd):
        fd.seek(self.file_offset + HEADER_STRUCT.size + self.dataSize)

    def read_fields(self, fd):
        if self.flags & self.F_COMPRESSED:
            raise Warning, "No reading of compressed data yet."
            return

        end_offset = self.data_end_offset()
        fd.seek(self.data_offset())

        prev_field = None
        while fd.tell() < end_offset:
            field = Field.read(fd)
            #if prev_field
            yield field
            prev_field = field
            fd.seek(field.file_offset + field_header_struct.size + field.dataSize)

    F_MASTER    = 0x01
    F_DELETED   = 0x20
    F_SHIELDS   = 0x40
    F_LOCALIZED = 0x80
    F_HIDDEN    = 0x200 # REFR
    F_DEAD      = 0x200 # ACHR
    F_QUEST_ITEM= 0x400
    F_MENU_DISLAY= F_QUEST_ITEM # # LSCR
    F_INITIALLY_DISABLED = 0x800
    F_IGNORED   = 0x1000
    F_DANGEROUS = 0x20000 # CELL
    F_COMPRESSED =0x40000
    F_NO_WAIT   = 0x80000

    def flag_list(self):
        return [fname for (fname, mask) in self.__FLAGS__.items()
                        if self.flags & mask]

def make_flag_defrag():
    Record.__FLAGS__ = dict((k,v) for (k,v) in Record.__dict__.items() if k.startswith('F_'))

make_flag_defrag()


field_header_struct = struct.Struct("4sH")
class Field:
    @staticmethod
    def read(fd):
        f = Field()
        f.file_offset = fd.tell()
        (f.type, f.dataSize) = field_header_struct.unpack(fd.read(field_header_struct.size))
        return f
    def read_data(self, fd):
        fd.seek(self.file_offset + field_header_struct.size)
        return fd.read(self.dataSize)

@record_type('TES4')
class TES4(Record):
    pass


def test_read(plugin):
    with plugin.open() as plug:
        while True:
            rec = Record.read_from(plug)
            print "=== RECORD %s: id %s ===" % (rec.type, rec.id)
            print "flags:", rec.flag_list()
            for f in rec.read_fields(plug):
                print "F:", f.type, repr(f.read_data(plug))
            rec.skip_past(plug)

if __name__ == '__main__':
    game = game_.Skyrim()
    #plugin = game.plugins.get(game.MASTER_PLUGIN)
    plugin = game.plugins.get("zs - npc - Cass.esp")
    test_read(plugin)
