

### WARNING: THIS IS A GENERATED FILE. HAND EDITS WILL BE LOST.

__doc__=\
"""Generated Python Model for TESVSnip RecordStructure.xml.
"""

from esp import Record, ChildGroup, Field, record_type


#### Top-level Subrecord groups ####

class CONDITIONAL (ChildGroup):
	__optional__ = True
	__repeat__ = True

class EFFECT (ChildGroup):
	__optional__ = True
	__repeat__ = True

class KEYWORDS (ChildGroup):
	__optional__ = True
	__repeat__ = True

class TINTING (ChildGroup):
	__optional__ = True
	__repeat__ = True

class MODEL_NAME (ChildGroup):
	__optional__ = False
	__repeat__ = True

class QUEST_ALID (ChildGroup):
	__optional__ = True
	__repeat__ = True

class SCEN_SCHR (ChildGroup):
	__optional__ = True
	__repeat__ = True


#### Record Types (non-group) ####

GROUP_ORDER = ['TES4', 'GMST', 'KYWD', 'LCRT', 'AACT', 'TXST', 'GLOB', 'CLAS', 'FACT', 'HDPT', 'EYES', 'RACE', 'SOUN', 'ASPC', 'MGEF', 'LTEX', 'ENCH', 'SPEL', 'SCRL', 'ACTI', 'TACT', 'ARMO', 'BOOK', 'CONT', 'DOOR', 'INGR', 'LIGH', 'MISC', 'APPA', 'STAT', 'MSTT', 'GRAS', 'TREE', 'FLOR', 'FURN', 'WEAP', 'AMMO', 'NPC_', 'LVLN', 'KEYM', 'ALCH', 'IDLM', 'COBJ', 'PROJ', 'HAZD', 'SLGM', 'LVLI', 'WTHR', 'CLMT', 'SPGD', 'RFCT', 'REGN', 'DIAL', 'INFO', 'QUST', 'IDLE', 'PACK', 'CSTY', 'LSCR', 'LVSP', 'ANIO', 'WATR', 'EFSH', 'EXPL', 'DEBR', 'IMGS', 'IMAD', 'FLST', 'PERK', 'BPTD', 'ADDN', 'AVIF', 'CAMS', 'CPTH', 'VTYP', 'MATT', 'IPCT', 'IPDS', 'ARMA', 'ECZN', 'LCTN', 'MESG', 'DOBJ', 'LGTM', 'MUSC', 'FSTP', 'FSTS', 'SMBN', 'SMQN', 'SMEN', 'DLBR', 'MUST', 'DLVW', 'WOOP', 'SHOU', 'EQUP', 'RELA', 'SCEN', 'ASTP', 'OTFT', 'ARTO', 'MATO', 'MOVT', 'SNDR', 'DUAL', 'SNCT', 'SOPM', 'COLL', 'CLFM', 'REVB', 'NAVI', 'CELL', 'REFR', 'WRLD', 'LAND', 'PHZD', 'PGRE', 'ACHR', 'NAVM']

@record_type('TES4')
class MainPluginHeader(Record):
    '''Main plugin header'''
    #  HEDR The main plugin header
    #  CNAM Plugin author
    #  SNAM Plugin description
    # ChildGroup  None
     # MAST Plugin dependencies
     # SCRN Screenshot
     # DATA DATA
    #  INTV INTV

@record_type('GMST')
class GameSetting(Record):
    '''Game setting'''
    #  EDID Editor ID
    #  DATA Setting value
    #  DATA Setting value
    #  DATA Setting value
    #  DATA Setting value

@record_type('KYWD')
class Keyword(Record):
    '''Keyword'''
    #  EDID Editor ID
    #  CNAM CNAM

@record_type('LCRT')
class LocRefType(Record):
    '''Loc Ref Type'''
    #  EDID Editor ID
    #  CNAM Marker Color

@record_type('AACT')
class Action(Record):
    '''Action'''
    #  EDID Editor ID

@record_type('TXST')
class TextureSet(Record):
    '''Texture Set'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  TX00 Diffuse Map
    #  TX01 Normal Map
    #  TX02 Glow/Skin/Hair Map
    #  TX03 Height/Parallax Map
    #  TX04 Environment Map
    #  TX05 Environment Mask Map
    #  TX07 Specular Map
    #  DODT Lighting Shader Properties
    #  DNAM DNAM

@record_type('GLOB')
class GlobalVariable(Record):
    '''Global Variable'''
    #  EDID Editor ID
    #  FNAM Value Type
    #  FLTV Value

@record_type('CLAS')
class CharacterClass(Record):
    '''Character Class'''
    #  EDID Editor ID
    #  FULL Class Name
    #  DESC Unknown - Possibly Unused
    #  DATA Class Data

@record_type('FACT')
class Faction(Record):
    '''Faction'''
    #  EDID Editor ID
    #  FULL Full Name
    #  XNAM XNAM
    #  DATA DATA
    #  JAIL Jail
    #  WAIT Jail Bed?
    #  STOL Jail Chest?
    #  PLCN PLCN
    #  CRGR Crime Group
    #  JOUT Jail Outfit?
    #  CRVA CRVA
    # ChildGroup  None
     # RNAM Rank ID
     # MNAM Rank Name?
     # FNAM FNAM
    #  VEND Vendor List
    #  VENC Vendor Chest
    #  VENV VENV
    #  PLVD PLVD (related to services)
    #  CITC Fence Factions
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2

@record_type('HDPT')
class HeadPart(Record):
    '''Head Part'''
    #  EDID Editor ID
    #  FULL Full Name
    #  MODL Model Name
    #  MODT Model Data
    #  DATA flags
    #  PNAM PNAM
    #  HNAM Additional Part
    # ChildGroup  None
     # NAM0 Option Type
     # NAM1 TRI File
    #  TNAM Base Texture
    #  RNAM Resource List

@record_type('EYES')
class Eyes(Record):
    '''Eyes'''
    #  EDID Editor ID
    #  FULL Full Name
    #  ICON ICON
    #  DATA DATA

@record_type('RACE')
class RaceCreatureType(Record):
    '''Race / Creature Type'''
    #  EDID Editor ID
    #  FULL Full Name
    #  DESC Description
    #  SPCT Spell Count
    #  SPLO Learned Spell
    #  WNAM Naked Armor
    #  BODT BODT
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    # ChildGroup  None
     # DATA Actor Values
     # ChildGroup MODEL_NAME
         # ChildGroup None
             # MNAM MNAM
             # INDX INDX
             # ANAM ANAM
             # MODL Model Name
             # MODT Model Data
         # ChildGroup None
             # FNAM FNAM
             # INDX INDX
             # ANAM ANAM
             # MODL Model Name
             # MODT Model Data
     # MTNM MTNM
     # VTCK Voice Type
     # DNAM Decapitated Head
     # HCLF Hair Color
     # TINL TINL
     # PNAM PNAM
     # UNAM UNAM
     # ChildGroup None
         # ATKD ATKD
         # ATKE ATKE
    # ChildGroup  None
     # NAM1 NAM1
     # ChildGroup MODEL_NAME
         # ChildGroup None
             # MNAM MNAM
             # INDX INDX
             # ANAM ANAM
             # MODL Model Name
             # MODT Model Data
         # ChildGroup None
             # FNAM FNAM
             # INDX INDX
             # ANAM ANAM
             # MODL Model Name
             # MODT Model Data
     # GNAM GNAM
    # ChildGroup  None
     # NAM3 NAM3
     # ChildGroup MODEL_NAME
         # ChildGroup None
             # MNAM MNAM
             # INDX INDX
             # ANAM ANAM
             # MODL Model Name
             # MODT Model Data
         # ChildGroup None
             # FNAM FNAM
             # INDX INDX
             # ANAM ANAM
             # MODL Model Name
             # MODT Model Data
    #  NAM4 NAM4
    #  NAM5 NAM5
    #  NAM7 NAM7
    #  ONAM ONAM
    #  LNAM LNAM
    #  NAME NAME
    # ChildGroup  None
     # MTYP MTYP
     # SPED SPED
    #  VNAM VNAM
    #  QNAM QNAM
    #  UNES UNES
    #  PHTN PHTN
    #  PHWT PHWT
    #  WKMV WKMV
    #  RNMV RNMV
    #  SWMV SWMV
    #  FLMV FLMV
    #  SNMV SNMV
    # ChildGroup  None
     # ChildGroup None
         # NAM0 NAM0
         # ChildGroup MODEL_NAME
             # ChildGroup None
                 # MNAM MNAM
                 # INDX INDX
                 # ANAM ANAM
                 # MODL Model Name
                 # MODT Model Data
             # ChildGroup None
                 # FNAM FNAM
                 # INDX INDX
                 # ANAM ANAM
                 # MODL Model Name
                 # MODT Model Data
     # ChildGroup None
         # HEAD HEAD
         # INDX INDX
     # ChildGroup None
         # MPAI MPAI
         # MPAV MPAV
     # ChildGroup None
         # RPRM Male Presets
         # AHCM Male Hair Color Preset
         # FTSM FTSM
         # DFTM DFTM
         # ChildGroup TINTING
             # TINI TINI
             # TINT TINT
             # TINP TINP
             # TIND TIND
             # ChildGroup None
                 # TINC TINC
                 # TINV TINV
                 # TIRS TIRS
     # ChildGroup None
         # RPRF Female Presets
         # AHCF Female Hair Color Preset
         # FTSF FTSF
         # DFTF DFTF
         # ChildGroup TINTING
             # TINI TINI
             # TINT TINT
             # TINP TINP
             # TIND TIND
             # ChildGroup None
                 # TINC TINC
                 # TINV TINV
                 # TIRS TIRS
    #  NAM8 NAM8
    #  RNAM RNAM

@record_type('SOUN')
class Sound(Record):
    '''Sound'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FNAM File name
    #  SNDD Sound Data?
    #  SDSC Sound

@record_type('ASPC')
class AcousticSpace(Record):
    '''Acoustic Space'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  SNAM Ambient
    #  RDAT Region Data
    #  BNAM Reverb

@record_type('MGEF')
class MagicEffect(Record):
    '''Magic Effect'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  FULL Full Name
    #  MDOB MDOB
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DATA Effect data
    #  SNDD SNDD
    #  DNAM DNAM
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2

@record_type('LTEX')
class LandTexture(Record):
    '''Land Texture'''
    #  EDID Editor ID
    #  TNAM Texture
    #  MNAM Material
    #  HNAM Havok Data?
    #  SNAM Texture Specular Exponent?
    #  GNAM Grass

@record_type('ENCH')
class Enchantment(Record):
    '''Enchantment'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Name
    #  ENIT Enchantment Info and Type ??
    # ChildGroup  EFFECT
     # EFID EFID
     # EFIT EFIT
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2

@record_type('SPEL')
class Spell(Record):
    '''Spell'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Name
    #  MDOB MDOB
    #  ETYP ETYP
    #  DESC Description
    #  SPIT Spell Info and Type ??
    # ChildGroup  EFFECT
     # EFID EFID
     # EFIT EFIT
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2

@record_type('SCRL')
class Scroll(Record):
    '''Scroll'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  MDOB Inv Icon
    #  ETYP Equip Type
    #  DESC Description
    #  MODL Ground Model Path
    #  MODT Model Struct
    #  DATA DATA
    #  SPIT Spell Info and Type ??
    # ChildGroup  EFFECT
     # EFID EFID
     # EFIT EFIT
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2

@record_type('ACTI')
class Activator(Record):
    '''Activator'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model Name
    #  MODT Model Data
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  MODS MODS
    #  DEST Destruction Data
    # ChildGroup  None
     # DSTD DSTD
     # DMDL DMDL
     # DMDT DMDT
     # DMDS DMDS
     # DSTF DSTF
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  PNAM PNAM
    #  SNAM Ambient? Sound
    #  WNAM Water
    #  VNAM Use Sound
    #  RNAM Verbe String
    #  FNAM Flags
    #  KNAM Keyword

@record_type('TACT')
class TalkingActivator(Record):
    '''Talking Activator'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model file
    #  MODT Model Data
    #  PNAM PNAM
    #  FNAM FNAM
    #  VNAM Voice Type

@record_type('ARMO')
class Armor(Record):
    '''Armor'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Full Item Name
    #  EITM EnchantmentID
    #  MOD2 Male Ground Model Path
    #  MO2T Model Data 2
    #  MO2S Model Data 2S
    #  MOD4 Female Ground Model Path
    #  MO4T Model Data 4
    #  MO4S Model Data 4S
    #  BODT Body Template
    #  ETYP Equipment Type
    #  BIDS Bash Impact Data Set
    #  BAMT Bash Material
    #  YNAM Pick Up Sound Ref
    #  ZNAM Drop Sound Ref
    #  RNAM Race
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DESC Item Description
    #  MODL Model Path
    #  DATA Armor Data
    #  DNAM Damage Resistance(DR) -- actual DR is this value*0.01
    #  TNAM Message Type (??)

@record_type('BOOK')
class Book(Record):
    '''Book'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Book Name
    #  MODL Book Model
    #  MODT Model Data ?? Blob
    #  DESC Book Description - Sometimes a copy of the book name.
    #  YNAM Pick Up Sound Ref
    #  ZNAM Drop Sound Ref
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DATA Book Settings
    #  INAM STAT Model
    #  CNAM Alternate Text

@record_type('CONT')
class Container(Record):
    '''Container'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Name
    #  MODL Model NIF
    #  MODT Model Data
    #  MODS MODS
    #  COCT COCT
    #  CNTO Container List Item
    #  CNAM CNAM
    #  COED CND extra data
    #  DATA Container Data
    #  SNAM Sound Record - Open
    #  QNAM Sound Record - Close

@record_type('DOOR')
class Door(Record):
    '''Door'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model File
    #  MODT Model Data
    #  MODS MODS
    #  SNAM SNAM
    #  ANAM ANAM
    #  FNAM Flags

@record_type('INGR')
class Ingredient(Record):
    '''Ingredient'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Full Name
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  MODL Model Name
    #  MODT Model Data
    #  YNAM Pick Up Sound Ref
    #  ZNAM Drop Sound Ref
    #  DATA DATA
    #  ENIT ENIT
    # ChildGroup  EFFECT
     # EFID EFID
     # EFIT EFIT
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2

@record_type('LIGH')
class LightTemplate(Record):
    '''Light Template'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  MODL Model Name
    #  MODT Model Data
    #  FULL Full Name
    #  DATA DATA
    #  FNAM FNAM
    #  SNAM SNAM

@record_type('MISC')
class MiscItem(Record):
    '''Misc Item'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Item Name
    #  MODL Item Model
    #  MODT Model Data
    #  ICON Item Icon
    #  YNAM Pick Up Sound Ref
    #  ZNAM Drop Sound Ref
    #  MODS MODS
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DATA Item Data

@record_type('APPA')
class Apparatus(Record):
    '''Apparatus'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    #  QUAL Quality
    #  DESC Description
    #  DATA DATA

@record_type('STAT')
class Static(Record):
    '''Static'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  MODL Model Name
    #  MODT Model Data
    #  MODS MODS
    #  DNAM DNAM
    #  MNAM MNAM

@record_type('MSTT')
class MovableStatic(Record):
    '''Movable Static'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  MODL Model Name
    #  MODT Model Data
    #  DEST Destruction Data
    # ChildGroup  None
     # DSTD DSTD
     # DMDL Destroyed Model
     # DMDT Destroyed Model Data
     # DSTF DSTF
    #  MODS MODS
    #  DATA DATA
    #  SNAM Ambient Sound

@record_type('GRAS')
class Grass(Record):
    '''Grass'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  MODL Model Name
    #  MODT Model Data
    #  DATA DATA

@record_type('TREE')
class Tree(Record):
    '''Tree'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  MODL Model Name
    #  MODT Model Data
    #  PFIG Result Item
    #  SNAM Use Sound
    #  PFPC Percent Chance?
    #  FULL Full Name
    #  CNAM CNAM

@record_type('FLOR')
class Flora(Record):
    '''Flora'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model Name
    #  MODT Model Data
    #  MODS MODS
    #  PNAM PNAM
    #  RNAM Verb String
    #  FNAM Flags?
    #  PFIG Result Item
    #  SNAM Use Sound
    #  PFPC Percent Chance?

@record_type('FURN')
class Furniture(Record):
    '''Furniture'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model Name
    #  MODT Model Data
    #  DEST Destruction Data
    # ChildGroup  None
     # DSTD DSTD
     # DSTF DSTF
    #  MODS MODS
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  PNAM PNAM
    #  FNAM FNAM
    #  KNAM KNAM
    #  MNAM MNAM
    #  WBDT WBDT
    # ChildGroup  None
     # ENAM ENAM
     # ChildGroup None
         # NAM0 NAM0
         # FNMK FNMK
    #  FNPR FNPR
    #  XMRK XMRK

@record_type('WEAP')
class Weapon(Record):
    '''Weapon'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Name
    #  MODL Model NIF
    #  MODT Model Data
    #  MODS MODS
    #  EITM Enchantment Record
    #  EAMT Enchantment Charge Amount
    #  ETYP Equip Type
    #  BIDS Weapon Bash Impact Set
    #  BAMT Weapon Bash Material
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DESC Item Description
    #  NNAM Projectile Node
    #  INAM Impact Data Set Record
    #  SNAM Sound Record - Gun - Shoot 3D
    #  WNAM World Static Record
    #  TNAM Sound Record - Melee - Swing / Gun - No Ammo
    #  UNAM Sound Record - Idle
    #  NAM9 Sound Record - Equip
    #  NAM8 Sound Record - Unequip
    #  DATA Weapon Data
    #  DNAM Damage Data
    #  CRDT Critical Damage Data
    #  VNAM Silenced yes/no
    #  CNAM Stage Description

@record_type('AMMO')
class AmmunitionType(Record):
    '''Ammunition Type'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Ammo Model
    #  MODT Model Data
    #  YNAM Pick Up Sound Ref
    #  ZNAM Drop Sound Ref
    #  DESC Description
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DATA Ammo Settings

@record_type('NPC_')
class NpcPackage(Record):
    '''NPC Package'''
    #  EDID Editor ID
    #  VMAD Script Packages
    #  OBND Object Bounds
    #  ACBS ACBS Data
    #  SNAM Faction
    #  INAM Death Item
    #  VTCK Voice Type
    #  TPLT Template NPC
    #  RNAM Race
    #  DEST Destruction Data
    #  DSTD DSTD
    #  DSTF DSTF
    #  SPOR SPOR
    #  SPCT Spell Book Count
    #  SPLO Spell Book List
    #  WNAM World Static Record
    #  ANAM ANAM
    #  ATKR Attack Race
    #  ATKD ATKD
    #  ATKE ATKE
    #  ECOR ECOR
    #  PRKZ Perk Count
    #  PRKR Perk
    #  COCT Container Count
    #  CNTO Container Item
    #  AIDT AIDT
    #  PKID PKID
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  CNAM Class Name
    #  FULL Full Name
    #  SHRT Short Name
    #  DATA Data
    #  DNAM DNAM
    #  PNAM Head Parts
    #  HCLF Hair Color
    #  ZNAM ZNAM
    #  GNAM GNAM
    #  NAM5 NAM5
    #  NAM6 Body Scale
    #  NAM7 Body Morph Slider
    #  NAM8 NAM8
    # ChildGroup  None
     # CSDT Sound Template
     # CSDI Sound Recording
     # CSDC Sound Level?
    #  CSCR CSCR Template
    #  DOFT Daily Outfit
    #  SOFT Sleep Outfit
    #  DPLT Daily Package List
    #  CRIF Crime Faction
    #  FTST Complexion Texture
    #  QNAM QNAME
    #  NAM9 Facial Morph Sliders?
    #  NAMA Face parts
    # ChildGroup  None
     # TINI Tint Mask Index?
     # TINC Tint Mask Color?
     # TINV Tint Mask Value?
     # TIAS TIAS

@record_type('LVLN')
class LeveledActor(Record):
    '''Leveled Actor'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  LVLD Chance None Value
    #  LVLF List Flags
    #  LLCT Count of Level Items
    # ChildGroup  None
     # LVLO Level
     # COED COED
    #  MODL Model Name
    #  MODT Model Data

@record_type('KEYM')
class Key(Record):
    '''Key'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model Name
    #  MODT Model Data
    #  YNAM Pick Up Sound Ref
    #  ZNAM Drop Sound Ref
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DATA DATA

@record_type('ALCH')
class Potion(Record):
    '''Potion'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Name
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  MODL Model NIF
    #  MODT MODT ??
    #  MODS MODS
    #  YNAM Pick Up Sound Ref
    #  ZNAM Drop Sound Ref
    #  DATA Item Data
    #  ENIT 'Enchantment' Info and Type
    # ChildGroup  EFFECT
     # EFID EFID
     # EFIT EFIT
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2

@record_type('IDLM')
class IdleForm(Record):
    '''Idle Form'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  IDLF IDLF
    #  IDLC Idle Count
    #  IDLT IDLT
    #  IDLA Idle Animations

@record_type('COBJ')
class ConstructibleObjects(Record):
    '''Constructible Objects (Recipes)'''
    #  EDID Editor ID
    #  COCT Component Count
    #  CNTO Component Object
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  CNAM Output Object
    #  BNAM Required Crafting Station (KYWD)
    #  NAM1 Resulting Quantity

@record_type('PROJ')
class Projectile(Record):
    '''Projectile'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model NIF
    #  MODT Model Data
    #  DEST Destruction Start
    # ChildGroup  None
     # DSTD Destruction Data
     # DSTF Destruction Footer
    #  DATA Projectile Data
    #  NAM1 Effect NIF
    #  NAM2 Effect Data ??
    #  VNAM Silenced yes/no

@record_type('HAZD')
class Hazard(Record):
    '''Hazard'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model Name
    #  MODT Model Data
    #  MNAM MNAM
    #  DATA DATA

@record_type('SLGM')
class SoulGem(Record):
    '''Soul Gem'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model Name
    #  MODT Model Data
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  DATA DATA
    #  SOUL Current Soul
    #  SLCP Soul Gem Capacity
    #  NAM0 NAM0

@record_type('LVLI')
class LeveledItem(Record):
    '''Leveled Item'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  LVLD Chance None Value
    #  LVLF List Flags
    #  LVLG Global
    #  LLCT Leveled Item Count
    #  LVLO List Item

@record_type('WTHR')
class Weather(Record):
    '''Weather'''
    #  EDID EDID
    #  DNAM DNAM
    #  CNAM CNAM
    #  ANAM ANAM
    #  BNAM BNAM
    #  00TX Dynamic Cloud Texture
    #  10TX Dynamic Cloud Texture
    #  20TX Dynamic Cloud Texture
    #  30TX Dynamic Cloud Texture
    #  40TX Dynamic Cloud Texture
    #  50TX Dynamic Cloud Texture
    #  60TX Dynamic Cloud Texture
    #  70TX Dynamic Cloud Texture
    #  80TX Dynamic Cloud Texture
    #  90TX Dynamic Cloud Texture
    #  :0TX :Dynamic Cloud Texture
    #  ;0TX Dynamic Cloud Texture
    #  <0TX Dynamic Cloud Texture
    #  =0TX Dynamic Cloud Texture
    #  >0TX Dynamic Cloud Texture
    #  ?0TX Dynamic Cloud Texture
    #  @0TX Dynamic Cloud Texture
    #  A0TX Dynamic Cloud Texture
    #  B0TX Dynamic Cloud Texture
    #  C0TX Dynamic Cloud Texture
    #  D0TX Dynamic Cloud Texture
    #  E0TX Dynamic Cloud Texture
    #  F0TX Dynamic Cloud Texture
    #  G0TX Dynamic Cloud Texture
    #  H0TX Dynamic Cloud Texture
    #  I0TX Dynamic Cloud Texture
    #  J0TX Dynamic Cloud Texture
    #  K0TX Dynamic Cloud Texture
    #  L0TX Dynamic Cloud Texture
    #  LNAM LNAM
    #  MNAM MNAM
    #  NNAM NNAM
    #  ONAM ONAM
    #  RNAM RNAM
    #  QNAM QNAM
    #  PNAM PNAM
    #  JNAM JNAM
    #  NAM0 NAM0
    #  FNAM FNAM
    #  DATA DATA
    #  NAM1 NAM1
    #  SNAM Sound Reference
    #  TNAM Static Clouds
    #  IMSP Image Spaces
    #  DALC DALC
    #  NAM2 NAM2
    #  NAM3 NAM3
    #  MODL MODL
    #  MODT MODT

@record_type('CLMT')
class Climate(Record):
    '''Climate'''
    #  EDID Editor ID
    #  WLST WLST
    #  FNAM FNAM
    #  GNAM GNAM
    #  MODL Model Name
    #  MODT Model Data
    #  TNAM TNAM

@record_type('SPGD')
class ShaderParticleGeometry(Record):
    '''Shader Particle Geometry'''
    #  EDID Editor ID
    #  DATA DATA
    #  ICON ICON

@record_type('RFCT')
class Refraction(Record):
    '''Refraction'''
    #  EDID Editor ID
    #  DATA DATA

@record_type('REGN')
class Region(Record):
    '''Region (Audio/Weather)'''
    #  EDID Editor ID
    #  RCLR RCLR
    #  WNAM WNAM
    # ChildGroup  None
     # RPLI RPLI
     # RPLD RPLD
    # ChildGroup  None
     # RDAT RDAT
     # ICON ICON
     # RDOT RDOT
     # RDMO RDMO
     # RDWT RDWT
     # RDMP RDMP
     # RDSA RDSA

@record_type('DIAL')
class DialogueTopic(Record):
    '''Dialogue Topic'''
    #  EDID Editor ID
    #  FULL Topic Text
    #  PNAM Topic Priority
    #  BNAM BNAM
    #  QNAM QNAM
    #  DATA Unknown Data 2
    #  SNAM SNAM
    #  TIFC TIFC

@record_type('INFO')
class DialogueInfo(Record):
    '''Dialogue Info'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  ENAM ENAM
    #  DATA Unknown Data
    #  PNAM PNAM
    #  CNAM CNAM
    #  TCLT Linked To Topic
    #  DNAM DNAM
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    # ChildGroup  None
     # SCHR SCHR
     # QNAM QNAM
     # NEXT Separator
    # ChildGroup  None
     # TRDT Topic Response Data
     # NAM1 Dialogue Text
     # NAM2 Uknown Byte
     # NAM3 Uknown Byte
     # SNAM Idle Record
    #  LNAM LNAM
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    # ChildGroup  None
     # ANAM Next Speaker
     # RNAM RNAM
    #  TWAT TWAT
    #  ONAM ONAM

@record_type('QUST')
class Quest(Record):
    '''Quest'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  FULL Full Name
    #  DNAM DNAM
    #  ENAM ENAM
    #  NEXT Separator
    # ChildGroup  None
     # QTGL QTGL
     # NEXT NEXT
    # ChildGroup  None
     # FLTR FLTR
     # NEXT NEXT
    # ChildGroup  None
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2
     # CNAM CNAM
     # NEXT Separator
    # ChildGroup  None
     # INDX Quest Stage
     # ChildGroup None
         # QSDT Quest Stage Data
         # NAM0 NAM0
         # ChildGroup CONDITIONAL
             # CTDA Conditional
             # CIS1 CIS1
             # CIS2 CIS2
         # CNAM CNAM
         # SCHR SCHR
         # SCTX SCTX
         # QNAM QNAM
    # ChildGroup  None
     # QOBJ QOBJ
     # FNAM FNAM
     # NNAM NNAM
     # ChildGroup None
         # QSTA QSTA
         # ChildGroup CONDITIONAL
             # CTDA Conditional
             # CIS1 CIS1
             # CIS2 CIS2
    #  NEXT Separator
    #  ANAM ANAM
    # ChildGroup  None
     # ALST ALST
     # ChildGroup QUEST_ALID
         # ALID ALID
         # FNAM FNAM
         # ALFA ALFA
         # ALRT ALRT
         # ALNA ALNA
         # ALNT ALNT
         # ALEQ ALEQ
         # ALEA ALEA
         # NNAM NNAM
         # QSTA QSTA
         # ALFI ALFI
         # ALFR ALFR
         # ALFE ALFE
         # ALFD ALFD
         # ALCO ALCO
         # ALCA ALCA
         # ALCL ALCL
         # ALUA ALUA
         # ChildGroup CONDITIONAL
             # CTDA Conditional
             # CIS1 CIS1
             # CIS2 CIS2
         # ChildGroup KEYWORDS
             # KSIZ Number of Keywords
             # KWDA Keyword List
         # COCT COCT
         # CNTO CNTO
         # SPOR SPOR
         # ECOR ECOR
         # ALDN ALDN
         # ALSP ALSP
         # ALFC ALFC
         # ALPC ALPC
         # VTCK VTCK
         # KNAM KNAM
         # ALFL ALFL
         # ALED ALED
    # ChildGroup  None
     # ChildGroup None
         # ALLS ALLS
         # ChildGroup QUEST_ALID
             # ALID ALID
             # FNAM FNAM
             # ALFA ALFA
             # ALRT ALRT
             # ALNA ALNA
             # ALNT ALNT
             # ALEQ ALEQ
             # ALEA ALEA
             # NNAM NNAM
             # QSTA QSTA
             # ALFI ALFI
             # ALFR ALFR
             # ALFE ALFE
             # ALFD ALFD
             # ALCO ALCO
             # ALCA ALCA
             # ALCL ALCL
             # ALUA ALUA
             # ChildGroup CONDITIONAL
                 # CTDA Conditional
                 # CIS1 CIS1
                 # CIS2 CIS2
             # ChildGroup KEYWORDS
                 # KSIZ Number of Keywords
                 # KWDA Keyword List
             # COCT COCT
             # CNTO CNTO
             # SPOR SPOR
             # ECOR ECOR
             # ALDN ALDN
             # ALSP ALSP
             # ALFC ALFC
             # ALPC ALPC
             # VTCK VTCK
             # KNAM KNAM
             # ALFL ALFL
             # ALED ALED
     # ChildGroup None
         # ALST ALST
         # ChildGroup QUEST_ALID
             # ALID ALID
             # FNAM FNAM
             # ALFA ALFA
             # ALRT ALRT
             # ALNA ALNA
             # ALNT ALNT
             # ALEQ ALEQ
             # ALEA ALEA
             # NNAM NNAM
             # QSTA QSTA
             # ALFI ALFI
             # ALFR ALFR
             # ALFE ALFE
             # ALFD ALFD
             # ALCO ALCO
             # ALCA ALCA
             # ALCL ALCL
             # ALUA ALUA
             # ChildGroup CONDITIONAL
                 # CTDA Conditional
                 # CIS1 CIS1
                 # CIS2 CIS2
             # ChildGroup KEYWORDS
                 # KSIZ Number of Keywords
                 # KWDA Keyword List
             # COCT COCT
             # CNTO CNTO
             # SPOR SPOR
             # ECOR ECOR
             # ALDN ALDN
             # ALSP ALSP
             # ALFC ALFC
             # ALPC ALPC
             # VTCK VTCK
             # KNAM KNAM
             # ALFL ALFL
             # ALED ALED

@record_type('IDLE')
class IdleAnimation(Record):
    '''Idle Animation'''
    #  EDID Editor ID
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  DNAM Havok File
    #  ENAM ENAM
    #  ANAM Animations
    #  DATA DATA

@record_type('PACK')
class AiPackage(Record):
    '''AI Package'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  PKDT PKDT
    #  PSDT PSDT
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  CNAM CNAM
    #  IDLF IDLF
    #  IDLC IDLC
    #  IDLT IDLT
    #  IDLA IDLA
    #  QNAM QNAM
    #  PKCU PKCU
    # ChildGroup  None
     # ANAM ANAM
     # TPIC TPIC
     # CNAM CNAM
     # PLDT PLDT
     # PTDA PTDA
     # PDTO PDTO
     # UNAM UNAM
     # XNAM XNAM
     # CITC CITC
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2
     # PRCB PRCB
     # PNAM PNAM
     # FNAM FNAM
     # PKC2 PKC2
     # PFOR PFOR
     # PFO2 PFO2
    # ChildGroup  None
     # UNAM UNAM
     # BNAM BNAM
     # PNAM PNAM
    #  POBA POBA
    # ChildGroup  None
     # INAM INAM
     # SCHR SCHR
     # TNAM TNAM
     # SCDA SCDA
     # SCTX SCTX
     # QNAM QNAM
     # PDTO PDTO
     # POEA POEA
     # POCA POCA

@record_type('CSTY')
class CombatStyle(Record):
    '''Combat Style'''
    #  EDID Editor ID
    #  CSGD CSGD
    #  CSMD CSMD
    #  CSME CSME
    #  CSCR CSCR
    #  CSLR CSLR
    #  CSFL CSFL
    #  DATA DATA

@record_type('LSCR')
class LoadScreen(Record):
    '''Load Screen'''
    #  EDID Editor ID
    #  DESC Description
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  NNAM NNAM
    #  SNAM SNAM
    #  RNAM RNAM
    #  ONAM ONAM
    #  XNAM XNAM
    #  MOD2 Camera NIF

@record_type('LVSP')
class LeveledSpell(Record):
    '''Leveled Spell'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  LVLD Chance
    #  LVLF Leveled List Flags
    #  LLCT List Item Count
    #  LVLO LVLO

@record_type('ANIO')
class AnimatedObject(Record):
    '''Animated Object'''
    #  EDID Editor ID
    #  MODL Model Name
    #  MODT Model Data
    #  BNAM BNAM

@record_type('WATR')
class Water(Record):
    '''Water'''
    #  EDID Editor ID
    #  FULL Full Name
    #  NNAM NNAM
    #  ANAM ANAM
    #  FNAM FNAM
    #  TNAM TNAM
    #  MNAM MNAM
    #  SNAM SNAM
    #  DATA DATA
    #  DNAM DNAM
    #  GNAM GNAM
    #  NAM0 NAM0
    #  NAM1 NAM1

@record_type('EFSH')
class EffectShader(Record):
    '''Effect Shader'''
    #  EDID Editor ID
    #  ICON ICON
    #  ICO2 ICO2
    #  NAM7 NAM7
    #  NAM8 NAM8
    #  NAM9 NAM9
    #  DATA DATA

@record_type('EXPL')
class Explosions(Record):
    '''Explosions'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  FULL Full Name
    #  MODL Model NIF
    #  MODT Model Data
    #  EITM Enchantment Record
    #  MNAM Audio Space Record
    #  DATA Explosion Data

@record_type('DEBR')
class Debris(Record):
    '''Debris'''
    #  EDID Editor ID
    # ChildGroup  None
     # DATA DATA
     # MODT Model Data

@record_type('IMGS')
class ImageSpace(Record):
    '''Image Space'''
    #  EDID Editor ID
    #  ENAM ENAM
    #  HNAM HNAM
    #  CNAM CNAM
    #  TNAM TNAM
    #  DNAM DNAM

@record_type('IMAD')
class ImageSpaceModifier(Record):
    '''Image Space Modifier'''
    #  EDID Editor ID
    #  DNAM DNAM
    #  BNAM BNAM
    #  VNAM VNAM
    #  TNAM TNAM
    #  NAM3 NAM3
    #  RNAM RNAM
    #  SNAM SNAM
    #  UNAM UNAM
    #  NAM1 NAM1
    #  NAM2 NAM2
    #  WNAM WNAM
    #  XNAM XNAM
    #  YNAM YNAM
    #  ZNAM ZNAM
    #  NAM4 NAM4
    #  &#x0;IAD &#x0;IAD
    #  @IAD @IAD
    #  &#x1;IAD &#x1;IAD
    #  AIAD AIAD
    #  &#x2;IAD &#x2;IAD
    #  BIAD BIAD
    #  &#x3;IAD &#x3;IAD
    #  CIAD CIAD
    #  &#x4;IAD &#x4;IAD
    #  DIAD DIAD
    #  &#x5;IAD &#x5;IAD
    #  EIAD EIAD
    #  &#x6;IAD &#x6;IAD
    #  FIAD FIAD
    #  &#x7;IAD &#x7;IAD
    #  GIAD GIAD
    #  &#x8;IAD &#x8;IAD
    #  HIAD HIAD
    #  &#x9;IAD &#x9;IAD
    #  IIAD IIAD
    #  &#xA;IAD &#xA;IAD
    #  JIAD JIAD
    #  &#xB;IAD &#xB;IAD
    #  KIAD KIAD
    #  &#xC;IAD &#xC;IAD
    #  LIAD LIAD
    #  &#xD;IAD &#xD;IAD
    #  MIAD MIAD
    #  &#xE;IAD &#xE;IAD
    #  NIAD NIAD
    #  &#xF;IAD &#xF;IAD
    #  OIAD OIAD
    #  &#x10;IAD &#x10;IAD
    #  PIAD PIAD
    #  &#x11;IAD &#x11;IAD
    #  QIAD QIAD
    #  &#x12;IAD &#x12;IAD
    #  RIAD RIAD
    #  &#x13;IAD &#x13;IAD
    #  SIAD SIAD
    #  &#x14;IAD &#x14;IAD
    #  TIAD TIAD

@record_type('FLST')
class FormIdList(Record):
    '''Form ID List'''
    #  EDID Editor ID
    #  LNAM List Item

@record_type('PERK')
class Perk(Record):
    '''Perk'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  FULL Perk Name
    #  DESC Perk Description
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  DATA Perk Data
    #  NNAM NNAM
    # ChildGroup  None
     # PRKE Rank Effect Header
     # DATA Perk Effect Data
     # DATA Perk Effect Data
     # DATA Perk Effect Data
     # ChildGroup None
         # PRKC Conditional Info
         # ChildGroup CONDITIONAL
             # CTDA Conditional
             # CIS1 CIS1
             # CIS2 CIS2
     # EPFT Extra Data Type
     # EPF2 ==> Script Data 2 ??
     # EPF3 ==> Script Data 3 ?? Always 00 00
     # EPFD ==> Float Value
     # EPFD ==> 8 Byte Struct
     # EPFD ==> FormID
     # EPFD ==> FormID
     # EPFD ==> Spell
     # EPFD ==> zString
     # EPFD ==> lString
     # PRKF  Rank Effect Footer 

@record_type('BPTD')
class BodyPart(Record):
    '''Body Part'''
    #  EDID Editor ID
    #  MODL Model Name
    #  MODT Model Data
    # ChildGroup  None
     # BPTN Body Part Name
     # BPNN Body Part Node Name
     # BPNT Body Part Node Title
     # BPNI Body Part Node Info
     # BPND Body Part Node Data
     # NAM1 NAM1
     # NAM4 NAM4
     # NAM5 NAM5

@record_type('ADDN')
class Nodes(Record):
    '''Add-On Nodes'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  MODL Effect NIF
    #  MODT Model Data
    #  DATA Unique ID?
    #  DNAM Type??

@record_type('AVIF')
class ActorValueInfo(Record):
    '''Actor Value Info'''
    #  EDID Editor ID
    #  FULL Full Name
    #  DESC Description
    #  ANAM Alternate Name
    #  CNAM CNAM
    #  AVSK AVSK
    # ChildGroup  None
     # PNAM Perk Name
     # FNAM FNAM
     # XNAM XNAM
     # YNAM YNAM
     # HNAM HNAM
     # VNAM VNAM
     # SNAM Skill
     # CNAM Unlocks
     # INAM INAM

@record_type('CAMS')
class CameraShot(Record):
    '''Camera Shot'''
    #  EDID Editor ID
    #  MODL Model Name
    #  MODT Model Data
    #  DATA DATA
    #  MNAM MNAM

@record_type('CPTH')
class CameraPath(Record):
    '''Camera Path'''
    #  EDID Editor ID
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  ANAM ANAM
    #  DATA DATA
    #  SNAM SNAM

@record_type('VTYP')
class VoiceType(Record):
    '''Voice Type'''
    #  EDID Editor ID
    #  DNAM Voice Type Data

@record_type('MATT')
class MaterialType(Record):
    '''Material Type'''
    #  EDID Editor ID
    #  PNAM PNAM
    #  MNAM MNAM
    #  CNAM CNAM
    #  BNAM BNAM
    #  FNAM FNAM
    #  HNAM HNAM

@record_type('IPCT')
class ImpactData(Record):
    '''Impact Data'''
    #  EDID Editor ID
    #  MODL Impact NIF
    #  MODT Model Data ??
    #  DATA Impact Data
    #  DODT ?? Data
    #  DNAM Decal Type Record
    #  ENAM ENAM
    #  SNAM Sound Type Record
    #  NAM1 NAM1
    #  NAM2 NAM2

@record_type('IPDS')
class ImpactDataSet(Record):
    '''Impact Data Set'''
    #  EDID Editor ID
    #  PNAM PNAM

@record_type('ARMA')
class Armature(Record):
    '''Armature'''
    #  EDID Editor ID
    #  BODT Unknown
    #  RNAM RNAM
    #  DNAM Type??
    #  MOD2 Model NIF 2
    #  MO2T Model Data 2
    #  MO2S MO2S
    #  MOD3 Model NIF 3
    #  MO3T Model Data 3
    #  MO3S MO3S
    #  MOD4 Model NIF 4
    #  MO4T Model Data 4
    #  MO4S MO4S
    #  MOD5 Model NIF 5
    #  MO5T Model Data 5
    #  NAM0 Base Male Texture
    #  NAM1 Base Female Texture
    #  NAM2 Base Male 1st Texture
    #  NAM3 Base Female 1st Texture
    #  MODL Included Race
    #  SNDD Footstep Sound

@record_type('ECZN')
class EncounterZone(Record):
    '''Encounter Zone'''
    #  EDID Editor ID
    #  DATA ECZN Data

@record_type('LCTN')
class Location(Record):
    '''Location'''
    #  EDID Editor ID
    #  LCPR Unique Refs
    #  LCUN LCUN
    #  LCSR Static Refs
    #  LCEC Encounter
    #  LCID LCID
    #  LCEP Enable Points
    #  FULL Full Name
    # ChildGroup  KEYWORDS
     # KSIZ Number of Keywords
     # KWDA Keyword List
    #  PNAM Parent Location
    #  FNAM FNAM
    #  NAM1 Music
    #  MNAM Marker
    #  RNAM RNAM
    #  NAM0 NAM0
    #  CNAM CNAM

@record_type('MESG')
class GameMessages(Record):
    '''Game messages'''
    #  EDID Editor ID
    #  DESC Description
    #  FULL Screen name
    #  INAM INAM
    #  QNAM Quest
    #  DNAM Description Type (??)
    #  TNAM Message Type (??)
    # ChildGroup  None
     # ITXT Button 1
     # ChildGroup CONDITIONAL
         # CTDA Conditional
         # CIS1 CIS1
         # CIS2 CIS2

@record_type('DOBJ')
class DynamicObject(Record):
    '''Dynamic Object'''
    #  DNAM DNAM

@record_type('LGTM')
class LGTM(Record):
    '''Light Template'''
    #  EDID Editor ID
    #  DATA DATA
    #  DALC DALC

@record_type('MUSC')
class MusicFile(Record):
    '''Music File'''
    #  EDID Editor ID
    #  FNAM Music File Path
    #  PNAM PNAM
    #  WNAM WNAM
    #  TNAM Music Templates

@record_type('FSTP')
class Footstep(Record):
    '''Footstep'''
    #  EDID Editor ID
    #  DATA Impact Data
    #  ANAM Action Name

@record_type('FSTS')
class FootstepSet(Record):
    '''Footstep Set'''
    #  EDID Editor ID
    #  XCNT Set count
    #  DATA Footstep Sets

@record_type('SMBN')
class StoryManagerBranchNode(Record):
    '''Story Manager Branch Node'''
    #  EDID Editor ID
    #  PNAM PNAM
    #  SNAM SNAM
    #  CITC CITC
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  DNAM DNAM
    #  XNAM XNAM

@record_type('SMQN')
class StoryManagerQuestNode(Record):
    '''Story Manager Quest Node'''
    #  EDID Editor ID
    #  PNAM PNAM
    #  SNAM SNAM
    #  CITC CITC
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  DNAM DNAM
    #  XNAM XNAM
    #  MNAM MNAM
    #  QNAM QNAM
    # ChildGroup  None
     # NNAM NNAM
     # FNAM FNAM
     # RNAM RNAM

@record_type('SMEN')
class StoryManagerEventNode(Record):
    '''Story Manager Event Node'''
    #  EDID EDID
    #  PNAM PNAM
    #  SNAM SNAM
    #  CITC CITC
    #  DNAM DNAM
    #  XNAM XNAM
    #  ENAM ENAM

@record_type('DLBR')
class DialogBranch(Record):
    '''Dialog Branch'''
    #  EDID Editor ID
    #  QNAM QNAM
    #  TNAM TNAM
    #  DNAM DNAM
    #  SNAM SNAM

@record_type('MUST')
class MusicTrack(Record):
    '''Music Track'''
    #  EDID Editor ID
    #  CNAM CNAM
    #  FLTV FLTV
    #  DNAM DNAM
    #  ANAM ANAM
    #  LNAM LNAM
    #  BNAM BNAM
    #  FNAM FNAM
    #  CITC CITC
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  SNAM SNAM

@record_type('DLVW')
class DialogView(Record):
    '''Dialog View'''
    #  EDID Editor ID
    #  QNAM QNAM
    #  TNAM TNAM
    #  BNAM BNAM
    #  ENAM ENAM
    #  DNAM DNAM

@record_type('WOOP')
class WordOfPower(Record):
    '''Word Of Power'''
    #  EDID Editor ID
    #  FULL Full Name
    #  TNAM TNAM

@record_type('SHOU')
class Shout(Record):
    '''Shout'''
    #  EDID Editor ID
    #  FULL Full Name
    #  MDOB Inventory Model
    #  DESC Description
    #  SNAM Shout Data

@record_type('EQUP')
class EquipmentSlot(Record):
    '''Equipment Slot'''
    #  EDID Editor ID
    #  PNAM Hand Reference
    #  DATA Occupies Slot

@record_type('RELA')
class Relationship(Record):
    '''Relationship'''
    #  EDID Editor ID
    #  DATA DATA

@record_type('SCEN')
class Scen(Record):
    '''SCEN'''
    #  EDID Editor ID
    #  VMAD VMAD
    # ChildGroup  None
     # WNAM WNAM
     # FNAM FNAM
     # HNAM HNAM
     # NAM0 NAM0
     # ChildGroup None
         # NEXT Seperator
         # ChildGroup CONDITIONAL
             # CTDA Conditional
             # CIS1 CIS1
             # CIS2 CIS2
     # ChildGroup SCEN_SCHR
         # SCHR SCHR
         # QNAM QNAM
         # NEXT NEXT
         # SCDA SCDA
         # SCTX SCTX
         # SCRO SCRO
    # ChildGroup  None
     # WNAM WNAM
     # ALID ALID
     # INAM INAM
     # FNAM FNAM
     # LNAM LNAM
     # DNAM DNAM
     # HNAM HNAM
     # SNAM SNAM
     # ENAM ENAM
     # DATA DATA
     # HNAM HNAM
     # NAM0 NAM0
     # HTID HTID
     # DMAX DMAX
     # DMIN DMIN
     # DEMO DEMO
     # DEVA DEVA
     # ANAM ANAM
     # PNAM PNAM
     # ChildGroup SCEN_SCHR
         # SCHR SCHR
         # QNAM QNAM
         # NEXT NEXT
         # SCDA SCDA
         # SCTX SCTX
         # SCRO SCRO
    #  VNAM VNAM
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2

@record_type('ASTP')
class Association(Record):
    '''Association'''
    #  EDID Editor ID
    #  MPRT Male Parent Title
    #  FPRT Female Parent Title
    #  MCHT Male Child Title
    #  FCHT Female Child Title
    #  DATA DATA

@record_type('OTFT')
class Outfit(Record):
    '''Outfit'''
    #  EDID Editor ID
    #  INAM INAM

@record_type('ARTO')
class ArtObject(Record):
    '''Art Object'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  MODL Model Name
    #  MODT Model Data
    #  DNAM DNAM

@record_type('MATO')
class MaterialObjects(Record):
    '''Material Objects'''
    #  EDID Editor ID
    #  MODL Model Name
    #  DNAM DNAM
    #  DATA DATA

@record_type('MOVT')
class MovementType(Record):
    '''Movement Type'''
    #  EDID Editor ID
    #  MNAM MNAM
    #  SPED SPED
    #  INAM INAM

@record_type('SNDR')
class SoundDesc(Record):
    '''Sound Desc'''
    #  EDID Editor ID
    #  CNAM CNAM
    #  GNAM GNAM
    #  SNAM SNAM
    #  ANAM ANAM
    #  ONAM ONAM
    #  FNAM FNAM
    # ChildGroup  CONDITIONAL
     # CTDA Conditional
     # CIS1 CIS1
     # CIS2 CIS2
    #  LNAM LNAM
    #  BNAM BNAM

@record_type('DUAL')
class DualCast(Record):
    '''Dual Cast'''
    #  EDID Editor ID
    #  OBND Object Bounds
    #  DATA DATA

@record_type('SNCT')
class SoundCategory(Record):
    '''Sound Category'''
    #  EDID Editor ID
    #  FULL Full Name
    #  FNAM FNAM
    #  PNAM PNAM
    #  VNAM VNAM
    #  UNAM UNAM

@record_type('SOPM')
class SoundOutputMarker(Record):
    '''Sound Output Marker'''
    #  EDID Editor ID
    #  FNAM FNAM
    #  NAM1 NAM1
    #  MNAM MNAM
    #  CNAM CNAM
    #  SNAM SNAM
    #  ONAM ONAM
    #  ANAM ANAM

@record_type('COLL')
class CollisionLayer(Record):
    '''Collision Layer'''
    #  EDID Editor ID
    #  DESC Description
    #  BNAM BNAM
    #  FNAM FNAM
    #  GNAM GNAM
    #  MNAM MNAM
    #  INTV Count of interactables
    #  CNAM CNAM

@record_type('CLFM')
class Color(Record):
    '''Color'''
    #  EDID Editor ID
    #  FULL Full Name
    #  CNAM Color
    #  FNAM FNAM

@record_type('REVB')
class ReverbParameters(Record):
    '''Reverb Parameters'''
    #  EDID Editor ID
    #  DATA DATA

@record_type('NAVI')
class Navigation(Record):
    '''Navigation (master data)'''
    #  NVER NVER
    #  NVMI NVMI
    #  NVPP NVPP

@record_type('CELL')
class Cell(Record):
    '''Cell'''
    #  EDID Editor ID
    #  FULL Full name
    #  DATA DATA
    #  XCLC Grid Location
    #  TVDT TVDT
    #  MHDT MHDT
    #  XCLL Interior Cell Lighting
    #  LTMP Lighting Template
    #  LNAM LNAM
    #  XCLW Water Height
    #  XWCS XWCS
    # ChildGroup  None
     # XCLR XCLR
     # XNAM XNAM
    # ChildGroup  None
     # XCIM Image Space
     # XLCN Location of this cell
     # XCMO Music Type
     # XCAS Acoustic Space
     # XCCM Interior Cell Climate
     # XOWN Owner NPC or Faction
     # XILL XILL
     # XWCN XWCN
     # XWCU XWCU
     # XEZN Encounter Zone
     # XCWT Water Reference
     # XEZN Encounter Zone
     # XWEM XWEM

@record_type('REFR')
class ObjectReference(Record):
    '''Object Reference'''
    #  EDID EDID
    #  VMAD VM Data
    #  NAME Basic Object
    #  XCVL XCVL
    #  XHTW XHTW
    # ChildGroup  None
     # XLRT Location Ref Type
     # XLKR Location Route
     # XRDS Light Related
     # XESP Enable Script Point
     # XMRK XMRK
    #  FNAM FNAM
    #  FULL Full Name
    #  TNAM TNAM
    #  XWCN XWCN
    #  XWCU XWCU
    #  XSPC XSPC
    #  XMBO Object Bounds
    # ChildGroup  None
     # XACT XACT
     # XTEL Door Teleport
    # ChildGroup  None
     # XTNM XTNM
     # XMBR XMBR
     # XRGB XRGB
     # XALP XALP
     # XLTW XLTW
     # XRGD XRGD
     # XLIB Leveled Item Base
     # XEZN XEZN
     # XCNT Item Count
     # ChildGroup None
         # XRDS Light Related
         # XEMI Emitted-Light
         # XPWR XPWR
         # XLIG Light Data
     # ChildGroup None
         # XPRD XPRD
         # XPPA XPPA
         # INAM INAM
         # SCHR SCHR
         # SCTX SCTX
         # PDTO PDTO
     # XRNK XRNK
     # XIS2 XIS2
     # XRDS Light Related
     # XTRI XTRI
     # XESP Enable Script Point
     # XPRM Placement of Marker
     # XLOC Lock Information
     # XLRT Location Ref Type
     # XCZC XCZC
     # XCZA XCZA
     # XOWN Owner
     # XLCM XLCM
     # XLCN Location of this cell
     # XNDP Door Pivot?
     # XAPD Activation Point Flags
     # XAPR Activation Point Reference
     # XLKR Location Route
     # XPOD Portal Destination
    #  XFVC XFVC
    #  XOCP XOCP
    #  XRMR Reference Marker
    #  LNAM LNAM
    #  INAM INAM
    #  XLRM Location Room Marker
    #  XMBP XMBP
    #  XSCL Scale
    #  ONAM ONAM
    #  DATA Locational Data

@record_type('WRLD')
class WorldSpace(Record):
    '''World Space'''
    #  EDID EDID
    #  RNAM RNAM
    #  MHDT MHDT
    #  FULL FULL
    #  WCTR WCTR
    #  LTMP LTMP
    #  XEZN XEZN
    #  XLCN Location of this cell
    #  WNAM WNAM
    #  PNAM PNAM
    #  CNAM CNAM
    #  NAM2 NAM2
    #  NAM3 NAM3
    #  NAM4 NAM4
    #  DNAM DNAM
    #  MNAM MNAM
    #  ONAM ONAM
    #  NAMA NAMA
    #  DATA DATA
    #  NAM0 NAM0
    #  NAM9 NAM9
    #  ZNAM ZNAM
    #  TNAM TNAM
    #  UNAM UNAM
    #  OFST OFST

@record_type('LAND')
class Landscape(Record):
    '''Landscape'''
    #  DATA DATA
    #  VNML Vertex Normals
    #  VHGT Vertex Height
    #  VCLR Vertex Color
    # ChildGroup  None
     # BTXT Base Texture
     # ChildGroup None
         # ATXT Additional Texture
         # VTXT VTXT

@record_type('PHZD')
class PlacedHazard(Record):
    '''Placed Hazard'''
    #  EDID EDID
    #  VMAD VM Data
    #  NAME Base Hazard
    # ChildGroup  None
     # XSCL Scale
     # XESP Enable Script Point?
    #  DATA DATA

@record_type('PGRE')
class PlacedGrenade(Record):
    '''Placed grenade'''
    #  EDID Editor ID
    #  NAME Base Hazard
    #  XSCL Scale
    # ChildGroup  None
     # XOWN XOWN
     # XESP Enable Script Point?
    #  DATA Location

@record_type('ACHR')
class ActorReference(Record):
    '''Actor Reference'''
    #  EDID Editor ID
    #  VMAD VM Data
    #  NAME Base NPC
    # ChildGroup  None
     # XLCM XLCM
     # XRGD Rag Doll?
     # XRGB XRGB
     # XLCN Location of this cell
     # XOWN Owner/Faction
     # XLRT Location Type Reference
     # XLKR Location Route
     # XAPD Activation Point Flags
     # XIS2 XIS2
     # XAPR Activation Point Reference
     # XESP Enable Script Point?
     # ChildGroup None
         # XPRD XPRD
         # XPPA XPPA
         # INAM INAM
         # SCHR SCHR
         # PDTO PDTO
     # XEZN Encounter Zone
     # XHOR Horse ID
    #  XSCL XSCL
    #  DATA DATA

@record_type('NAVM')
class NavMesh(Record):
    '''Nav Mesh'''
    #  NVNM NVNM
    #  ONAM ONAM
    #  PNAM PNAM
    #  NNAM NNAM


