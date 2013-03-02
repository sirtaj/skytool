from esp import *
import esp

RECORD_ORDER = ['TES4', 'GMST', 'KYWD', 'LCRT', 'AACT', 'TXST', 'GLOB', 'CLAS', 'FACT', 'HDPT', 'EYES', 'RACE', 'SOUN', 'ASPC', 'MGEF', 'LTEX', 'ENCH', 'SPEL', 'SCRL', 'ACTI', 'TACT', 'ARMO', 'BOOK', 'CONT', 'DOOR', 'INGR', 'LIGH', 'MISC', 'APPA', 'STAT', 'MSTT', 'GRAS', 'TREE', 'FLOR', 'FURN', 'WEAP', 'AMMO', 'NPC_', 'LVLN', 'KEYM', 'ALCH', 'IDLM', 'COBJ', 'PROJ', 'HAZD', 'SLGM', 'LVLI', 'WTHR', 'CLMT', 'SPGD', 'RFCT', 'REGN', 'DIAL', 'INFO', 'QUST', 'IDLE', 'PACK', 'CSTY', 'LSCR', 'LVSP', 'ANIO', 'WATR', 'EFSH', 'EXPL', 'DEBR', 'IMGS', 'IMAD', 'FLST', 'PERK', 'BPTD', 'ADDN', 'AVIF', 'CAMS', 'CPTH', 'VTYP', 'MATT', 'IPCT', 'IPDS', 'ARMA', 'ECZN', 'LCTN', 'MESG', 'DOBJ', 'LGTM', 'MUSC', 'FSTP', 'FSTS', 'SMBN', 'SMQN', 'SMEN', 'DLBR', 'MUST', 'DLVW', 'WOOP', 'SHOU', 'EQUP', 'RELA', 'SCEN', 'ASTP', 'OTFT', 'ARTO', 'MATO', 'MOVT', 'SNDR', 'DUAL', 'SNCT', 'SOPM', 'COLL', 'CLFM', 'REVB', 'NAVI', 'CELL', 'REFR', 'WRLD', 'LAND', 'PHZD', 'PGRE', 'ACHR', 'NAVM']


class EDITORID(SubrecordGroup):
    editorId = scalar( tag = 'EDID', data_type = esp.String )


class FULLNAME(SubrecordGroup):
    ingameName = scalar( tag = 'FULL', data_type = esp.LString )


class CONDITIONAL(SubrecordGroup):
    conditional = structure_set( 'Conditional', tag = 'CTDA', null = True )
    cis1     = structure( 'Cis1', tag = 'CIS1', null = True )
    cis2     = scalar( tag = 'CIS2', data_type = esp.String, null = True )


class Conditional(Subrecord):
    comparisonType = field( data_type = esp.UnsignedByte )
    unknown1 = field( data_type = esp.UnsignedByte )
    unknown2 = field( data_type = esp.UnsignedByte )
    unknown3 = field( data_type = esp.UnsignedByte )
    comparisonValue = field( data_type = esp.Float )
    function4096 = field( data_type = esp.Short )
    unused   = field( data_type = esp.Short )
    param1CanBeIntFloatFormid = field( data_type = esp.Reference )
    param2CanBeIntFloatFormid = field( data_type = esp.Reference )
    param3CanBeIntFloatFormid = field( data_type = esp.Reference )
    reference = field( data_type = esp.Integer )
    unknownAlways1 = field( data_type = esp.Integer )


class Cis1(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


class EFFECT(SubrecordGroup):
    magicEffect = reference( tag = 'EFID', refers_to = 'MGEF' )
    efit     = structure( 'Efit', tag = 'EFIT', null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )


class Efit(Subrecord):
    magnitude = field( data_type = esp.Float )
    unknown  = field( data_type = esp.Integer )
    duration = field( data_type = esp.UnsignedInteger )


class KEYWORDS(SubrecordGroup):
    numberOfKeywords = scalar( tag = 'KSIZ', data_type = esp.Integer, size = 4, null = True )
    keywordList = reference_set( tag = 'KWDA', refers_to = 'KYWD', null = True )


class TINTING(SubrecordGroup):
    tini     = scalar( tag = 'TINI', data_type = esp.Short, size = 2 )
    tint     = scalar( tag = 'TINT', data_type = esp.String, null = True )
    tinp     = scalar( tag = 'TINP', data_type = esp.Short, size = 2, null = True )
    colortint = reference( tag = 'TIND', refers_to = 'CLFM', null = True )
    tinting_4 = subrecord_group_set( 'TINTING_4', null = True )


class TINTING_4(SubrecordGroup):
    colortint = reference( tag = 'TINC', refers_to = 'CLFM' )
    tinv     = scalar( tag = 'TINV', data_type = esp.Float, size = 4, null = True )
    tirs     = scalar( tag = 'TIRS', data_type = esp.Short, size = 2, null = True )


class BODY_TEMPLATE(SubrecordGroup):
    bodyTemplate = structure( 'BodyTemplate', tag = 'BODT', size = 12 )


class BodyTemplate(Subrecord):
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


class OBJECT_BOUNDS(SubrecordGroup):
    objectBounds = structure( 'ObjectBounds', tag = 'OBND' )


class ObjectBounds(Subrecord):
    x1       = field( data_type = esp.Short )
    y1       = field( data_type = esp.Short )
    z1       = field( data_type = esp.Short )
    x2       = field( data_type = esp.Short )
    y2       = field( data_type = esp.Short )
    z2       = field( data_type = esp.Short )


class SCRIPTS(SubrecordGroup):
    scriptData = structure( 'ScriptData', tag = 'VMAD' )


class ScriptData(Subrecord):
    version  = field( data_type = esp.Short )
    objformat = field( data_type = esp.Short )
    scriptcount = field( data_type = esp.UnsignedShort )
    scripts  = field( data_type = esp.Blob )


class BASE_MODEL(SubrecordGroup):
    meshPath = scalar( tag = 'MODL', data_type = esp.String )
    textureData = scalar( tag = 'MODT', data_type = esp.Blob, null = True )
    textureInfo = scalar( tag = 'MODS', data_type = esp.Blob, null = True )


class MODEL_NAME(SubrecordGroup):
    model_name_0 = subrecord_group( 'MODEL_NAME_0', null = True )
    model_name_1 = subrecord_group( 'MODEL_NAME_1', null = True )


class MODEL_NAME_0(SubrecordGroup):
    mnam     = structure( 'Mnam', tag = 'MNAM' )
    indx     = scalar( tag = 'INDX', data_type = esp.Integer, size = 4, null = True )
    anam     = scalar( tag = 'ANAM', data_type = esp.String, null = True )
    model    = scalar( tag = 'MODL', data_type = esp.String, null = True )
    modelData = structure( 'ModelData', tag = 'MODT', null = True )


class Mnam(Subrecord):
    pass


class ModelData(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


class MODEL_NAME_1(SubrecordGroup):
    fnam     = structure( 'Fnam', tag = 'FNAM' )
    indx     = scalar( tag = 'INDX', data_type = esp.Integer, size = 4, null = True )
    anam     = scalar( tag = 'ANAM', data_type = esp.String, null = True )
    model    = scalar( tag = 'MODL', data_type = esp.String, null = True )
    modelData = structure( 'ModelDataModt', tag = 'MODT', null = True )


class Fnam(Subrecord):
    pass


class ModelDataModt(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


class DESTRUCTIBLE(SubrecordGroup):
    destructionData = structure( 'DestructionData', tag = 'DEST', size = 8 )
    stages   = subrecord_group_set( 'Stages', null = True )


class DestructionData(Subrecord):
    health   = field( data_type = esp.UnsignedInteger )
    stageCount = field( data_type = esp.UnsignedByte )
    vatsFlag = field( data_type = esp.UnsignedShort )
    unknown1 = field( data_type = esp.UnsignedByte )
    unknown2 = field( data_type = esp.UnsignedByte )


class Stages(SubrecordGroup):
    destructionSection = structure( 'DestructionSection', tag = 'DSTD', size = 20 )
    replacementModel = scalar_set( tag = 'DMDL', data_type = esp.String, null = True )
    dmdt     = scalar_set( tag = 'DMDT', data_type = esp.Blob, null = True )
    dmds     = scalar( tag = 'DMDS', data_type = esp.Blob, size = 35, null = True )
    dstf     = structure( 'Dstf', tag = 'DSTF' )


class DestructionSection(Subrecord):
    healthPercent = field( data_type = esp.UnsignedShort )
    damageStage = field( data_type = esp.UnsignedByte )
    flags    = field( data_type = esp.UnsignedByte )
    selfDamageRate = field( data_type = esp.UnsignedInteger )
    explosion = reference_field( 'EXPL' )
    debris   = reference_field( 'DEBR' )
    debrisCount = field( data_type = esp.UnsignedInteger )


class Dstf(Subrecord):
    pass


class CARRYABLE(SubrecordGroup):
    pickupSound = reference( tag = 'YNAM', refers_to = 'SNDR', null = True )
    dropSound = reference( tag = 'ZNAM', refers_to = 'SNDR', null = True )


class LEVELED(SubrecordGroup):
    percentChanceNone = scalar( tag = 'LVLD', data_type = esp.UnsignedByte )
    flags    = scalar( tag = 'LVLF', data_type = esp.UnsignedByte )
    entryCount = scalar( tag = 'LLCT', data_type = esp.UnsignedByte )
    leveled_entry = subrecord_group_set( 'Leveled_Entry', null = True )


class Leveled_Entry(SubrecordGroup):
    level    = structure( 'Level', tag = 'LVLO', size = 12 )
    leveled_entry_owner = subrecord_group( 'Leveled_Entry_Owner' )


class Level(Subrecord):
    level    = field( data_type = esp.UnsignedLong )
    form     = field( data_type = esp.Reference )
    spawnNumber = field( data_type = esp.UnsignedLong )


class Leveled_Entry_Owner(SubrecordGroup):
    factionOwnerCondition = structure( 'FactionOwnerCondition', tag = 'COED', null = True )
    actorOwnerCondition = structure( 'ActorOwnerCondition', tag = 'COED', null = True )


class FactionOwnerCondition(Subrecord):
    owner    = reference_field( 'FACT' )
    requiredRank = field( data_type = esp.Integer )
    condition = field( data_type = esp.Float )


class ActorOwnerCondition(Subrecord):
    owner    = reference_field( 'NPC_' )
    value    = reference_field( 'GLOB' )
    condition = field( data_type = esp.Float )


class OBJECT(SubrecordGroup):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    fullname = subrecord_group( u'FULLNAME', null = True )


class SCRIPTED_OBJECT(SubrecordGroup):
    editorid = subrecord_group( u'EDITORID' )
    scripts  = subrecord_group( u'SCRIPTS', null = True )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    fullname = subrecord_group( u'FULLNAME', null = True )


class CONCEPT(SubrecordGroup):
    editorid = subrecord_group( u'EDITORID' )
    fullname = subrecord_group( u'FULLNAME', null = True )


class SCRIPTED_CONCEPT(SubrecordGroup):
    editorid = subrecord_group( u'EDITORID' )
    scripts  = subrecord_group( u'SCRIPTS', null = True )
    fullname = subrecord_group( u'FULLNAME', null = True )


class SCRIPTED_MODEL(SubrecordGroup):
    scripted_object = subrecord_group( u'SCRIPTED_OBJECT' )
    base_model = subrecord_group( u'BASE_MODEL', null = True )


########################
@record_type('TES4')

class MainPluginHeader(Record):
    header   = structure( 'Header', tag = 'HEDR' )
    author   = scalar( tag = 'CNAM', data_type = esp.String, null = True )
    description = scalar( tag = 'SNAM', data_type = esp.String, null = True )
    mainpluginheader_3 = subrecord_group_set( 'MainPluginHeader_3', null = True )
    unknownFixed = scalar( tag = 'INTV', data_type = esp.UnsignedInteger, size = 4, null = True )


class Header(Subrecord):
    fileVersion = field( data_type = esp.Float )
    recordCount = field( data_type = esp.Integer )
    nextFormid = field( data_type = esp.Reference )


class MainPluginHeader_3(SubrecordGroup):
    master   = scalar( tag = 'MAST', data_type = esp.String )
    filesize = scalar( tag = 'DATA', data_type = esp.UnsignedLong )


########################
@record_type('GMST')

class GameSetting(Record):
    editorid = subrecord_group( u'EDITORID' )
    stringValue = scalar( tag = 'DATA', data_type = esp.LString )
    floatValue = scalar( tag = 'DATA', data_type = esp.Float )
    integerValue = scalar( tag = 'DATA', data_type = esp.Integer )
    byteValue = scalar( tag = 'DATA', data_type = esp.Integer )


########################
@record_type('KYWD')

class Keyword(Record):
    editorid = subrecord_group( u'EDITORID' )
    color    = scalar( tag = 'CNAM', data_type = esp.Color, null = True )


########################
@record_type('LCRT')

class LocationRefType(Record):
    editorid = subrecord_group( u'EDITORID' )
    markerColor = scalar( tag = 'CNAM', data_type = esp.Color, null = True )


########################
@record_type('AACT')

class Action(Record):
    editorid = subrecord_group( u'EDITORID' )
    color    = scalar( tag = 'CNAM', data_type = esp.Color )


########################
@record_type('TXST')

class TextureSet(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    diffuseMap = scalar( tag = 'TX00', data_type = esp.String, null = True )
    normalMap = scalar( tag = 'TX01', data_type = esp.String, null = True )
    glowskinhairMap = scalar( tag = 'TX02', data_type = esp.String, null = True )
    heightparallaxMap = scalar( tag = 'TX03', data_type = esp.String, null = True )
    environmentMap = scalar( tag = 'TX04', data_type = esp.String, null = True )
    environmentMaskMap = scalar( tag = 'TX05', data_type = esp.String, null = True )
    specularMap = scalar( tag = 'TX07', data_type = esp.String, null = True )
    lightingShaderProperties = structure( 'LightingShaderProperties', tag = 'DODT', size = 36, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.UnsignedShort, size = 2, null = True )


class LightingShaderProperties(Subrecord):
    unknownFloat = field( data_type = esp.Float )
    unknownFloat1 = field( data_type = esp.Float )
    unknownFloat2 = field( data_type = esp.Float )
    unknownFloat3 = field( data_type = esp.Float )
    unknownFloat4 = field( data_type = esp.Float )
    unknownFloat5 = field( data_type = esp.Float )
    unknownFloat6 = field( data_type = esp.Float )
    unknownFloat7 = field( data_type = esp.Integer )
    unknownFloat8 = field( data_type = esp.Integer )


########################
@record_type('GLOB')

class GlobalVariable(Record):
    editorid = subrecord_group( u'EDITORID' )
    valueType = scalar( tag = 'FNAM', data_type = esp.UnsignedByte, size = 1, null = True )
    value    = scalar( tag = 'FLTV', data_type = esp.Float, size = 4, null = True )


########################
@record_type('CLAS')

class CharacterClass(Record):
    concept  = subrecord_group( u'CONCEPT' )
    unusedDescription = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    classData = structure( 'ClassData', tag = 'DATA', null = True )


class ClassData(Subrecord):
    tagSkill1AvCode = field( data_type = esp.Integer )
    tagSkill2AvCode = field( data_type = esp.Integer )
    tagSkill3AvCode = field( data_type = esp.Integer )
    unusedTagSlot = field( data_type = esp.Integer )
    unusedTagSlot = field( data_type = esp.Integer )
    unusedTagSlot = field( data_type = esp.Short )
    unusedTagSlot = field( data_type = esp.Short )
    unknownFloat6 = field( data_type = esp.Float )
    unknownInt7 = field( data_type = esp.Integer )
    unknownInt8 = field( data_type = esp.Integer )


########################
@record_type('FACT')

class Faction(Record):
    concept  = subrecord_group( u'CONCEPT' )
    fact     = structure_set( 'Fact', tag = 'XNAM', null = True )
    flags    = scalar( tag = 'DATA', data_type = esp.UnsignedInteger )
    jailExteriorMarker = reference( tag = 'JAIL', refers_to = 'REFR', null = True )
    followerWaitMarker = reference( tag = 'WAIT', refers_to = 'REFR', null = True )
    evidenceChest = reference( tag = 'STOL', refers_to = 'REFR', null = True )
    playerBelongingsChest = reference( tag = 'PLCN', refers_to = 'REFR', null = True )
    crimeFactions = reference( tag = 'CRGR', refers_to = 'FLST', null = True )
    jailOutfit = reference( tag = 'JOUT', refers_to = 'OTFT', null = True )
    crimeGold = structure( 'CrimeGold', tag = 'CRVA', null = True )
    vendorList = reference( tag = 'VEND', refers_to = 'FLST', null = True )
    vendorChest = reference( tag = 'VENC', refers_to = 'REFR', null = True )
    venv     = structure( 'Venv', tag = 'VENV', size = 12 )
    faction_13 = subrecord_group_set( 'Faction_13', null = True )
    plvdRelatedToServices = structure( 'PlvdRelatedToServices', tag = 'PLVD', size = 12, null = True )
    fenceFactions = scalar( tag = 'CITC', data_type = esp.Integer, size = 4, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )


class Fact(Subrecord):
    formid   = reference_field( 'FACT' )
    mod      = field( data_type = esp.Integer )
    combat   = field( data_type = esp.Integer )


class CrimeGold(Subrecord):
    flags    = field( data_type = esp.UnsignedShort )
    murder   = field( data_type = esp.UnsignedShort )
    assault  = field( data_type = esp.UnsignedShort )
    trespass = field( data_type = esp.UnsignedShort )
    pickpocket = field( data_type = esp.UnsignedShort )
    unused   = field( data_type = esp.UnsignedShort )
    stealMulti = field( data_type = esp.Float )
    escape   = field( data_type = esp.UnsignedShort )
    werewolf = field( data_type = esp.UnsignedShort )


class Venv(Subrecord):
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


class Faction_13(SubrecordGroup):
    rankId   = scalar( tag = 'RNAM', data_type = esp.Integer, size = 4 )
    rankName = scalar( tag = 'MNAM', data_type = esp.LString, null = True )


class PlvdRelatedToServices(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )
    unknown4bytes3 = field( data_type = esp.Integer )


########################
@record_type('HDPT')

class HeadpartMesh(Record):
    concept  = subrecord_group( u'CONCEPT' )
    base_model = subrecord_group( u'BASE_MODEL' )
    flag     = scalar( tag = 'DATA', data_type = esp.UnsignedByte, size = 1, null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    additionalHeadpartMesh = reference_set( tag = 'HNAM', refers_to = 'HDPT', null = True )
    headpartmesh_5 = subrecord_group_set( 'HeadpartMesh_5', null = True )
    baseTexture = reference( tag = 'TNAM', refers_to = 'TXST', null = True )
    resourceFormList = reference( tag = 'RNAM', refers_to = 'FLST', null = True )


class HeadpartMesh_5(SubrecordGroup):
    optionType = scalar( tag = 'NAM0', data_type = esp.Integer, size = 4 )
    triFile  = scalar( tag = 'NAM1', data_type = esp.String, null = True )


########################
@record_type('EYES')

class Eyes(Record):
    concept  = subrecord_group( u'CONCEPT' )
    icon     = scalar( tag = 'ICON', data_type = esp.String, null = True )
    availableForGender = scalar( tag = 'DATA', data_type = esp.UnsignedByte, size = 1, null = True )


########################
@record_type('RACE')

class Race(Record):
    concept  = subrecord_group( u'CONCEPT' )
    description = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    spellCount = scalar( tag = 'SPCT', data_type = esp.Integer, size = 4, null = True )
    learnedSpell = reference_set( tag = 'SPLO', refers_to = 'SPEL', null = True )
    nakedArmor = reference( tag = 'WNAM', refers_to = 'ARMO', null = True )
    body_template = subrecord_group( u'BODY_TEMPLATE', null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    race_7   = subrecord_group( 'Race_7' )
    race_8   = subrecord_group( 'Race_8' )
    race_9   = subrecord_group( 'Race_9' )
    materialType = reference( tag = 'NAM4', refers_to = 'MATT', null = True )
    impactDataSet = reference( tag = 'NAM5', refers_to = 'IPDS', null = True )
    artObject = reference( tag = 'NAM7', refers_to = 'ARTO', null = True )
    sound    = reference( tag = 'ONAM', refers_to = 'SNDR', null = True )
    sound    = reference( tag = 'LNAM', refers_to = 'SNDR', null = True )
    name     = scalar_set( tag = 'NAME', data_type = esp.String, null = True )
    race_16  = subrecord_group_set( 'Race_16', null = True )
    vnam     = scalar( tag = 'VNAM', data_type = esp.UnsignedInteger, size = 4, null = True )
    equipmentSlot = reference_set( tag = 'QNAM', refers_to = 'EQUP', null = True )
    equipmentSlot = reference( tag = 'UNES', refers_to = 'EQUP', null = True )
    phtn     = scalar_set( tag = 'PHTN', data_type = esp.String, null = True )
    phwt     = scalar_set( tag = 'PHWT', data_type = esp.Blob, null = True )
    movementType = reference( tag = 'WKMV', refers_to = 'MOVT', null = True )
    movementType = reference( tag = 'RNMV', refers_to = 'MOVT', null = True )
    movementType = reference( tag = 'SWMV', refers_to = 'MOVT', null = True )
    movementType = reference( tag = 'FLMV', refers_to = 'MOVT', null = True )
    movementType = reference( tag = 'SNMV', refers_to = 'MOVT', null = True )
    race_27  = subrecord_group_set( 'Race_27', null = True )
    raceType = reference( tag = 'NAM8', refers_to = 'RACE', null = True )
    raceType = reference( tag = 'RNAM', refers_to = 'RACE', null = True )


class Race_7(SubrecordGroup):
    actorValues = structure( 'ActorValues', tag = 'DATA', size = 128 )
    model_name = subrecord_group( u'MODEL_NAME', null = True )
    mtnm     = scalar_set( tag = 'MTNM', data_type = esp.Str4, size = 4, null = True )
    voiceType = structure( 'VoiceType', tag = 'VTCK', size = 8, null = True )
    decapitatedHead = structure( 'DecapitatedHead', tag = 'DNAM', size = 8, null = True )
    hairColor = structure( 'HairColor', tag = 'HCLF', size = 8, null = True )
    tinl     = scalar( tag = 'TINL', data_type = esp.Short, size = 2, null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Float, size = 4, null = True )
    unam     = scalar( tag = 'UNAM', data_type = esp.Float, size = 4, null = True )
    race_7_9 = subrecord_group_set( 'Race_7_9', null = True )


class ActorValues(Subrecord):
    unknownValue1 = field( data_type = esp.UnsignedByte )
    unknownValue2 = field( data_type = esp.UnsignedByte )
    unknownValue3 = field( data_type = esp.UnsignedByte )
    unknownValue4 = field( data_type = esp.UnsignedByte )
    unknownValue5 = field( data_type = esp.UnsignedByte )
    unknownValue6 = field( data_type = esp.UnsignedByte )
    unknownValue7 = field( data_type = esp.UnsignedByte )
    unknownValue8 = field( data_type = esp.UnsignedByte )
    unknownValue8 = field( data_type = esp.UnsignedByte )
    unknownValue9 = field( data_type = esp.UnsignedByte )
    unknownValue10 = field( data_type = esp.UnsignedByte )
    unknownValue11 = field( data_type = esp.UnsignedByte )
    unknownValue12 = field( data_type = esp.UnsignedByte )
    unknownValue13 = field( data_type = esp.UnsignedByte )
    unknownValue14 = field( data_type = esp.UnsignedByte )
    unknownValue15 = field( data_type = esp.UnsignedByte )
    scaleMale = field( data_type = esp.Float )
    scaleFemale = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Float )
    playerFlag = field( data_type = esp.UnsignedInteger )
    baseHealth = field( data_type = esp.Float )
    baseMagika = field( data_type = esp.Float )
    baseStamina = field( data_type = esp.Float )
    baseCarryWeight = field( data_type = esp.Float )
    unknown13 = field( data_type = esp.Float )
    unknown14 = field( data_type = esp.Float )
    unknown15 = field( data_type = esp.Float )
    unknown16 = field( data_type = esp.Integer )
    unknown17 = field( data_type = esp.Integer )
    unknown18 = field( data_type = esp.Integer )
    unknown19 = field( data_type = esp.Float )
    unknown20 = field( data_type = esp.Integer )
    baseHealRate = field( data_type = esp.Float )
    baseMagikaRate = field( data_type = esp.Float )
    baseStaminaRate = field( data_type = esp.Float )
    unknown24 = field( data_type = esp.Float )
    unknown25 = field( data_type = esp.Float )
    unknown26 = field( data_type = esp.Integer )
    unknown27 = field( data_type = esp.Float )
    unknown28 = field( data_type = esp.Float )
    unknown29 = field( data_type = esp.Float )
    unknown30 = field( data_type = esp.Float )
    unknown31 = field( data_type = esp.Integer )


class VoiceType(Subrecord):
    maleVoice = reference_field( 'VTYP' )
    femaleVoice = reference_field( 'VTYP' )


class DecapitatedHead(Subrecord):
    male     = reference_field( 'ARMO' )
    female   = reference_field( 'ARMO' )


class HairColor(Subrecord):
    male     = reference_field( 'CLFM' )
    female   = reference_field( 'CLFM' )


class Race_7_9(SubrecordGroup):
    atkd     = structure( 'Atkd', tag = 'ATKD', size = 44 )
    atke     = scalar( tag = 'ATKE', data_type = esp.String )


class Atkd(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    spell    = reference_field( 'SPEL' )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    keyword  = reference_field( 'KYWD' )
    unknown8 = field( data_type = esp.Float )
    unknown9 = field( data_type = esp.Float )
    unknown10 = field( data_type = esp.Float )


class Race_8(SubrecordGroup):
    nam1     = structure( 'Nam1', tag = 'NAM1' )
    model_name = subrecord_group( u'MODEL_NAME' )
    bodyPart = reference( tag = 'GNAM', refers_to = 'BPTD', null = True )


class Nam1(Subrecord):
    pass


class Race_9(SubrecordGroup):
    nam3     = structure( 'Nam3', tag = 'NAM3' )
    model_name = subrecord_group( u'MODEL_NAME' )


class Nam3(Subrecord):
    pass


class Race_16(SubrecordGroup):
    movementType = reference( tag = 'MTYP', refers_to = 'MOVT' )
    speedData = structure( 'SpeedData', tag = 'SPED', size = 44 )


class SpeedData(Subrecord):
    strafe1MinSpeed = field( data_type = esp.Float )
    strafe1MaxSpeed = field( data_type = esp.Float )
    strafe2MinSpeed = field( data_type = esp.Float )
    strafe2MaxSpeed = field( data_type = esp.Float )
    forwardMinSpeed = field( data_type = esp.Float )
    forwardMaxSpeed = field( data_type = esp.Float )
    backMinSpeed = field( data_type = esp.Float )
    backMaxSpeed = field( data_type = esp.Float )
    direction1 = field( data_type = esp.Float )
    direction2 = field( data_type = esp.Float )
    direction3 = field( data_type = esp.Float )


class Race_27(SubrecordGroup):
    race_27_0 = subrecord_group( 'Race_27_0' )
    race_27_1 = subrecord_group_set( 'Race_27_1', null = True )
    race_27_2 = subrecord_group_set( 'Race_27_2', null = True )
    race_27_3 = subrecord_group( 'Race_27_3', null = True )
    race_27_4 = subrecord_group( 'Race_27_4', null = True )


class Race_27_0(SubrecordGroup):
    nam0     = structure( 'Nam0', tag = 'NAM0' )
    model_name = subrecord_group( u'MODEL_NAME' )


class Nam0(Subrecord):
    pass


class Race_27_1(SubrecordGroup):
    headpartMesh = reference( tag = 'HEAD', refers_to = 'HDPT' )
    indx     = scalar( tag = 'INDX', data_type = esp.Integer, size = 4, null = True )


class Race_27_2(SubrecordGroup):
    mpai     = scalar( tag = 'MPAI', data_type = esp.Integer, size = 4 )
    mpav     = structure( 'Mpav', tag = 'MPAV', size = 32 )


class Mpav(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )


class Race_27_3(SubrecordGroup):
    malePresetsNpc_ = reference_set( tag = 'RPRM', refers_to = 'NPC_', null = True )
    maleHairColorPreset = reference_set( tag = 'AHCM', refers_to = 'CLFM', null = True )
    textureSet = reference_set( tag = 'FTSM', refers_to = 'TXST', null = True )
    textureSet = reference( tag = 'DFTM', refers_to = 'TXST', null = True )
    tinting  = subrecord_group_set( u'TINTING', null = True )


class Race_27_4(SubrecordGroup):
    femalePresetsNpc_ = reference_set( tag = 'RPRF', refers_to = 'NPC_', null = True )
    femaleHairColorPreset = reference_set( tag = 'AHCF', refers_to = 'CLFM', null = True )
    textureSet = reference_set( tag = 'FTSF', refers_to = 'TXST', null = True )
    textureSet = reference( tag = 'DFTF', refers_to = 'TXST', null = True )
    tinting  = subrecord_group_set( u'TINTING', null = True )


########################
@record_type('SOUN')

class SoundDescriptor(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    filename = scalar( tag = 'FNAM', data_type = esp.String, null = True )
    soundData = structure( 'SoundData', tag = 'SNDD', null = True )
    sound    = reference( tag = 'SDSC', refers_to = 'SNDR', null = True )


class SoundData(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Short )
    unknown3 = field( data_type = esp.Short )
    unknown4 = field( data_type = esp.Short )
    unknown4 = field( data_type = esp.Short )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    cell     = reference_field( 'CELL' )
    reference = reference_field( 'REFR' )


########################
@record_type('ASPC')

class AcousticSpace(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    ambientSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    region   = reference( tag = 'RDAT', refers_to = 'REGN', null = True )
    reverb   = reference( tag = 'BNAM', refers_to = 'REVB', null = True )


########################
@record_type('MGEF')

class MagicEffectFixmeTodo(Record):
    scripted_object = subrecord_group( u'SCRIPTED_OBJECT' )
    model    = reference( tag = 'MDOB', refers_to = 'STAT', null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    effectData = structure( 'EffectData', tag = 'DATA', size = 152, null = True )
    sndd     = scalar( tag = 'SNDD', data_type = esp.Blob, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.LString, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )


class EffectData(Subrecord):
    flags    = field( data_type = esp.Integer )
    baseCost = field( data_type = esp.Float )
    targetedId = field( data_type = esp.Reference )
    primarySkill = field( data_type = esp.Integer )
    resistance = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.UnsignedInteger )
    light    = reference_field( 'LIGH' )
    taperWeight = field( data_type = esp.Float )
    hitEfsh  = reference_field( 'EFSH' )
    enchantEfsh = reference_field( 'EFSH' )
    skillLevel = field( data_type = esp.Integer )
    area     = field( data_type = esp.Integer )
    castingDelay = field( data_type = esp.Float )
    taperCurve = field( data_type = esp.Float )
    taperDuration = field( data_type = esp.Float )
    secondavWeight = field( data_type = esp.Float )
    effectType = field( data_type = esp.Integer )
    primaryAvifAffected = field( data_type = esp.Integer )
    projectile = reference_field( 'PROJ' )
    explosion = reference_field( 'EXPL' )
    castType = field( data_type = esp.Integer )
    aimType  = field( data_type = esp.Integer )
    secondaryAvifAffected = field( data_type = esp.Integer )
    wielded  = reference_field( 'ARTO' )
    impacted = reference_field( 'ARTO' )
    impactDataSet = reference_field( 'IPDS' )
    skillusagemult = field( data_type = esp.Float )
    dualcast = reference_field( 'DUAL' )
    dualcastScale = field( data_type = esp.Float )
    enchant  = reference_field( 'ARTO' )
    nulldata1 = field( data_type = esp.Integer )
    nulldata2 = field( data_type = esp.Integer )
    equipSpell = reference_field( 'SPEL' )
    imagespaceIpds = reference_field( 'IPDS' )
    perk     = reference_field( 'PERK' )
    soundVolume = field( data_type = esp.Integer )
    scriptAidataScore = field( data_type = esp.Float )
    scriptAidataDelay = field( data_type = esp.Float )


########################
@record_type('LTEX')

class LandTexture(Record):
    editorid = subrecord_group( u'EDITORID' )
    textureSet = reference( tag = 'TNAM', refers_to = 'TXST', null = True )
    materialType = reference( tag = 'MNAM', refers_to = 'MATT', null = True )
    havokData = scalar( tag = 'HNAM', data_type = esp.Short, size = 2, null = True )
    textureSpecularExponent = scalar( tag = 'SNAM', data_type = esp.UnsignedByte, size = 1, null = True )
    grass    = reference_set( tag = 'GNAM', refers_to = 'GRAS', null = True )


########################
@record_type('ENCH')

class Enchantment(Record):
    object   = subrecord_group( u'OBJECT' )
    enchantmentData = structure( 'EnchantmentData', tag = 'ENIT', null = True )
    effect   = subrecord_group_set( u'EFFECT', null = True )


class EnchantmentData(Subrecord):
    baseCost = field( data_type = esp.Integer )
    flags    = field( data_type = esp.Integer )
    castType = field( data_type = esp.Integer )
    chargeAmount = field( data_type = esp.Integer )
    targetType = field( data_type = esp.Integer )
    enchantType = field( data_type = esp.Integer )
    chargeTime = field( data_type = esp.Integer )
    baseEnchant = reference_field( 'ENCH' )
    wornRestrict = reference_field( 'FLST', null = True )


########################
@record_type('SPEL')

class Spell(Record):
    object   = subrecord_group( u'OBJECT' )
    inventoryIcon = reference( tag = 'MDOB', refers_to = 'STAT', null = True )
    equipment = reference( tag = 'ETYP', refers_to = 'EQUP', null = True )
    description = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    spellInfoAndType = structure( 'SpellInfoAndType', tag = 'SPIT', null = True )
    effect   = subrecord_group_set( u'EFFECT', null = True )


class SpellInfoAndType(Subrecord):
    baseCost = field( data_type = esp.UnsignedInteger )
    flags    = field( data_type = esp.UnsignedInteger )
    type     = field( data_type = esp.Integer )
    castTime = field( data_type = esp.Float )
    activateType = field( data_type = esp.Integer )
    aimType  = field( data_type = esp.Integer )
    duration = field( data_type = esp.Float )
    range    = field( data_type = esp.Float )
    perk     = reference_field( 'PERK' )


########################
@record_type('SCRL')

class Scroll(Record):
    object   = subrecord_group( u'OBJECT' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    invIcon  = reference( tag = 'MDOB', refers_to = 'STAT', null = True )
    equipment = reference( tag = 'ETYP', refers_to = 'EQUP', null = True )
    description = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    data     = structure( 'Data', tag = 'DATA', size = 8, null = True )
    spellInfoAndType = structure( 'SpellInfoAndTypeSpit', tag = 'SPIT', size = 36, null = True )
    effect   = subrecord_group_set( u'EFFECT', null = True )


class Data(Subrecord):
    unknown4bytes = field( data_type = esp.Integer )
    itemWeight = field( data_type = esp.Float )


class SpellInfoAndTypeSpit(Subrecord):
    baseCost = field( data_type = esp.UnsignedInteger )
    flags    = field( data_type = esp.UnsignedInteger )
    type     = field( data_type = esp.Integer )
    castTime = field( data_type = esp.Float )
    activateType = field( data_type = esp.Integer )
    aimType  = field( data_type = esp.Integer )
    duration = field( data_type = esp.Float )
    range    = field( data_type = esp.Float )
    perk     = reference_field( 'PERK' )


########################
@record_type('ACTI')

class Activator(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    destructible = subrecord_group( u'DESTRUCTIBLE' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    ambientSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    water    = reference( tag = 'WNAM', refers_to = 'WATR', null = True )
    useSound = reference( tag = 'VNAM', refers_to = 'SNDR', null = True )
    verbeString = scalar( tag = 'RNAM', data_type = esp.LString, null = True )
    flags    = scalar( tag = 'FNAM', data_type = esp.Short, size = 2, null = True )
    keyword  = reference( tag = 'KNAM', refers_to = 'KYWD', null = True )


########################
@record_type('TACT')

class TalkingActivator(Record):
    object   = subrecord_group( u'OBJECT' )
    base_model = subrecord_group( u'BASE_MODEL' )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Short, size = 2, null = True )
    voiceType = reference( tag = 'VNAM', refers_to = 'VTYP', null = True )


########################
@record_type('ARMO')

class Armor(Record):
    scripted_object = subrecord_group( u'SCRIPTED_OBJECT' )
    enchantment = reference( tag = 'EITM', refers_to = 'ENCH', null = True )
    maleGroundModelPath = scalar( tag = 'MOD2', data_type = esp.String, null = True )
    modelData2 = scalar( tag = 'MO2T', data_type = esp.Blob, null = True )
    modelData2s = scalar( tag = 'MO2S', data_type = esp.Blob, null = True )
    femaleGroundModelPath = scalar( tag = 'MOD4', data_type = esp.String, null = True )
    modelData4 = scalar( tag = 'MO4T', data_type = esp.Blob, null = True )
    modelData4s = scalar( tag = 'MO4S', data_type = esp.Blob, null = True )
    body_template = subrecord_group( u'BODY_TEMPLATE', null = True )
    equipmentType = reference( tag = 'ETYP', refers_to = 'EQUP', null = True )
    weaponBashImpactDataSet = reference( tag = 'BIDS', refers_to = 'IPDS', null = True )
    bashMaterial = reference( tag = 'BAMT', refers_to = 'MATT', null = True )
    carryable = subrecord_group( u'CARRYABLE' )
    raceType = reference( tag = 'RNAM', refers_to = 'RACE', null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    itemDescription = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    armatureModelarma = reference_set( tag = 'MODL', refers_to = 'ARMA', null = True )
    armorData = structure( 'ArmorData', tag = 'DATA', size = 8, null = True )
    damageResistancedrActualDrIsThisValue001 = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )
    messageType = reference( tag = 'TNAM', refers_to = 'ARMO', null = True )


class ArmorData(Subrecord):
    value    = field( data_type = esp.Integer )
    weightwg = field( data_type = esp.Float )


########################
@record_type('BOOK')

class Book(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    bookDescriptionSometimesACopyOfTheBookName = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    carryable = subrecord_group( u'CARRYABLE' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    bookSettings = structure( 'BookSettings', tag = 'DATA', null = True )
    model    = reference( tag = 'INAM', refers_to = 'STAT', null = True )
    alternateText = scalar( tag = 'CNAM', data_type = esp.LString, size = 4, null = True )


class BookSettings(Subrecord):
    flags1   = field( data_type = esp.UnsignedByte )
    flags2   = field( data_type = esp.UnsignedByte )
    flags3   = field( data_type = esp.UnsignedShort )
    skillToIncreasespellToCast = field( data_type = esp.Reference )
    bookValue = field( data_type = esp.Integer )
    bookWeight = field( data_type = esp.Float )


########################
@record_type('CONT')

class Container(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    containedCount = scalar( tag = 'COCT', data_type = esp.Integer, size = 4, null = True )
    contents = structure_set( 'Contents', tag = 'CNTO', size = 8, null = True )
    cndExtraData = structure( 'CndExtraData', tag = 'COED', size = 12, null = True )
    containerData = structure( 'ContainerData', tag = 'DATA' )
    openSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    closeSound = reference( tag = 'QNAM', refers_to = 'SNDR', null = True )


class Contents(Subrecord):
    formid   = field( data_type = esp.Reference )
    count    = field( data_type = esp.UnsignedInteger )


class CndExtraData(Subrecord):
    faction  = reference_field( 'FACT' )
    unknown  = field( data_type = esp.Integer )
    itemCondition = field( data_type = esp.Float )


class ContainerData(Subrecord):
    flags    = field( data_type = esp.UnsignedByte )
    weight   = field( data_type = esp.Float )


########################
@record_type('DOOR')

class Door(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    openSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    closeSound = reference( tag = 'ANAM', refers_to = 'SNDR', null = True )
    flags    = scalar( tag = 'FNAM', data_type = esp.UnsignedByte, size = 1, null = True )


########################
@record_type('INGR')

class Ingredient(Record):
    object   = subrecord_group( u'OBJECT' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    carryable = subrecord_group( u'CARRYABLE' )
    data     = structure( 'DataData', tag = 'DATA', size = 8, null = True )
    enit     = structure( 'Enit', tag = 'ENIT', size = 8, null = True )
    effect   = subrecord_group_set( u'EFFECT', null = True )


class DataData(Subrecord):
    value    = field( data_type = esp.Integer )
    weight   = field( data_type = esp.Float )


class Enit(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )


########################
@record_type('LIGH')

class LightTemplate(Record):
    editorid = subrecord_group( u'EDITORID' )
    scripts  = subrecord_group( u'SCRIPTS' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    fullname = subrecord_group( u'FULLNAME' )
    lightData = structure( 'LightData', tag = 'DATA', size = 48, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Float, size = 4, null = True )
    sound    = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )


class LightData(Subrecord):
    time1Infinite = field( data_type = esp.Integer )
    radius   = field( data_type = esp.Integer )
    color    = field( data_type = esp.Color )
    flags    = field( data_type = esp.Integer )
    falloff  = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Float )
    unknown8 = field( data_type = esp.Float )
    unknown9 = field( data_type = esp.Float )
    value    = field( data_type = esp.Integer )
    weight   = field( data_type = esp.Float )


########################
@record_type('MISC')

class MiscItem(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    itemIcon = scalar( tag = 'ICON', data_type = esp.String, size = 19, null = True )
    carryable = subrecord_group( u'CARRYABLE' )
    mods     = scalar( tag = 'MODS', data_type = esp.Blob, null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    itemData = structure( 'ItemData', tag = 'DATA', size = 8, null = True )


class ItemData(Subrecord):
    value    = field( data_type = esp.Integer )
    weight   = field( data_type = esp.Float )


########################
@record_type('APPA')

class Apparatus(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    quality  = scalar( tag = 'QUAL', data_type = esp.Integer, size = 4, null = True )
    description = scalar( tag = 'DESC', data_type = esp.Integer, null = True )
    data     = structure( 'Apparatus_3_DataData', tag = 'DATA', size = 8, null = True )


class Apparatus_3_DataData(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )


########################
@record_type('STAT')

class Static(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    dnam     = structure( 'Static_3_DnamDnam', tag = 'DNAM', size = 8, null = True )
    mnam     = scalar( tag = 'MNAM', data_type = esp.Blob, null = True )


class Static_3_DnamDnam(Subrecord):
    scale    = field( data_type = esp.Float )
    materialObject = reference_field( 'MATO' )


########################
@record_type('MSTT')

class MovableStatic(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    destructible = subrecord_group( u'DESTRUCTIBLE' )
    mods     = scalar( tag = 'MODS', data_type = esp.Blob, null = True )
    data     = scalar( tag = 'DATA', data_type = esp.UnsignedByte, size = 1, null = True )
    ambientSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )


########################
@record_type('GRAS')

class GRAS(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    data     = structure( 'GRAS_3_DataData', tag = 'DATA', size = 32, null = True )


class GRAS_3_DataData(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Integer )


########################
@record_type('TREE')

class Tree(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    harvestIngredient = reference( tag = 'PFIG', refers_to = 'INGR', null = True )
    useSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    percentChance = scalar( tag = 'PFPC', data_type = esp.Integer, size = 4, null = True )
    fullname = subrecord_group( u'FULLNAME' )
    data     = structure( 'DataCnam', tag = 'CNAM', size = 48, null = True )


class DataCnam(Subrecord):
    trunkFlexibility = field( data_type = esp.Float )
    branchFlexibility = field( data_type = esp.Float )
    unknown0 = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Float )
    leafAmplitude = field( data_type = esp.Float )
    leafFrequency = field( data_type = esp.Float )


########################
@record_type('FLOR')

class Flora(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    verbString = scalar( tag = 'RNAM', data_type = esp.LString, size = 4, null = True )
    flag     = scalar( tag = 'FNAM', data_type = esp.Short, size = 2, null = True )
    resultItem = reference( tag = 'PFIG', refers_to = 'INGR', null = True )
    useSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    percentChance = scalar( tag = 'PFPC', data_type = esp.Integer, size = 4, null = True )


########################
@record_type('FURN')

class Furniture(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    destructible = subrecord_group( u'DESTRUCTIBLE' )
    mods     = scalar( tag = 'MODS', data_type = esp.Blob, null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Short, size = 2, null = True )
    keyword  = reference( tag = 'KNAM', refers_to = 'KYWD', null = True )
    mnam     = scalar( tag = 'MNAM', data_type = esp.Float, size = 4, null = True )
    wbdt     = scalar( tag = 'WBDT', data_type = esp.Short, size = 2, null = True )
    furniture_9 = subrecord_group_set( 'Furniture_9', null = True )
    fnpr     = structure_set( 'Fnpr', tag = 'FNPR', size = 4, null = True )
    xmrk     = scalar( tag = 'XMRK', data_type = esp.String, null = True )


class Furniture_9(SubrecordGroup):
    enam     = scalar( tag = 'ENAM', data_type = esp.Integer, size = 4 )
    furniture_9_1 = subrecord_group( 'Furniture_9_1' )


class Furniture_9_1(SubrecordGroup):
    nam0     = scalar_set( tag = 'NAM0', data_type = esp.Integer, size = 4, null = True )
    keyword  = reference_set( tag = 'FNMK', refers_to = 'KYWD', null = True )


class Fnpr(Subrecord):
    unknownShort = field( data_type = esp.Short )
    unknownShort = field( data_type = esp.Short )


########################
@record_type('WEAP')

class Weapon(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    enchantment = reference( tag = 'EITM', refers_to = 'ENCH', null = True )
    enchantmentChargeAmount = scalar( tag = 'EAMT', data_type = esp.Short, size = 2, null = True )
    equipment = reference( tag = 'ETYP', refers_to = 'EQUP', null = True )
    weaponBashImpactSet = reference( tag = 'BIDS', refers_to = 'IPDS', null = True )
    weaponBashMaterial = reference( tag = 'BAMT', refers_to = 'MATT', null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    itemDescription = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    projectileNode = structure( 'ProjectileNode', tag = 'NNAM', size = 11, null = True )
    impactDataSet = reference( tag = 'INAM', refers_to = 'IPDS', null = True )
    shoot3dSound = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    worldStatic = reference( tag = 'WNAM', refers_to = 'STAT', null = True )
    meleeswingOrGunnoAmmoSound = reference( tag = 'TNAM', refers_to = 'SNDR', null = True )
    idleSound = reference( tag = 'UNAM', refers_to = 'SNDR', null = True )
    equipSound = reference( tag = 'NAM9', refers_to = 'SNDR', null = True )
    unequipSound = reference( tag = 'NAM8', refers_to = 'SNDR', null = True )
    weaponData = structure( 'WeaponData', tag = 'DATA', size = 10, null = True )
    damageData = structure( 'DamageData', tag = 'DNAM', size = 100, null = True )
    criticalDamageData = structure( 'CriticalDamageData', tag = 'CRDT', size = 16, null = True )
    silencedYesno = scalar( tag = 'VNAM', data_type = esp.Integer, size = 4, null = True )
    templateWeapon = reference( tag = 'CNAM', refers_to = 'WEAP', null = True )


class ProjectileNode(Subrecord):
    nodeName = field( data_type = esp.LString )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Short )
    unknown3 = field( data_type = esp.Short )


class WeaponData(Subrecord):
    itemValue = field( data_type = esp.Integer )
    itemWeight = field( data_type = esp.Float )
    weaponDamage = field( data_type = esp.Short )


class DamageData(Subrecord):
    weaponType = field( data_type = esp.Integer )
    animationTimescale = field( data_type = esp.Float )
    zoomAnimationFloat = field( data_type = esp.Float )
    fireTrigger = field( data_type = esp.Short )
    secondaryTrigger = field( data_type = esp.Short )
    unknownByte = field( data_type = esp.Float )
    reloadAnimation = field( data_type = esp.Integer )
    unknownFormByte1 = field( data_type = esp.UnsignedByte )
    unknownFormByte2 = field( data_type = esp.UnsignedByte )
    ofProjectiles = field( data_type = esp.UnsignedByte )
    unknownFormByte4 = field( data_type = esp.UnsignedByte )
    minimumspreadinitialSpeedminRange = field( data_type = esp.Integer )
    maximumspreadmaximumSpeedmaxRange = field( data_type = esp.Integer )
    zoomFov  = field( data_type = esp.Integer )
    flags    = field( data_type = esp.Integer )
    projectileFormIdboolValueRelatedToBows = field( data_type = esp.Float )
    unknownValuespread = field( data_type = esp.Integer )
    weaponFiringAnimation = field( data_type = esp.Float )
    unknownValuedamageMultiplierprojectiles = field( data_type = esp.Integer )
    criticalDeathEffectChance = field( data_type = esp.Float )
    minRangeprojectilevelocity = field( data_type = esp.Integer )
    maxRange = field( data_type = esp.Integer )
    projectileBehavioronHitDismemberment = field( data_type = esp.Integer )
    weaponSkillUse = field( data_type = esp.Integer )
    weaponStanceOverride = field( data_type = esp.Integer )
    weaponSkillAnimationOverride = field( data_type = esp.Integer )
    weaponRelatedValue = field( data_type = esp.Integer )
    resistType = field( data_type = esp.Integer )
    weaponspeed = field( data_type = esp.Float )


class CriticalDamageData(Subrecord):
    criticalDamageBonus = field( data_type = esp.Integer )
    criticalChance = field( data_type = esp.Float )
    unknownInt = field( data_type = esp.Integer )
    criticalEffectSpell = reference_field( 'SPEL' )


########################
@record_type('AMMO')

class AmmunitionType(Record):
    object   = subrecord_group( u'OBJECT' )
    base_model = subrecord_group( u'BASE_MODEL' )
    carryable = subrecord_group( u'CARRYABLE' )
    description = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    ammoSettings = structure( 'AmmoSettings', tag = 'DATA', size = 16, null = True )


class AmmoSettings(Subrecord):
    projectile = reference_field( 'PROJ' )
    flags    = field( data_type = esp.Integer )
    damage   = field( data_type = esp.Float )
    value    = field( data_type = esp.Integer )


########################
@record_type('NPC_')

class Actor(Record):
    editorid = subrecord_group( u'EDITORID' )
    scripts  = subrecord_group( u'SCRIPTS' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    traits   = structure( 'Traits', tag = 'ACBS', size = 24 )
    factionTab = structure_set( 'FactionTab', tag = 'SNAM', size = 8, null = True )
    deathItem = reference( tag = 'INAM', refers_to = 'LVLI', null = True )
    voiceType = reference( tag = 'VTCK', refers_to = 'VTYP', null = True )
    templateNpcNpc_ = reference( tag = 'TPLT', refers_to = 'NPC_', null = True )
    raceType = reference( tag = 'RNAM', refers_to = 'RACE', null = True )
    destructible = subrecord_group( u'DESTRUCTIBLE' )
    totalSpellCount = scalar( tag = 'SPCT', data_type = esp.Integer, size = 4, null = True )
    spell    = reference_set( tag = 'SPLO', refers_to = 'SPEL', null = True )
    worldStatic = reference( tag = 'WNAM', refers_to = 'ARMO', null = True )
    armament = reference( tag = 'ANAM', refers_to = 'ARMO', null = True )
    attackRace = reference( tag = 'ATKR', refers_to = 'RACE', null = True )
    atkd     = structure( 'AtkdAtkd', tag = 'ATKD', size = 44, null = True )
    atke     = scalar( tag = 'ATKE', data_type = esp.String, null = True )
    ecor     = reference( tag = 'ECOR', refers_to = 'FLST', null = True )
    totalPerkCount = scalar( tag = 'PRKZ', data_type = esp.Integer, size = 4, null = True )
    perk     = structure_set( 'Perk', tag = 'PRKR', size = 8, null = True )
    containerTotalItemCount = scalar( tag = 'COCT', data_type = esp.Integer, size = 4, null = True )
    containerItem = structure_set( 'ContainerItem', tag = 'CNTO', size = 8, null = True )
    aiDataTab = structure( 'AiDataTab', tag = 'AIDT', size = 20, null = True )
    aiPackage = reference_set( tag = 'PKID', refers_to = 'PACK', null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    className = reference( tag = 'CNAM', refers_to = 'CLAS', null = True )
    fullname = subrecord_group( u'FULLNAME' )
    shortIngameName = scalar( tag = 'SHRT', data_type = esp.LString, null = True )
    dataBufferAlwaysEmpty = structure( 'DataBufferAlwaysEmpty', tag = 'DATA', null = True )
    statsTab = structure( 'StatsTab', tag = 'DNAM', size = 52, null = True )
    headPart = reference_set( tag = 'PNAM', refers_to = 'HDPT', null = True )
    hairColor = reference( tag = 'HCLF', refers_to = 'CLFM', null = True )
    combatStyle = reference( tag = 'ZNAM', refers_to = 'CSTY', null = True )
    gift     = reference( tag = 'GNAM', refers_to = 'FLST', null = True )
    unknownFlag = scalar( tag = 'NAM5', data_type = esp.UnsignedShort, null = True )
    height   = scalar( tag = 'NAM6', data_type = esp.Float, size = 4 )
    weight   = scalar( tag = 'NAM7', data_type = esp.Float, size = 4 )
    soundLevel = scalar( tag = 'NAM8', data_type = esp.UnsignedInteger, size = 4 )
    actor_38 = subrecord_group_set( 'Actor_38', null = True )
    soundTemplateNpc_ = reference( tag = 'CSCR', refers_to = 'NPC_', null = True )
    dailyOutfit = reference( tag = 'DOFT', refers_to = 'OTFT', null = True )
    sleepOutfit = reference( tag = 'SOFT', refers_to = 'OTFT', null = True )
    dailyPackageList = reference( tag = 'DPLT', refers_to = 'FLST', null = True )
    crimeFaction = reference( tag = 'CRIF', refers_to = 'FACT', null = True )
    skinComplexion = reference( tag = 'FTST', refers_to = 'TXST', null = True )
    qnam     = structure( 'Qnam', tag = 'QNAM', size = 12, null = True )
    characterGenMorphsTab = structure( 'CharacterGenMorphsTab', tag = 'NAM9', size = 76, null = True )
    chargenMorphsTabPulldownsFaceparts = structure( 'ChargenMorphsTabPulldownsFaceparts', tag = 'NAMA', size = 16, null = True )
    actor_48 = subrecord_group_set( 'Actor_48', null = True )


class Traits(Subrecord):
    uageprun = field( data_type = esp.UnsignedByte )
    summonableprotected = field( data_type = esp.UnsignedByte )
    oppgendanimsnobleedsimpactor = field( data_type = esp.UnsignedByte )
    invulnerableisghost = field( data_type = esp.UnsignedByte )
    spellPoints = field( data_type = esp.UnsignedShort )
    fatigue  = field( data_type = esp.UnsignedShort )
    baseLevel = field( data_type = esp.UnsignedByte )
    startLevel = field( data_type = esp.UnsignedByte )
    altLevel = field( data_type = esp.UnsignedByte )
    altLevel = field( data_type = esp.UnsignedByte )
    calcmin  = field( data_type = esp.UnsignedShort )
    speed    = field( data_type = esp.UnsignedShort )
    dispositionBase = field( data_type = esp.UnsignedShort )
    extraFlags = field( data_type = esp.UnsignedByte )
    unknown2 = field( data_type = esp.UnsignedByte )
    unknown3 = field( data_type = esp.UnsignedInteger )


class FactionTab(Subrecord):
    faction  = reference_field( 'FACT' )
    rank     = field( data_type = esp.UnsignedByte )
    unknown  = field( data_type = esp.UnsignedByte )
    flag     = field( data_type = esp.UnsignedShort )


class AtkdAtkd(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    spell    = reference_field( 'SPEL' )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )
    unknown9 = field( data_type = esp.Integer )
    unknown10 = field( data_type = esp.Float )


class Perk(Subrecord):
    formid   = reference_field( 'PERK' )
    unknown  = field( data_type = esp.UnsignedInteger )


class ContainerItem(Subrecord):
    formid   = field( data_type = esp.Reference )
    count    = field( data_type = esp.Integer )


class AiDataTab(Subrecord):
    aggression = field( data_type = esp.UnsignedByte )
    confidence = field( data_type = esp.UnsignedByte )
    energy   = field( data_type = esp.UnsignedByte )
    morality = field( data_type = esp.UnsignedByte )
    mood     = field( data_type = esp.UnsignedByte )
    assistance = field( data_type = esp.UnsignedByte )
    unknownByte1 = field( data_type = esp.UnsignedByte )
    unknownByte2 = field( data_type = esp.UnsignedByte )
    aggroWarn = field( data_type = esp.Float )
    aggroWarnattack = field( data_type = esp.Float )
    aggroWarnattack = field( data_type = esp.Float )


class DataBufferAlwaysEmpty(Subrecord):
    pass


class StatsTab(Subrecord):
    onehandedBase = field( data_type = esp.UnsignedByte )
    twohandedBase = field( data_type = esp.UnsignedByte )
    marksmanBase = field( data_type = esp.UnsignedByte )
    blockBase = field( data_type = esp.UnsignedByte )
    smithingBase = field( data_type = esp.UnsignedByte )
    heavyarmorBase = field( data_type = esp.UnsignedByte )
    lightarmorBase = field( data_type = esp.UnsignedByte )
    pickpocketBase = field( data_type = esp.UnsignedByte )
    lockpickingBase = field( data_type = esp.UnsignedByte )
    sneakBase = field( data_type = esp.UnsignedByte )
    alchemyBase = field( data_type = esp.UnsignedByte )
    speechcraftBase = field( data_type = esp.UnsignedByte )
    alterationBase = field( data_type = esp.UnsignedByte )
    conjurationBase = field( data_type = esp.UnsignedByte )
    destructionBase = field( data_type = esp.UnsignedByte )
    illusionBase = field( data_type = esp.UnsignedByte )
    restorationBase = field( data_type = esp.UnsignedByte )
    enchantingBase = field( data_type = esp.UnsignedByte )
    onehandedMod = field( data_type = esp.Byte )
    twohandedMod = field( data_type = esp.Byte )
    marksmanMod = field( data_type = esp.Byte )
    blockMod = field( data_type = esp.Byte )
    smithingMod = field( data_type = esp.Byte )
    heavyarmorMod = field( data_type = esp.Byte )
    lightarmorMod = field( data_type = esp.Byte )
    pickpocketMod = field( data_type = esp.Byte )
    lockpickingMod = field( data_type = esp.Byte )
    sneakMod = field( data_type = esp.Byte )
    alchemyMod = field( data_type = esp.Byte )
    speechcraftMod = field( data_type = esp.Byte )
    alterationMod = field( data_type = esp.Byte )
    conjurationMod = field( data_type = esp.Byte )
    destructionMod = field( data_type = esp.Byte )
    illusionMod = field( data_type = esp.Byte )
    restorationMod = field( data_type = esp.Byte )
    enchantingMod = field( data_type = esp.Byte )
    health   = field( data_type = esp.UnsignedShort )
    magika   = field( data_type = esp.UnsignedShort )
    stamina  = field( data_type = esp.UnsignedShort )
    baseArmorunarmed = field( data_type = esp.UnsignedShort )
    flags1   = field( data_type = esp.UnsignedShort )
    unknown1 = field( data_type = esp.UnsignedShort )
    unknown2 = field( data_type = esp.UnsignedShort )
    unknown3 = field( data_type = esp.UnsignedShort )


class Actor_38(SubrecordGroup):
    soundType = scalar( tag = 'CSDT', data_type = esp.Integer, size = 4 )
    actorSound = reference( tag = 'CSDI', refers_to = 'SNDR', null = True )
    soundChance = scalar( tag = 'CSDC', data_type = esp.UnsignedByte, size = 1, null = True )


class Qnam(Subrecord):
    unknownFloat1 = field( data_type = esp.Float )
    unknownFloat2 = field( data_type = esp.Float )
    unknownFloat3 = field( data_type = esp.Float )


class CharacterGenMorphsTab(Subrecord):
    noseLength = field( data_type = esp.Float )
    noseHeight = field( data_type = esp.Float )
    jawHeight = field( data_type = esp.Float )
    jawWidth = field( data_type = esp.Float )
    jawDepth = field( data_type = esp.Float )
    cheekboneHeight = field( data_type = esp.Float )
    cheekboneWidth = field( data_type = esp.Float )
    eyesHeight = field( data_type = esp.Float )
    eyesWidth = field( data_type = esp.Float )
    browHeight = field( data_type = esp.Float )
    browWidth = field( data_type = esp.Float )
    browDepth = field( data_type = esp.Float )
    mouthHeight = field( data_type = esp.Float )
    mouthDepth = field( data_type = esp.Float )
    chinWidth = field( data_type = esp.Float )
    chinLength = field( data_type = esp.Float )
    chinDepth = field( data_type = esp.Float )
    eyesDepth = field( data_type = esp.Float )
    bufferflags4bytes = field( data_type = esp.UnsignedInteger )


class ChargenMorphsTabPulldownsFaceparts(Subrecord):
    nosetype = field( data_type = esp.Integer )
    unknown4bytes = field( data_type = esp.Integer )
    eyestype = field( data_type = esp.Integer )
    mouthtype = field( data_type = esp.Integer )


class Actor_48(SubrecordGroup):
    tintMaskIndex = scalar( tag = 'TINI', data_type = esp.Short, size = 2 )
    tintMaskColor = scalar( tag = 'TINC', data_type = esp.Color, null = True )
    tintMaskValue = scalar( tag = 'TINV', data_type = esp.Integer, size = 4, null = True )
    tias     = scalar( tag = 'TIAS', data_type = esp.Short, size = 2, null = True )


########################
@record_type('LVLN')

class LeveledActor(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    leveled  = subrecord_group( u'LEVELED' )
    base_model = subrecord_group( u'BASE_MODEL' )


########################
@record_type('KEYM')

class Key(Record):
    scripted_model = subrecord_group( u'SCRIPTED_MODEL', null = True )
    carryable = subrecord_group( u'CARRYABLE' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    specs    = structure( 'Specs', tag = 'DATA' )


class Specs(Subrecord):
    value    = field( data_type = esp.UnsignedInteger )
    weight   = field( data_type = esp.Float )


########################
@record_type('ALCH')

class Potion(Record):
    object   = subrecord_group( u'OBJECT' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    carryable = subrecord_group( u'CARRYABLE' )
    itemData = scalar( tag = 'DATA', data_type = esp.Float, size = 4, null = True )
    enchantmentInfoAndType = structure( 'EnchantmentInfoAndType', tag = 'ENIT', size = 20, null = True )
    effect   = subrecord_group_set( u'EFFECT', null = True )


class EnchantmentInfoAndType(Subrecord):
    itemValue = field( data_type = esp.Integer )
    itemType = field( data_type = esp.Integer )
    padding1 = field( data_type = esp.Integer )
    padding2 = field( data_type = esp.Integer )
    useSound = reference_field( 'SNDR' )


########################
@record_type('IDLM')

class IdleForm(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    idlf     = scalar( tag = 'IDLF', data_type = esp.UnsignedByte, size = 1, null = True )
    idleCount = scalar( tag = 'IDLC', data_type = esp.UnsignedByte, size = 1, null = True )
    idlt     = scalar( tag = 'IDLT', data_type = esp.Float, size = 4, null = True )
    idleAnim = reference_set( tag = 'IDLA', refers_to = 'IDLE', null = True )


########################
@record_type('COBJ')

class ConstructibleObject(Record):
    editorid = subrecord_group( u'EDITORID' )
    componentTotalItemCount = scalar( tag = 'COCT', data_type = esp.Integer, size = 4, null = True )
    componentObject = structure_set( 'ComponentObject', tag = 'CNTO', size = 8, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    outputObject = scalar_set( tag = 'CNAM', data_type = esp.Reference, null = True )
    craftingStation = reference( tag = 'BNAM', refers_to = 'KYWD', null = True )
    resultingQuantity = scalar( tag = 'NAM1', data_type = esp.Short, size = 2, null = True )


class ComponentObject(Subrecord):
    object   = reference_field( 'MISC' )
    requiredQuantity = field( data_type = esp.Integer )


########################
@record_type('PROJ')

class Projectile(Record):
    object   = subrecord_group( u'OBJECT' )
    base_model = subrecord_group( u'BASE_MODEL' )
    destructible = subrecord_group( u'DESTRUCTIBLE' )
    projectileData = structure( 'ProjectileData', tag = 'DATA', null = True )
    effectModel = scalar( tag = 'NAM1', data_type = esp.String, null = True )
    effectData = scalar( tag = 'NAM2', data_type = esp.Blob, null = True )
    silencedYesno = scalar( tag = 'VNAM', data_type = esp.Integer, size = 4, null = True )


class ProjectileData(Subrecord):
    flags    = field( data_type = esp.Integer )
    acceleration = field( data_type = esp.Float )
    initialSpeedminimumrange = field( data_type = esp.Float )
    maxSpeedmaximumRange = field( data_type = esp.Float )
    light    = reference_field( 'LIGH' )
    light2   = reference_field( 'LIGH' )
    value6   = field( data_type = esp.Integer )
    endOfRow2 = field( data_type = esp.Integer )
    value8   = field( data_type = esp.Integer )
    explosion1 = reference_field( 'EXPL' )
    sound1   = reference_field( 'SNDR' )
    endOfRow3 = field( data_type = esp.Integer )
    value10  = field( data_type = esp.Float )
    value11  = field( data_type = esp.Float )
    value12  = field( data_type = esp.Integer )
    endOfRow4 = field( data_type = esp.Integer )
    value13  = field( data_type = esp.Integer )
    value14  = field( data_type = esp.Float )
    forcemultiplier = field( data_type = esp.Float )
    endOfRow5 = field( data_type = esp.Integer )
    value16  = field( data_type = esp.Float )
    value17  = field( data_type = esp.Integer )
    value18  = field( data_type = esp.Integer, null = True )


########################
@record_type('HAZD')

class Hazard(Record):
    object   = subrecord_group( u'OBJECT' )
    base_model = subrecord_group( u'BASE_MODEL' )
    imageSpaceModifier = reference( tag = 'MNAM', refers_to = 'IMAD', null = True )
    data     = structure( 'Hazard_3_DataData', tag = 'DATA', size = 40, null = True )


class Hazard_3_DataData(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Integer )
    spell    = reference_field( 'SPEL' )
    lighFormid = reference_field( 'LIGH' )
    unknown8 = field( data_type = esp.Integer )
    sndrFormid = reference_field( 'SNDR' )


########################
@record_type('SLGM')

class SoulGem(Record):
    object   = subrecord_group( u'OBJECT' )
    base_model = subrecord_group( u'BASE_MODEL' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    data     = structure( 'SoulGem_3_DataData', tag = 'DATA', size = 8, null = True )
    currentSoul = scalar( tag = 'SOUL', data_type = esp.UnsignedByte, size = 1, null = True )
    soulGemCapacity = scalar( tag = 'SLCP', data_type = esp.UnsignedByte, size = 1, null = True )
    soulGem  = reference( tag = 'NAM0', refers_to = 'SLGM', null = True )


class SoulGem_3_DataData(Subrecord):
    value    = field( data_type = esp.Integer )
    weight   = field( data_type = esp.Float )


########################
@record_type('LVLI')

class LeveledItem(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    leveled  = subrecord_group( u'LEVELED' )
    globalVariable = reference( tag = 'LVLG', refers_to = 'GLOB', null = True )


########################
@record_type('WTHR')

class Weather(Record):
    editorid = subrecord_group( u'EDITORID' )
    dnam     = structure( 'Weather_1_DnamDnam', tag = 'DNAM', size = 35, null = True )
    cnam     = structure( 'Cnam', tag = 'CNAM', size = 32, null = True )
    anam     = structure( 'Weather_3_AnamAnam', tag = 'ANAM', size = 14, null = True )
    bnam     = structure( 'Bnam', tag = 'BNAM', size = 35, null = True )
    dynamicCloudTexture = scalar( tag = '00TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '10TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '20TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '30TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '40TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '50TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '60TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '70TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '80TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '90TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = ':0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = ';0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '<0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '=0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '>0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '?0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = '@0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'A0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'B0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'C0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'D0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'E0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'F0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'G0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'H0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'I0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'J0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'K0TX', data_type = esp.String, null = True )
    dynamicCloudTexture = scalar( tag = 'L0TX', data_type = esp.String, null = True )
    lnam     = scalar( tag = 'LNAM', data_type = esp.Integer, size = 4, null = True )
    shaderParticleGeometry = reference( tag = 'MNAM', refers_to = 'SPGD', null = True )
    refraction = reference( tag = 'NNAM', refers_to = 'RFCT', null = True )
    onam     = scalar( tag = 'ONAM', data_type = esp.Integer, size = 4, null = True )
    rnam     = structure( 'Rnam', tag = 'RNAM', size = 32, null = True )
    qnam     = structure( 'QnamQnam', tag = 'QNAM', size = 32, null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Blob, null = True )
    jnam     = scalar( tag = 'JNAM', data_type = esp.Blob, null = True )
    typetimeOfLight = structure( 'TypetimeOfLight', tag = 'NAM0', null = True )
    fogDistance = structure( 'FogDistance', tag = 'FNAM', size = 32, null = True )
    windglaredamageetcSlidersNumbersAreNotAccurateSpecialConvertionIsNeeded = structure( 'WindglaredamageetcSlidersNumbersAreNotAccurateSpecialConvertionIsNeeded', tag = 'DATA', size = 19, null = True )
    nam1     = scalar( tag = 'NAM1', data_type = esp.Integer, size = 4, null = True )
    soundTab = structure_set( 'SoundTab', tag = 'SNAM', size = 8, null = True )
    staticClouds = reference_set( tag = 'TNAM', refers_to = 'STAT', null = True )
    imageSpaces = structure( 'ImageSpaces', tag = 'IMSP', size = 16, null = True )
    dalc     = scalar_set( tag = 'DALC', data_type = esp.Blob, null = True )
    nam2     = structure( 'Nam2', tag = 'NAM2', size = 16, null = True )
    nam3     = structure( 'Nam3Nam3', tag = 'NAM3', size = 16, null = True )
    base_model = subrecord_group( u'BASE_MODEL' )


class Weather_1_DnamDnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Short )
    unknown9 = field( data_type = esp.Short )


class Cnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )


class Weather_3_AnamAnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Short )


class Bnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Short )
    unknown9 = field( data_type = esp.Short )


class Rnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )


class QnamQnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )


class TypetimeOfLight(Subrecord):
    skyUpperSunriseR = field( data_type = esp.UnsignedByte )
    skyUpperSunriseG = field( data_type = esp.UnsignedByte )
    skyUpperSunriseB = field( data_type = esp.Short )
    skyUpperDayR = field( data_type = esp.UnsignedByte )
    skyUpperDayG = field( data_type = esp.UnsignedByte )
    skyUpperDayB = field( data_type = esp.Short )
    skyUpperSunsetR = field( data_type = esp.UnsignedByte )
    skyUpperSunsetG = field( data_type = esp.UnsignedByte )
    skyUpperSunsetB = field( data_type = esp.Short )
    skyUpperNightR = field( data_type = esp.UnsignedByte )
    skyUpperNightG = field( data_type = esp.UnsignedByte )
    skyUpperNightB = field( data_type = esp.Short )
    fogNearSunriseR = field( data_type = esp.UnsignedByte )
    fogNearSunriseG = field( data_type = esp.UnsignedByte )
    fogNearSunriseB = field( data_type = esp.Short )
    fogNearDayR = field( data_type = esp.UnsignedByte )
    fogNearDayG = field( data_type = esp.UnsignedByte )
    fogNearDayB = field( data_type = esp.Short )
    fogNearSunsetR = field( data_type = esp.UnsignedByte )
    fogNearSunsetG = field( data_type = esp.UnsignedByte )
    fogNearSunsetB = field( data_type = esp.Short )
    fogNearNightR = field( data_type = esp.UnsignedByte )
    fogNearNightG = field( data_type = esp.UnsignedByte )
    fogNearNightB = field( data_type = esp.Short )
    cloudLayerAreAlwaysZeroes = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    ambientSunriseR = field( data_type = esp.UnsignedByte )
    ambientSunriseG = field( data_type = esp.UnsignedByte )
    ambientSunriseB = field( data_type = esp.Short )
    ambientDayR = field( data_type = esp.UnsignedByte )
    ambientDayG = field( data_type = esp.UnsignedByte )
    ambientDayB = field( data_type = esp.Short )
    ambientSunsetR = field( data_type = esp.UnsignedByte )
    ambientSunsetG = field( data_type = esp.UnsignedByte )
    ambientSunsetB = field( data_type = esp.Short )
    ambientNightR = field( data_type = esp.UnsignedByte )
    ambientNightG = field( data_type = esp.UnsignedByte )
    ambientNightB = field( data_type = esp.Short )
    sunlightSunriseR = field( data_type = esp.UnsignedByte )
    sunlightSunriseG = field( data_type = esp.UnsignedByte )
    sunlightSunriseB = field( data_type = esp.Short )
    sunlightDayR = field( data_type = esp.UnsignedByte )
    sunlightDayG = field( data_type = esp.UnsignedByte )
    sunlightDayB = field( data_type = esp.Short )
    sunlightSunsetR = field( data_type = esp.UnsignedByte )
    sunlightSunsetG = field( data_type = esp.UnsignedByte )
    sunlightSunsetB = field( data_type = esp.Short )
    sunlightNightR = field( data_type = esp.UnsignedByte )
    sunlightNightG = field( data_type = esp.UnsignedByte )
    sunlightNightB = field( data_type = esp.Short )
    sunSunriseR = field( data_type = esp.UnsignedByte )
    sunSunriseG = field( data_type = esp.UnsignedByte )
    sunSunriseB = field( data_type = esp.Short )
    sunDayR  = field( data_type = esp.UnsignedByte )
    sunDayG  = field( data_type = esp.UnsignedByte )
    sunDayB  = field( data_type = esp.Short )
    sunSunsetR = field( data_type = esp.UnsignedByte )
    sunSunsetG = field( data_type = esp.UnsignedByte )
    sunSunsetB = field( data_type = esp.Short )
    sunNightR = field( data_type = esp.UnsignedByte )
    sunNightG = field( data_type = esp.UnsignedByte )
    sunNightB = field( data_type = esp.Short )
    starsSunriseR = field( data_type = esp.UnsignedByte )
    starsSunriseG = field( data_type = esp.UnsignedByte )
    starsSunriseB = field( data_type = esp.Short )
    starsDayR = field( data_type = esp.UnsignedByte )
    starsDayG = field( data_type = esp.UnsignedByte )
    starsDayB = field( data_type = esp.Short )
    starsSunsetR = field( data_type = esp.UnsignedByte )
    starsSunsetG = field( data_type = esp.UnsignedByte )
    starsSunsetB = field( data_type = esp.Short )
    starsNightR = field( data_type = esp.UnsignedByte )
    starsNightG = field( data_type = esp.UnsignedByte )
    starsNightB = field( data_type = esp.Short )
    skyLowerSunriseR = field( data_type = esp.UnsignedByte )
    skyLowerSunriseG = field( data_type = esp.UnsignedByte )
    skyLowerSunriseB = field( data_type = esp.Short )
    skyLowerDayR = field( data_type = esp.UnsignedByte )
    skyLowerDayG = field( data_type = esp.UnsignedByte )
    skyLowerDayB = field( data_type = esp.Short )
    skyLowerSunsetR = field( data_type = esp.UnsignedByte )
    skyLowerSunsetG = field( data_type = esp.UnsignedByte )
    skyLowerSunsetB = field( data_type = esp.Short )
    skyLowerNightR = field( data_type = esp.UnsignedByte )
    skyLowerNightG = field( data_type = esp.UnsignedByte )
    skyLowerNightB = field( data_type = esp.Short )
    horizonSunriseR = field( data_type = esp.UnsignedByte )
    horizonSunriseG = field( data_type = esp.UnsignedByte )
    horizonSunriseB = field( data_type = esp.Short )
    horizonDayR = field( data_type = esp.UnsignedByte )
    horizonDayG = field( data_type = esp.UnsignedByte )
    horizonDayB = field( data_type = esp.Short )
    horizonSunsetR = field( data_type = esp.UnsignedByte )
    horizonSunsetG = field( data_type = esp.UnsignedByte )
    horizonSunsetB = field( data_type = esp.Short )
    horizonNightR = field( data_type = esp.UnsignedByte )
    horizonNightG = field( data_type = esp.UnsignedByte )
    horizonNightB = field( data_type = esp.Short )
    effectLightingSunriseR = field( data_type = esp.UnsignedByte )
    effectLightingSunriseG = field( data_type = esp.UnsignedByte )
    effectLightingSunriseB = field( data_type = esp.Short )
    effectLightingDayR = field( data_type = esp.UnsignedByte )
    effectLightingDayG = field( data_type = esp.UnsignedByte )
    effectLightingDayB = field( data_type = esp.Short )
    effectLightingSunsetR = field( data_type = esp.UnsignedByte )
    effectLightingSunsetG = field( data_type = esp.UnsignedByte )
    effectLightingSunsetB = field( data_type = esp.Short )
    effectLightingNightR = field( data_type = esp.UnsignedByte )
    effectLightingNightG = field( data_type = esp.UnsignedByte )
    effectLightingNightB = field( data_type = esp.Short )
    cloudLodDiffuseSunriseR = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseSunriseG = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseSunriseB = field( data_type = esp.Short )
    cloudLodDiffuseDayR = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseDayG = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseDayB = field( data_type = esp.Short )
    cloudLodDiffuseSunsetR = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseSunsetG = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseSunsetB = field( data_type = esp.Short )
    cloudLodDiffuseNightR = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseNightG = field( data_type = esp.UnsignedByte )
    cloudLodDiffuseNightB = field( data_type = esp.Short )
    cloudLodAmbientSunriseR = field( data_type = esp.UnsignedByte )
    cloudLodAmbientSunriseG = field( data_type = esp.UnsignedByte )
    cloudLodAmbientSunriseB = field( data_type = esp.Short )
    cloudLodAmbientDayR = field( data_type = esp.UnsignedByte )
    cloudLodAmbientDayG = field( data_type = esp.UnsignedByte )
    cloudLodAmbientDayB = field( data_type = esp.Short )
    cloudLodAmbientSunsetR = field( data_type = esp.UnsignedByte )
    cloudLodAmbientSunsetG = field( data_type = esp.UnsignedByte )
    cloudLodAmbientSunsetB = field( data_type = esp.Short )
    cloudLodAmbientNightR = field( data_type = esp.UnsignedByte )
    cloudLodAmbientNightG = field( data_type = esp.UnsignedByte )
    cloudLodAmbientNightB = field( data_type = esp.Short )
    fogFarSunriseR = field( data_type = esp.UnsignedByte )
    fogFarSunriseG = field( data_type = esp.UnsignedByte )
    fogFarSunriseB = field( data_type = esp.Short )
    fogFarDayR = field( data_type = esp.UnsignedByte )
    fogFarDayG = field( data_type = esp.UnsignedByte )
    fogFarDayB = field( data_type = esp.Short )
    fogFarSunsetR = field( data_type = esp.UnsignedByte )
    fogFarSunsetG = field( data_type = esp.UnsignedByte )
    fogFarSunsetB = field( data_type = esp.Short )
    fogFarNightR = field( data_type = esp.UnsignedByte )
    fogFarNightG = field( data_type = esp.UnsignedByte )
    fogFarNightB = field( data_type = esp.Short )
    skyStaticsSunriseR = field( data_type = esp.UnsignedByte )
    skyStaticsSunriseG = field( data_type = esp.UnsignedByte )
    skyStaticsSunriseB = field( data_type = esp.Short )
    skyStaticsDayR = field( data_type = esp.UnsignedByte )
    skyStaticsDayG = field( data_type = esp.UnsignedByte )
    skyStaticsDayB = field( data_type = esp.Short )
    skyStaticsSunsetR = field( data_type = esp.UnsignedByte )
    skyStaticsSunsetG = field( data_type = esp.UnsignedByte )
    skyStaticsSunsetB = field( data_type = esp.Short )
    skyStaticsNightR = field( data_type = esp.UnsignedByte )
    skyStaticsNightG = field( data_type = esp.UnsignedByte )
    skyStaticsNightB = field( data_type = esp.Short )
    waterMultiplierSunriseR = field( data_type = esp.UnsignedByte )
    waterMultiplierSunriseG = field( data_type = esp.UnsignedByte )
    waterMultiplierSunriseB = field( data_type = esp.Short )
    waterMultiplierDayR = field( data_type = esp.UnsignedByte )
    waterMultiplierDayG = field( data_type = esp.UnsignedByte )
    waterMultiplierDayB = field( data_type = esp.Short )
    waterMultiplierSunsetR = field( data_type = esp.UnsignedByte )
    waterMultiplierSunsetG = field( data_type = esp.UnsignedByte )
    waterMultiplierSunsetB = field( data_type = esp.Short )
    waterMultiplierNightR = field( data_type = esp.UnsignedByte )
    waterMultiplierNightG = field( data_type = esp.UnsignedByte )
    waterMultiplierNightB = field( data_type = esp.Short )
    sunGlareSunriseR = field( data_type = esp.UnsignedByte )
    sunGlareSunriseG = field( data_type = esp.UnsignedByte )
    sunGlareSunriseB = field( data_type = esp.Short )
    sunGlareDayR = field( data_type = esp.UnsignedByte )
    sunGlareDayG = field( data_type = esp.UnsignedByte )
    sunGlareDayB = field( data_type = esp.Short )
    sunGlareSunsetR = field( data_type = esp.UnsignedByte )
    sunGlareSunsetG = field( data_type = esp.UnsignedByte )
    sunGlareSunsetB = field( data_type = esp.Short )
    sunGlareNightR = field( data_type = esp.UnsignedByte )
    sunGlareNightG = field( data_type = esp.UnsignedByte )
    sunGlareNightB = field( data_type = esp.Short )
    moonGlareSunriseR = field( data_type = esp.UnsignedByte )
    moonGlareSunriseG = field( data_type = esp.UnsignedByte )
    moonGlareSunriseB = field( data_type = esp.Short )
    moonGlareDayR = field( data_type = esp.UnsignedByte )
    moonGlareDayG = field( data_type = esp.UnsignedByte )
    moonGlareDayB = field( data_type = esp.Short )
    moonGlareSunsetR = field( data_type = esp.UnsignedByte )
    moonGlareSunsetG = field( data_type = esp.UnsignedByte )
    moonGlareSunsetB = field( data_type = esp.Short )
    moonGlareNightR = field( data_type = esp.UnsignedByte )
    moonGlareNightG = field( data_type = esp.UnsignedByte )
    moonGlareNightB = field( data_type = esp.Short )


class FogDistance(Subrecord):
    dayNear  = field( data_type = esp.Float )
    dayFar   = field( data_type = esp.Float )
    nightNear = field( data_type = esp.Float )
    nightFar = field( data_type = esp.Float )
    dayPow   = field( data_type = esp.Float )
    nightPow = field( data_type = esp.Float )
    dayMax   = field( data_type = esp.Float )
    nightMax = field( data_type = esp.Float )


class WindglaredamageetcSlidersNumbersAreNotAccurateSpecialConvertionIsNeeded(Subrecord):
    windSpeedtransDelta = field( data_type = esp.Integer )
    sunDamageglare = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    windDirection = field( data_type = esp.Short )
    windDirRange = field( data_type = esp.UnsignedByte )


class SoundTab(Subrecord):
    sndrFormid = reference_field( 'SNDR' )
    always0  = field( data_type = esp.Integer )


class ImageSpaces(Subrecord):
    sunriseFormid = reference_field( 'IMGS' )
    dayFormid = reference_field( 'IMGS' )
    sunsetFormid = reference_field( 'IMGS' )
    nightFormid = reference_field( 'IMGS' )


class Nam2(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


class Nam3Nam3(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


########################
@record_type('CLMT')

class Climate(Record):
    editorid = subrecord_group( u'EDITORID' )
    weather  = structure( 'WeatherWlst', tag = 'WLST', size = 12, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Blob, null = True )
    gnam     = scalar( tag = 'GNAM', data_type = esp.Blob, null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    tnam     = structure( 'Tnam', tag = 'TNAM', size = 6, null = True )


class WeatherWlst(Subrecord):
    wthrFormid = reference_field( 'WTHR' )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


class Tnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Short )


########################
@record_type('SPGD')

class SPGD(Record):
    editorid = subrecord_group( u'EDITORID' )
    data     = scalar( tag = 'DATA', data_type = esp.Blob, null = True )
    icon     = scalar( tag = 'ICON', data_type = esp.String, null = True )


########################
@record_type('RFCT')

class RFCT(Record):
    editorid = subrecord_group( u'EDITORID' )
    artAndEffectShader = structure( 'ArtAndEffectShader', tag = 'DATA', size = 12, null = True )


class ArtAndEffectShader(Subrecord):
    artoFormid = reference_field( 'ARTO' )
    efshFormid = reference_field( 'EFSH' )
    unknown2 = field( data_type = esp.Integer )


########################
@record_type('REGN')

class REGN(Record):
    editorid = subrecord_group( u'EDITORID' )
    rclr     = scalar( tag = 'RCLR', data_type = esp.Integer, size = 4, null = True )
    wnam     = scalar( tag = 'WNAM', data_type = esp.Integer, size = 4, null = True )
    regn_3   = subrecord_group_set( 'REGN_3', null = True )
    regn_4   = subrecord_group_set( 'REGN_4', null = True )


class REGN_3(SubrecordGroup):
    rpli     = scalar_set( tag = 'RPLI', data_type = esp.LString, size = 4, null = True )
    rpld     = scalar_set( tag = 'RPLD', data_type = esp.Blob, null = True )


class REGN_4(SubrecordGroup):
    rdat     = structure_set( 'Rdat', tag = 'RDAT', size = 8, null = True )
    icon     = scalar( tag = 'ICON', data_type = esp.String, null = True )
    rdot     = structure( 'Rdot', tag = 'RDOT', null = True )
    music    = reference( tag = 'RDMO', refers_to = 'MUSC', null = True )
    weather  = reference_set( tag = 'RDWT', refers_to = 'WTHR', null = True )
    rdmp     = scalar( tag = 'RDMP', data_type = esp.LString, size = 4, null = True )
    sound    = reference_set( tag = 'RDSA', refers_to = 'SNDR', null = True )


class Rdat(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.LString )


class Rdot(Subrecord):
    pass


########################
@record_type('DIAL')

class DialogueTopic(Record):
    concept  = subrecord_group( u'CONCEPT' )
    topicPriority = scalar( tag = 'PNAM', data_type = esp.Float, size = 4, null = True )
    dialogBranch = reference( tag = 'BNAM', refers_to = 'DLBR', null = True )
    quest    = reference( tag = 'QNAM', refers_to = 'QUST', null = True )
    data     = scalar( tag = 'DATA', data_type = esp.Integer, size = 4, null = True )
    snam     = scalar( tag = 'SNAM', data_type = esp.Integer, size = 4, null = True )
    tifc     = scalar( tag = 'TIFC', data_type = esp.Integer, size = 4, null = True )


########################
@record_type('INFO')

class DialogueInfo(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    dialogueText = scalar( tag = 'NAM1', data_type = esp.LString, size = 4 )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    actorNotes = scalar( tag = 'NAM2', data_type = esp.String, null = True )
    unknown  = scalar( tag = 'NAM3', data_type = esp.UnsignedByte, null = True )
    favorLevel = scalar( tag = 'CNAM', data_type = esp.UnsignedByte, null = True )
    flags    = structure( 'FlagsEnam', tag = 'ENAM' )
    possiblePlayerResponses = reference_set( tag = 'TCLT', refers_to = 'INFO', null = True )
    emotion  = structure( 'Emotion', tag = 'TRDT' )
    scripts  = subrecord_group( u'SCRIPTS' )
    playerResponse = reference( tag = 'RNAM', refers_to = 'INFO', null = True )
    showResponseDataFromInfo = reference( tag = 'DNAM', refers_to = 'INFO', null = True )
    audioOutputOverride = reference( tag = 'ONAM', refers_to = 'SOPM', null = True )
    speakerIdle = reference( tag = 'SNAM', refers_to = 'IDLE', null = True )
    listenerIdle = reference( tag = 'SNAM', refers_to = 'IDLE', null = True )


class FlagsEnam(Subrecord):
    flags    = field( data_type = esp.UnsignedShort )
    scaledHoursUntilReset = field( data_type = esp.UnsignedShort )


class Emotion(Subrecord):
    emotionType = field( data_type = esp.UnsignedInteger )
    emotionValue = field( data_type = esp.UnsignedInteger )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )


class QUEST_ALID(SubrecordGroup):
    alid     = scalar_set( tag = 'ALID', data_type = esp.String, null = True )
    fnam     = scalar_set( tag = 'FNAM', data_type = esp.LString, size = 4, null = True )
    alfa     = scalar_set( tag = 'ALFA', data_type = esp.Integer, size = 4, null = True )
    alertLocationRefType = reference_set( tag = 'ALRT', refers_to = 'LCRT', null = True )
    alna     = scalar_set( tag = 'ALNA', data_type = esp.Integer, size = 4, null = True )
    alnt     = scalar_set( tag = 'ALNT', data_type = esp.Integer, size = 4, null = True )
    externalAliasReference = reference_set( tag = 'ALEQ', refers_to = 'QUST', null = True )
    alea     = scalar_set( tag = 'ALEA', data_type = esp.Integer, size = 4, null = True )
    nnam     = scalar_set( tag = 'NNAM', data_type = esp.LString, size = 4, null = True )
    qsta     = structure_set( 'Qsta', tag = 'QSTA', size = 8, null = True )
    alfi     = scalar_set( tag = 'ALFI', data_type = esp.Integer, size = 4, null = True )
    aliasForcedReference = reference_set( tag = 'ALFR', refers_to = 'REFR', null = True )
    alfe     = scalar_set( tag = 'ALFE', data_type = esp.Float, size = 4, null = True )
    alfd     = scalar_set( tag = 'ALFD', data_type = esp.LString, size = 4, null = True )
    npc_     = reference_set( tag = 'ALCO', refers_to = 'NPC_', null = True )
    alca     = scalar_set( tag = 'ALCA', data_type = esp.Integer, size = 4, null = True )
    alcl     = scalar_set( tag = 'ALCL', data_type = esp.Integer, size = 4, null = True )
    npc_     = reference_set( tag = 'ALUA', refers_to = 'NPC_', null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    containerTotalItemCount = scalar_set( tag = 'COCT', data_type = esp.Integer, size = 4, null = True )
    containerItem = structure_set( 'ContainerItemCnto', tag = 'CNTO', size = 8, null = True )
    formList = reference( tag = 'SPOR', refers_to = 'FLST', null = True )
    formList = reference_set( tag = 'ECOR', refers_to = 'FLST', null = True )
    messagebox = reference_set( tag = 'ALDN', refers_to = 'MESG', null = True )
    spell    = reference_set( tag = 'ALSP', refers_to = 'SPEL', null = True )
    faction  = reference_set( tag = 'ALFC', refers_to = 'FACT', null = True )
    aiPackage = reference_set( tag = 'ALPC', refers_to = 'PACK', null = True )
    voiceType = reference_set( tag = 'VTCK', refers_to = 'VTYP', null = True )
    keyword  = reference_set( tag = 'KNAM', refers_to = 'KYWD', null = True )
    location = reference_set( tag = 'ALFL', refers_to = 'LCTN', null = True )
    aled     = structure_set( 'Aled', tag = 'ALED', null = True )


class Qsta(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )


class ContainerItemCnto(Subrecord):
    item     = field( data_type = esp.Reference )
    quantity = field( data_type = esp.Integer )


class Aled(Subrecord):
    pass


########################
@record_type('QUST')

class QUST(Record):
    scripted_concept = subrecord_group( u'SCRIPTED_CONCEPT' )
    questData = structure( 'QuestData', tag = 'DNAM', size = 12, null = True )
    event    = scalar( tag = 'ENAM', data_type = esp.UnsignedInteger, size = 4, null = True )
    qust_3   = subrecord_group_set( 'QUST_3', null = True )
    qust_4   = subrecord_group_set( 'QUST_4', null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    separator = structure( 'Separator', tag = 'NEXT' )
    qust_7   = subrecord_group_set( 'QUST_7', null = True )
    qust_8   = subrecord_group_set( 'QUST_8', null = True )
    separator = structure( 'SeparatorNext', tag = 'NEXT', null = True )
    anam     = scalar( tag = 'ANAM', data_type = esp.Integer, size = 4, null = True )
    qust_11  = subrecord_group_set( 'QUST_11', null = True )
    qust_12  = subrecord_group_set( 'QUST_12', null = True )


class QuestData(Subrecord):
    flags1   = field( data_type = esp.UnsignedByte )
    flags2   = field( data_type = esp.UnsignedByte )
    priority = field( data_type = esp.UnsignedByte )
    unknown1 = field( data_type = esp.UnsignedByte )
    unknownZero = field( data_type = esp.Integer )
    questType = field( data_type = esp.UnsignedInteger )


class QUST_3(SubrecordGroup):
    globalVariable = reference_set( tag = 'QTGL', refers_to = 'GLOB', null = True )


class QUST_4(SubrecordGroup):
    filter   = scalar( tag = 'FLTR', data_type = esp.String, null = True )


class Separator(Subrecord):
    pass


class QUST_7(SubrecordGroup):
    questStage = structure( 'QuestStage', tag = 'INDX', size = 4 )
    qust_7_1 = subrecord_group_set( 'QUST_7_1', null = True )


class QuestStage(Subrecord):
    stageNumber = field( data_type = esp.UnsignedShort )
    unknown  = field( data_type = esp.UnsignedByte )
    percentComplete = field( data_type = esp.UnsignedByte )


class QUST_7_1(SubrecordGroup):
    questStageData = scalar_set( tag = 'QSDT', data_type = esp.UnsignedByte, size = 1, null = True )
    quest    = reference_set( tag = 'NAM0', refers_to = 'QUST', null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    cnam     = scalar_set( tag = 'CNAM', data_type = esp.LString, null = True )
    schr     = structure_set( 'Schr', tag = 'SCHR', size = 20, null = True )
    sctx     = scalar( tag = 'SCTX', data_type = esp.Blob, null = True )
    quest    = reference_set( tag = 'QNAM', refers_to = 'QUST', null = True )


class Schr(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )


class QUST_8(SubrecordGroup):
    qobj     = scalar_set( tag = 'QOBJ', data_type = esp.Short, size = 2, null = True )
    fnam     = scalar_set( tag = 'FNAM', data_type = esp.LString, size = 4, null = True )
    nnam     = scalar_set( tag = 'NNAM', data_type = esp.LString, size = 4, null = True )
    qust_8_3 = subrecord_group_set( 'QUST_8_3', null = True )


class QUST_8_3(SubrecordGroup):
    qsta     = structure_set( 'QstaQsta', tag = 'QSTA', size = 8, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )


class QstaQsta(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )


class SeparatorNext(Subrecord):
    pass


class QUST_11(SubrecordGroup):
    alst     = scalar_set( tag = 'ALST', data_type = esp.Integer, size = 4, null = True )
    quest_alid = subrecord_group( u'QUEST_ALID', null = True )


class QUST_12(SubrecordGroup):
    qust_12_0 = subrecord_group_set( 'QUST_12_0', null = True )
    qust_12_1 = subrecord_group_set( 'QUST_12_1', null = True )


class QUST_12_0(SubrecordGroup):
    alls     = scalar_set( tag = 'ALLS', data_type = esp.Integer, size = 4, null = True )
    quest_alid = subrecord_group( u'QUEST_ALID', null = True )


class QUST_12_1(SubrecordGroup):
    alst     = scalar_set( tag = 'ALST', data_type = esp.Integer, size = 4, null = True )
    quest_alid = subrecord_group( u'QUEST_ALID', null = True )


########################
@record_type('IDLE')

class IdleAnimation(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    havokFile = scalar( tag = 'DNAM', data_type = esp.String, null = True )
    enam     = scalar( tag = 'ENAM', data_type = esp.String, null = True )
    idleAnims = structure( 'IdleAnims', tag = 'ANAM', size = 8, null = True )
    data     = structure( 'IdleAnimation_5_DataData', tag = 'DATA', size = 6, null = True )


class IdleAnims(Subrecord):
    rootFormid = reference_field( 'IDLE' )
    haltFormid = reference_field( 'IDLE' )


class IdleAnimation_5_DataData(Subrecord):
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Short )


########################
@record_type('PACK')

class PACK(Record):
    editorid = subrecord_group( u'EDITORID' )
    scripts  = subrecord_group( u'SCRIPTS' )
    pkdt     = structure( 'Pkdt', tag = 'PKDT', size = 12, null = True )
    psdt     = structure( 'Psdt', tag = 'PSDT', size = 12, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    cnam     = scalar_set( tag = 'CNAM', data_type = esp.LString, null = True )
    idlf     = scalar( tag = 'IDLF', data_type = esp.UnsignedByte, size = 1, null = True )
    idlc     = scalar( tag = 'IDLC', data_type = esp.UnsignedByte, size = 1, null = True )
    idlt     = scalar( tag = 'IDLT', data_type = esp.Float, size = 4, null = True )
    idleAnim = reference_set( tag = 'IDLA', refers_to = 'IDLE', null = True )
    quest    = reference_set( tag = 'QNAM', refers_to = 'QUST', null = True )
    aiPackageData = structure( 'AiPackageData', tag = 'PKCU', size = 12, null = True )
    pack_12  = subrecord_group_set( 'PACK_12', null = True )
    pack_13  = subrecord_group_set( 'PACK_13', null = True )
    poba     = structure( 'Poba', tag = 'POBA', null = True )
    pack_15  = subrecord_group_set( 'PACK_15', null = True )


class Pkdt(Subrecord):
    unknown  = field( data_type = esp.Short )
    unknown  = field( data_type = esp.Short )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.LString )


class Psdt(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.LString )
    actorValue = reference_field( 'AVIF' )


class AiPackageData(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    packFormid = reference_field( 'PACK' )
    unknown4bytes2 = field( data_type = esp.Integer )


class PACK_12(SubrecordGroup):
    anam     = scalar_set( tag = 'ANAM', data_type = esp.String, null = True )
    dialog   = reference( tag = 'TPIC', refers_to = 'DIAL', null = True )
    cnam     = scalar_set( tag = 'CNAM', data_type = esp.Blob, null = True )
    pldt     = structure_set( 'Pldt', tag = 'PLDT', size = 12, null = True )
    ptda     = structure_set( 'Ptda', tag = 'PTDA', size = 12, null = True )
    pdto     = structure_set( 'Pdto', tag = 'PDTO', size = 8, null = True )
    unam     = scalar_set( tag = 'UNAM', data_type = esp.UnsignedByte, size = 1, null = True )
    xnam     = scalar( tag = 'XNAM', data_type = esp.UnsignedByte, size = 1, null = True )
    citc     = scalar_set( tag = 'CITC', data_type = esp.Integer, size = 4, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    prcb     = structure_set( 'Prcb', tag = 'PRCB', size = 8, null = True )
    pnam     = scalar_set( tag = 'PNAM', data_type = esp.Blob, null = True )
    fnam     = scalar_set( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    pkc2     = scalar_set( tag = 'PKC2', data_type = esp.UnsignedByte, size = 1, null = True )
    pfor     = structure_set( 'Pfor', tag = 'PFOR', size = 12, null = True )
    spell    = structure_set( 'SpellPfo2', tag = 'PFO2', size = 16, null = True )


class Pldt(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    refrFormid = reference_field( 'REFR' )
    unknown4bytes2 = field( data_type = esp.LString )


class Ptda(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )
    unknown4bytes3 = field( data_type = esp.Integer )


class Pdto(Subrecord):
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Short )
    unknown3 = field( data_type = esp.Short )


class Prcb(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )


class Pfor(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )
    unknown4bytes3 = field( data_type = esp.Integer )


class SpellPfo2(Subrecord):
    name     = field( data_type = esp.LString )
    unknown1 = field( data_type = esp.Integer )
    spell    = reference_field( 'SPEL' )
    unknown2 = field( data_type = esp.Integer )


class PACK_13(SubrecordGroup):
    unam     = scalar_set( tag = 'UNAM', data_type = esp.UnsignedByte, size = 1, null = True )
    bnam     = scalar_set( tag = 'BNAM', data_type = esp.String, null = True )
    pnam     = scalar_set( tag = 'PNAM', data_type = esp.Blob, null = True )


class Poba(Subrecord):
    pass


class PACK_15(SubrecordGroup):
    idleAnim = reference_set( tag = 'INAM', refers_to = 'IDLE', null = True )
    schr     = structure_set( 'SchrSchr', tag = 'SCHR', size = 20, null = True )
    tnam     = scalar_set( tag = 'TNAM', data_type = esp.Integer, size = 4, null = True )
    scda     = structure( 'Scda', tag = 'SCDA', size = 17, null = True )
    sctx     = scalar_set( tag = 'SCTX', data_type = esp.Blob, null = True )
    quest    = reference_set( tag = 'QNAM', refers_to = 'QUST', null = True )
    pdto     = structure_set( 'PdtoPdto', tag = 'PDTO', size = 8, null = True )
    poea     = structure( 'Poea', tag = 'POEA', null = True )
    poca     = structure( 'Poca', tag = 'POCA', null = True )


class SchrSchr(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )


class Scda(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Short )
    unknown1 = field( data_type = esp.Short )
    unknown2 = field( data_type = esp.LString )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.UnsignedByte )


class PdtoPdto(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Short )
    unknown1 = field( data_type = esp.Short )


class Poea(Subrecord):
    pass


class Poca(Subrecord):
    pass


########################
@record_type('CSTY')

class CSTY(Record):
    editorid = subrecord_group( u'EDITORID' )
    csgd     = scalar( tag = 'CSGD', data_type = esp.Blob, null = True )
    csmd     = structure( 'Csmd', tag = 'CSMD', size = 8, null = True )
    csme     = scalar( tag = 'CSME', data_type = esp.Blob, null = True )
    cscr     = scalar( tag = 'CSCR', data_type = esp.Blob, null = True )
    cslr     = scalar( tag = 'CSLR', data_type = esp.Float, size = 4, null = True )
    csfl     = scalar( tag = 'CSFL', data_type = esp.Blob, null = True )
    data     = scalar( tag = 'DATA', data_type = esp.Integer, size = 4, null = True )


class Csmd(Subrecord):
    unknownFloat1 = field( data_type = esp.Float )
    unknownFlaot2 = field( data_type = esp.Float )


########################
@record_type('LSCR')

class LoadScreen(Record):
    editorid = subrecord_group( u'EDITORID' )
    displayedText = scalar( tag = 'DESC', data_type = esp.LString )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    displayModel = reference( tag = 'NNAM', refers_to = 'STAT' )
    initialScale = scalar( tag = 'SNAM', data_type = esp.Float, size = 4 )
    initialRotation = structure( 'InitialRotation', tag = 'RNAM', size = 6 )
    rotationOffsetConstraints = structure( 'RotationOffsetConstraints', tag = 'ONAM' )
    initialTranslationOffset = structure( 'InitialTranslationOffset', tag = 'XNAM', size = 12 )
    cameraPath = scalar( tag = 'MOD2', data_type = esp.String, null = True )


class InitialRotation(Subrecord):
    rotateX  = field( data_type = esp.Short )
    rotateY  = field( data_type = esp.Short )
    rotateZ  = field( data_type = esp.Short )


class RotationOffsetConstraints(Subrecord):
    rotationMin = field( data_type = esp.Short )
    rotationMax = field( data_type = esp.Short )


class InitialTranslationOffset(Subrecord):
    translateX = field( data_type = esp.Float )
    translateY = field( data_type = esp.Float )
    translateZ = field( data_type = esp.Float )


########################
@record_type('LVSP')

class LeveledSpell(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    leveled  = subrecord_group( u'LEVELED' )


########################
@record_type('ANIO')

class AnimatedObject(Record):
    editorid = subrecord_group( u'EDITORID' )
    base_model = subrecord_group( u'BASE_MODEL' )
    bnam     = scalar( tag = 'BNAM', data_type = esp.String, null = True )


########################
@record_type('WATR')

class WATR(Record):
    concept  = subrecord_group( u'CONCEPT' )
    nnam     = scalar_set( tag = 'NNAM', data_type = esp.String, null = True )
    anam     = scalar( tag = 'ANAM', data_type = esp.UnsignedByte, size = 1, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.String, null = True )
    materialType = reference( tag = 'TNAM', refers_to = 'MATT', null = True )
    mnam     = scalar( tag = 'MNAM', data_type = esp.String, null = True )
    sound    = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    data     = scalar( tag = 'DATA', data_type = esp.Short, size = 2, null = True )
    dnam     = structure( 'WATR_8_DnamDnam', tag = 'DNAM', size = 228, null = True )
    gnam     = structure( 'GnamGnam', tag = 'GNAM', size = 12, null = True )
    nam0     = structure( 'WATR_10_Nam0Nam0', tag = 'NAM0', size = 12, null = True )
    nam1     = structure( 'WATR_11_Nam1Nam1', tag = 'NAM1', size = 12, null = True )


class WATR_8_DnamDnam(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Float )
    unknown9 = field( data_type = esp.Float )
    unknown10 = field( data_type = esp.Integer )
    unknown11 = field( data_type = esp.Integer )
    unknown12 = field( data_type = esp.Integer )
    unknown13 = field( data_type = esp.Integer )
    unknown14 = field( data_type = esp.Float )
    unknown15 = field( data_type = esp.Float )
    unknown16 = field( data_type = esp.Float )
    unknown17 = field( data_type = esp.Float )
    unknown18 = field( data_type = esp.Float )
    unknown19 = field( data_type = esp.Float )
    unknown20 = field( data_type = esp.Float )
    unknown21 = field( data_type = esp.Float )
    unknown22 = field( data_type = esp.Float )
    unknown23 = field( data_type = esp.Float )
    unknown24 = field( data_type = esp.Float )
    unknown25 = field( data_type = esp.Float )
    unknown26 = field( data_type = esp.Float )
    unknown27 = field( data_type = esp.Float )
    unknown28 = field( data_type = esp.Float )
    unknown29 = field( data_type = esp.Float )
    unknown30 = field( data_type = esp.Float )
    unknown31 = field( data_type = esp.Float )
    unknown32 = field( data_type = esp.Float )
    unknown33 = field( data_type = esp.Float )
    unknown34 = field( data_type = esp.Float )
    unknown35 = field( data_type = esp.Float )
    unknown36 = field( data_type = esp.Float )
    unknown37 = field( data_type = esp.Float )
    unknown38 = field( data_type = esp.Float )
    unknown39 = field( data_type = esp.Float )
    unknown40 = field( data_type = esp.Float )
    unknown41 = field( data_type = esp.Float )
    unknown42 = field( data_type = esp.Float )
    unknown43 = field( data_type = esp.Float )
    unknown44 = field( data_type = esp.Float )
    unknown45 = field( data_type = esp.Float )
    unknown46 = field( data_type = esp.Float )
    unknown47 = field( data_type = esp.Float )
    unknown48 = field( data_type = esp.Float )
    unknown49 = field( data_type = esp.Float )
    unknown50 = field( data_type = esp.Float )
    unknown51 = field( data_type = esp.Float )
    unknown52 = field( data_type = esp.Float )
    unknown53 = field( data_type = esp.Float )
    unknown54 = field( data_type = esp.Float )
    unknown55 = field( data_type = esp.Float )
    unknown56 = field( data_type = esp.Float )


class GnamGnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


class WATR_10_Nam0Nam0(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Integer )


class WATR_11_Nam1Nam1(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


########################
@record_type('EFSH')

class EffectShader(Record):
    editorid = subrecord_group( u'EDITORID' )
    icon     = scalar( tag = 'ICON', data_type = esp.String, null = True )
    ico2     = scalar( tag = 'ICO2', data_type = esp.String, null = True )
    nam7     = scalar( tag = 'NAM7', data_type = esp.String, null = True )
    nam8     = scalar( tag = 'NAM8', data_type = esp.String, null = True )
    nam9     = scalar( tag = 'NAM9', data_type = esp.String, null = True )
    data     = scalar( tag = 'DATA', data_type = esp.Blob, null = True )


########################
@record_type('EXPL')

class Explosion(Record):
    object   = subrecord_group( u'OBJECT' )
    base_model = subrecord_group( u'BASE_MODEL' )
    enchantment = reference( tag = 'EITM', refers_to = 'ENCH', null = True )
    imagespace = reference( tag = 'MNAM', refers_to = 'IMAD', null = True )
    explosionLight = reference_set( tag = 'DATA', refers_to = 'LIGH', null = True )


########################
@record_type('DEBR')

class Debris(Record):
    editorid = subrecord_group( u'EDITORID' )
    debris_1 = subrecord_group_set( 'Debris_1', null = True )


class Debris_1(SubrecordGroup):
    data     = scalar_set( tag = 'DATA', data_type = esp.Blob, null = True )
    modelData = structure_set( 'Debris_1_1_ModelDataModt', tag = 'MODT', size = 72, null = True )


class Debris_1_1_ModelDataModt(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )
    unknown9 = field( data_type = esp.Integer )
    unknown10 = field( data_type = esp.Integer )
    unknown11 = field( data_type = esp.Float )
    unknown12 = field( data_type = esp.Integer )
    unknown13 = field( data_type = esp.Integer )
    unknown14 = field( data_type = esp.Integer )
    unknown15 = field( data_type = esp.Integer )
    unknown16 = field( data_type = esp.Integer )
    unknown17 = field( data_type = esp.Integer )


########################
@record_type('IMGS')

class ImageSpace(Record):
    editorid = subrecord_group( u'EDITORID' )
    enam     = structure( 'ImageSpace_1_EnamEnam', tag = 'ENAM', size = 56, null = True )
    hnam     = structure( 'Hnam', tag = 'HNAM', size = 36, null = True )
    cinematic = structure( 'Cinematic', tag = 'CNAM', size = 12, null = True )
    tint     = structure( 'TintTnam', tag = 'TNAM', size = 16, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Blob, null = True )


class ImageSpace_1_EnamEnam(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Float )
    unknown8 = field( data_type = esp.Float )
    unknown9 = field( data_type = esp.Float )
    unknown10 = field( data_type = esp.Integer )
    unknown11 = field( data_type = esp.Integer )
    unknown12 = field( data_type = esp.Integer )
    unknown13 = field( data_type = esp.Integer )


class Hnam(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Float )
    unknown8 = field( data_type = esp.Float )


class Cinematic(Subrecord):
    saturation = field( data_type = esp.Float )
    brightness = field( data_type = esp.Float )
    contrast = field( data_type = esp.Float )


class TintTnam(Subrecord):
    rwxred   = field( data_type = esp.Float )
    rwxgreen = field( data_type = esp.Float )
    rwxblue  = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


########################
@record_type('IMAD')

class IMAD(Record):
    editorid = subrecord_group( u'EDITORID' )
    dnam     = structure( 'IMAD_1_DnamDnam', tag = 'DNAM', size = 244, null = True )
    bnam     = scalar( tag = 'BNAM', data_type = esp.Blob, null = True )
    vnam     = scalar( tag = 'VNAM', data_type = esp.Blob, null = True )
    tnam     = scalar( tag = 'TNAM', data_type = esp.Blob, null = True )
    nam3     = scalar( tag = 'NAM3', data_type = esp.Blob, null = True )
    rnam     = scalar( tag = 'RNAM', data_type = esp.Blob, null = True )
    snam     = scalar( tag = 'SNAM', data_type = esp.Blob, null = True )
    unam     = scalar( tag = 'UNAM', data_type = esp.Blob, null = True )
    nam1     = scalar( tag = 'NAM1', data_type = esp.Blob, null = True )
    nam2     = scalar( tag = 'NAM2', data_type = esp.Blob, null = True )
    wnam     = scalar( tag = 'WNAM', data_type = esp.Blob, null = True )
    xnam     = scalar( tag = 'XNAM', data_type = esp.Blob, null = True )
    ynam     = scalar( tag = 'YNAM', data_type = esp.Blob, null = True )
    znam     = scalar( tag = 'ZNAM', data_type = esp.Blob, null = True )
    nam4     = scalar( tag = 'NAM4', data_type = esp.Blob, null = True )
    x0iad    = scalar( tag = '&#x0;IAD', data_type = esp.Blob, null = True )
    iad      = scalar( tag = '@IAD', data_type = esp.Blob, null = True )
    x1iad    = scalar( tag = '&#x1;IAD', data_type = esp.Blob, null = True )
    aiad     = scalar( tag = 'AIAD', data_type = esp.Blob, null = True )
    x2iad    = scalar( tag = '&#x2;IAD', data_type = esp.Blob, null = True )
    biad     = scalar( tag = 'BIAD', data_type = esp.Blob, null = True )
    x3iad    = scalar( tag = '&#x3;IAD', data_type = esp.Blob, null = True )
    ciad     = scalar( tag = 'CIAD', data_type = esp.Blob, null = True )
    x4iad    = scalar( tag = '&#x4;IAD', data_type = esp.Blob, null = True )
    diad     = scalar( tag = 'DIAD', data_type = esp.Blob, null = True )
    x5iad    = scalar( tag = '&#x5;IAD', data_type = esp.Blob, null = True )
    eiad     = scalar( tag = 'EIAD', data_type = esp.Blob, null = True )
    x6iad    = scalar( tag = '&#x6;IAD', data_type = esp.Blob, null = True )
    fiad     = scalar( tag = 'FIAD', data_type = esp.Blob, null = True )
    x7iad    = scalar( tag = '&#x7;IAD', data_type = esp.Blob, null = True )
    giad     = scalar( tag = 'GIAD', data_type = esp.Blob, null = True )
    x8iad    = structure( 'X8iad', tag = '&#x8;IAD', size = 16, null = True )
    hiad     = structure( 'Hiad', tag = 'HIAD', size = 16, null = True )
    x9iad    = structure( 'X9iad', tag = '&#x9;IAD', size = 16, null = True )
    iiad     = structure( 'Iiad', tag = 'IIAD', size = 16, null = True )
    xaiad    = structure( 'Xaiad', tag = '&#xA;IAD', size = 16, null = True )
    jiad     = structure( 'Jiad', tag = 'JIAD', size = 16, null = True )
    xbiad    = structure( 'Xbiad', tag = '&#xB;IAD', size = 16, null = True )
    kiad     = structure( 'Kiad', tag = 'KIAD', size = 16, null = True )
    xciad    = structure( 'Xciad', tag = '&#xC;IAD', size = 16, null = True )
    liad     = structure( 'Liad', tag = 'LIAD', size = 16, null = True )
    xdiad    = structure( 'Xdiad', tag = '&#xD;IAD', size = 16, null = True )
    miad     = structure( 'Miad', tag = 'MIAD', size = 16, null = True )
    xeiad    = structure( 'Xeiad', tag = '&#xE;IAD', size = 16, null = True )
    niad     = structure( 'Niad', tag = 'NIAD', size = 16, null = True )
    xfiad    = structure( 'Xfiad', tag = '&#xF;IAD', size = 16, null = True )
    oiad     = structure( 'Oiad', tag = 'OIAD', size = 16, null = True )
    x10iad   = structure( 'X10iad', tag = '&#x10;IAD', size = 16, null = True )
    piad     = structure( 'Piad', tag = 'PIAD', size = 16, null = True )
    x11iad   = scalar( tag = '&#x11;IAD', data_type = esp.Blob, null = True )
    qiad     = scalar( tag = 'QIAD', data_type = esp.Blob, null = True )
    x12iad   = scalar( tag = '&#x12;IAD', data_type = esp.Blob, null = True )
    riad     = scalar( tag = 'RIAD', data_type = esp.Blob, null = True )
    x13iad   = scalar( tag = '&#x13;IAD', data_type = esp.Blob, null = True )
    siad     = scalar( tag = 'SIAD', data_type = esp.Blob, null = True )
    x14iad   = structure( 'X14iad', tag = '&#x14;IAD', size = 16, null = True )
    tiad     = structure( 'Tiad', tag = 'TIAD', size = 16, null = True )


class IMAD_1_DnamDnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )
    unknown9 = field( data_type = esp.Integer )
    unknown10 = field( data_type = esp.Integer )
    unknown11 = field( data_type = esp.Integer )
    unknown12 = field( data_type = esp.Integer )
    unknown13 = field( data_type = esp.Integer )
    unknown14 = field( data_type = esp.Integer )
    unknown15 = field( data_type = esp.Integer )
    unknown16 = field( data_type = esp.Integer )
    unknown17 = field( data_type = esp.Integer )
    unknown18 = field( data_type = esp.Integer )
    unknown19 = field( data_type = esp.Integer )
    unknown20 = field( data_type = esp.Integer )
    unknown21 = field( data_type = esp.Integer )
    unknown22 = field( data_type = esp.Integer )
    unknown23 = field( data_type = esp.Integer )
    unknown24 = field( data_type = esp.Integer )
    unknown25 = field( data_type = esp.Integer )
    unknown26 = field( data_type = esp.Integer )
    unknown27 = field( data_type = esp.Integer )
    unknown28 = field( data_type = esp.Integer )
    unknown29 = field( data_type = esp.Integer )
    unknown30 = field( data_type = esp.Integer )
    unknown31 = field( data_type = esp.Integer )
    unknown32 = field( data_type = esp.Integer )
    unknown33 = field( data_type = esp.Integer )
    unknown34 = field( data_type = esp.Integer )
    unknown35 = field( data_type = esp.Integer )
    unknown36 = field( data_type = esp.Integer )
    unknown37 = field( data_type = esp.Integer )
    unknown38 = field( data_type = esp.Integer )
    unknown39 = field( data_type = esp.Integer )
    unknown40 = field( data_type = esp.Integer )
    unknown41 = field( data_type = esp.Integer )
    unknown42 = field( data_type = esp.Integer )
    unknown43 = field( data_type = esp.Integer )
    unknown44 = field( data_type = esp.Integer )
    unknown45 = field( data_type = esp.Integer )
    unknown46 = field( data_type = esp.Integer )
    unknown47 = field( data_type = esp.Integer )
    unknown48 = field( data_type = esp.Integer )
    unknown49 = field( data_type = esp.Integer )
    unknown50 = field( data_type = esp.Integer )
    unknown51 = field( data_type = esp.Float )
    unknown52 = field( data_type = esp.Float )
    unknown53 = field( data_type = esp.Integer )
    unknown54 = field( data_type = esp.Integer )
    unknown55 = field( data_type = esp.Integer )
    unknown56 = field( data_type = esp.LString )
    unknown57 = field( data_type = esp.Integer )
    unknown58 = field( data_type = esp.Integer )
    unknown59 = field( data_type = esp.Integer )
    unknown60 = field( data_type = esp.Integer )


class X8iad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Hiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class X9iad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Iiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class Xaiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Jiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class Xbiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Kiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class Xciad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Liad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class Xdiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Miad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class Xeiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Niad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class Xfiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Oiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class X10iad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Piad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


class X14iad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class Tiad(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )


########################
@record_type('FLST')

class FLST(Record):
    editorid = subrecord_group( u'EDITORID' )
    listItem = scalar_set( tag = 'LNAM', data_type = esp.Reference, size = 4, null = True )


########################
@record_type('PERK')

class PERK(Record):
    scripted_concept = subrecord_group( u'SCRIPTED_CONCEPT' )
    perkDescription = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    perkData = structure( 'PerkData', tag = 'DATA', size = 5, null = True )
    perk     = reference( tag = 'NNAM', refers_to = 'PERK', null = True )
    perk_5   = subrecord_group_set( 'PERK_5', null = True )


class PerkData(Subrecord):
    istrait  = field( data_type = esp.UnsignedByte )
    level    = field( data_type = esp.UnsignedByte )
    numranks = field( data_type = esp.UnsignedByte )
    isplayable = field( data_type = esp.UnsignedByte )
    ishidden = field( data_type = esp.UnsignedByte )


class PERK_5(SubrecordGroup):
    rankEffectHeader = structure_set( 'RankEffectHeader', tag = 'PRKE', size = 3, null = True )
    perkEffectData = structure( 'PerkEffectData', tag = 'DATA', size = 8, null = True )
    perkEffect = reference( tag = 'DATA', refers_to = 'SPEL', null = True )
    perkEffectData = structure( 'PerkEffectDataData', tag = 'DATA', size = 3, null = True )
    perk_5_4 = subrecord_group_set( 'PERK_5_4', null = True )
    extraDataType = scalar_set( tag = 'EPFT', data_type = esp.UnsignedByte, size = 1, null = True )
    scriptData2 = scalar_set( tag = 'EPF2', data_type = esp.LString, size = 4, null = True )
    scriptData3Always0000 = scalar_set( tag = 'EPF3', data_type = esp.Integer, size = 4, null = True )
    floatValue = scalar_set( tag = 'EPFD', data_type = esp.Float, size = 4, null = True )
    unknown8ByteStruct = scalar_set( tag = 'EPFD', data_type = esp.Blob, size = 8, null = True )
    formid   = scalar_set( tag = 'EPFD', data_type = esp.Reference, size = 4, null = True )
    formid   = scalar_set( tag = 'EPFD', data_type = esp.Reference, size = 4, null = True )
    spell    = reference_set( tag = 'EPFD', refers_to = 'SPEL', null = True )
    zstring  = scalar_set( tag = 'EPFD', data_type = esp.String, null = True )
    lstring  = scalar_set( tag = 'EPFD', data_type = esp.LString, null = True )
    rankEffectFooter = structure_set( 'RankEffectFooter', tag = 'PRKF', null = True )


class RankEffectHeader(Subrecord):
    effectType = field( data_type = esp.UnsignedByte )
    rankIndex = field( data_type = esp.UnsignedByte )
    always0  = field( data_type = esp.UnsignedByte )


class PerkEffectData(Subrecord):
    qustFormid = reference_field( 'QUST' )
    stage    = field( data_type = esp.UnsignedByte )
    unused   = field( data_type = esp.UnsignedByte )
    unused   = field( data_type = esp.UnsignedByte )
    unused   = field( data_type = esp.UnsignedByte )


class PerkEffectDataData(Subrecord):
    effecttype = field( data_type = esp.UnsignedByte )
    functiontype = field( data_type = esp.UnsignedByte )
    condtypecount = field( data_type = esp.UnsignedByte )


class PERK_5_4(SubrecordGroup):
    conditionalInfo = scalar_set( tag = 'PRKC', data_type = esp.UnsignedByte, size = 1, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )


class RankEffectFooter(Subrecord):
    pass


########################
@record_type('BPTD')

class BPTD(Record):
    editorid = subrecord_group( u'EDITORID' )
    base_model = subrecord_group( u'BASE_MODEL' )
    bptd_2   = subrecord_group_set( 'BPTD_2', null = True )


class BPTD_2(SubrecordGroup):
    bodyPartName = scalar_set( tag = 'BPTN', data_type = esp.LString, size = 4, null = True )
    bodyPartNodeName = scalar_set( tag = 'BPNN', data_type = esp.String, null = True )
    bodyPartNodeTitle = scalar_set( tag = 'BPNT', data_type = esp.String, null = True )
    bodyPartNodeInfo = scalar_set( tag = 'BPNI', data_type = esp.String, null = True )
    bodyPartNodeData = structure_set( 'BodyPartNodeData', tag = 'BPND', size = 84, null = True )
    nam1     = scalar_set( tag = 'NAM1', data_type = esp.String, null = True )
    nam4     = scalar_set( tag = 'NAM4', data_type = esp.String, null = True )
    nam5     = structure_set( 'Nam5', tag = 'NAM5', null = True )


class BodyPartNodeData(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )
    unknown9 = field( data_type = esp.Integer )
    unknown10 = field( data_type = esp.Float )
    unknown11 = field( data_type = esp.Integer )
    unknown12 = field( data_type = esp.Integer )
    unknown13 = field( data_type = esp.Integer )
    unknown14 = field( data_type = esp.Integer )
    unknown15 = field( data_type = esp.Integer )
    unknown16 = field( data_type = esp.Integer )
    ipdsFormid1 = reference_field( 'IPDS' )
    ipdsFormid2 = reference_field( 'IPDS' )
    unknown19 = field( data_type = esp.Integer )
    unknown20 = field( data_type = esp.Float )


class Nam5(Subrecord):
    pass


########################
@record_type('ADDN')

class AddonNode(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    uniqueId = scalar( tag = 'DATA', data_type = esp.Integer, size = 4, null = True )
    type     = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )


########################
@record_type('AVIF')

class ActorValueInfo(Record):
    concept  = subrecord_group( u'CONCEPT' )
    description = scalar( tag = 'DESC', data_type = esp.LString )
    abbreviation = scalar( tag = 'ANAM', data_type = esp.String, null = True )
    data     = scalar( tag = 'CNAM', data_type = esp.UnsignedInteger, null = True )
    useModifiers = structure( 'UseModifiers', tag = 'AVSK', null = True )
    actorvalueinfo_5 = subrecord_group_set( 'ActorValueInfo_5', null = True )


class UseModifiers(Subrecord):
    useMultiplier = field( data_type = esp.Float )
    useOffset = field( data_type = esp.Float )
    improveMultiplier = field( data_type = esp.Float )
    improveOffset = field( data_type = esp.Float )


class ActorValueInfo_5(SubrecordGroup):
    perk     = reference( tag = 'PNAM', refers_to = 'PERK' )
    flag     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4 )
    perkGridX = scalar( tag = 'XNAM', data_type = esp.Integer, size = 4 )
    perkGridY = scalar( tag = 'YNAM', data_type = esp.Integer, size = 4 )
    horizontalPosition = scalar( tag = 'HNAM', data_type = esp.Float, size = 4 )
    verticalPosition = scalar( tag = 'VNAM', data_type = esp.Float, size = 4 )
    skill    = reference( tag = 'SNAM', refers_to = 'AVIF' )
    unlocks  = scalar_set( tag = 'CNAM', data_type = esp.UnsignedInteger, size = 4, null = True )
    indexNumber = scalar_set( tag = 'INAM', data_type = esp.UnsignedInteger, size = 4, null = True )


########################
@record_type('CAMS')

class CameraShot(Record):
    editorid = subrecord_group( u'EDITORID' )
    base_model = subrecord_group( u'BASE_MODEL' )
    data     = structure( 'CameraShot_2_DataData', tag = 'DATA', size = 40, null = True )
    imagespace = reference( tag = 'MNAM', refers_to = 'IMAD', null = True )


class CameraShot_2_DataData(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Float )
    unknown8 = field( data_type = esp.Float )
    unknown9 = field( data_type = esp.Float )


########################
@record_type('CPTH')

class CPTH(Record):
    editorid = subrecord_group( u'EDITORID' )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    cameraPath = structure( 'CameraPathAnam', tag = 'ANAM', size = 8, null = True )
    data     = scalar( tag = 'DATA', data_type = esp.String, null = True )
    cameraShot = reference_set( tag = 'SNAM', refers_to = 'CAMS', null = True )


class CameraPathAnam(Subrecord):
    formid1  = reference_field( 'CPTH' )
    formid2  = reference_field( 'CPTH' )


########################
@record_type('VTYP')

class VTYP(Record):
    editorid = subrecord_group( u'EDITORID' )
    voiceTypeData = scalar( tag = 'DNAM', data_type = esp.UnsignedByte, size = 1, null = True )


########################
@record_type('MATT')

class MATT(Record):
    editorid = subrecord_group( u'EDITORID' )
    materialName = scalar( tag = 'MNAM', data_type = esp.String )
    havokImpactDataSet = reference( tag = 'HNAM', refers_to = 'IPDS', null = True )
    parentMaterial = reference( tag = 'PNAM', refers_to = 'MATT', null = True )
    havokDisplayColor = structure( 'HavokDisplayColor', tag = 'CNAM' )
    bouyancy = scalar( tag = 'BNAM', data_type = esp.Float )
    flags    = scalar( tag = 'FNAM', data_type = esp.UnsignedInteger, null = True )


class HavokDisplayColor(Subrecord):
    rwxred   = field( data_type = esp.Float )
    rwxgreen = field( data_type = esp.Float )
    rwxblue  = field( data_type = esp.Float )


########################
@record_type('IPCT')

class ImpactData(Record):
    editorid = subrecord_group( u'EDITORID' )
    base_model = subrecord_group( u'BASE_MODEL' )
    impactData = structure( 'ImpactDataData', tag = 'DATA', size = 24, null = True )
    data     = structure( 'DataDodt', tag = 'DODT', size = 36, null = True )
    decalType = reference( tag = 'DNAM', refers_to = 'TXST', null = True )
    textureSet = reference( tag = 'ENAM', refers_to = 'TXST', null = True )
    soundType = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    sound    = reference( tag = 'NAM1', refers_to = 'SNDR', null = True )
    hazard   = reference( tag = 'NAM2', refers_to = 'HAZD', null = True )


class ImpactDataData(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.LString )


class DataDodt(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )


########################
@record_type('IPDS')

class IPDS(Record):
    editorid = subrecord_group( u'EDITORID' )
    impactMaterialAndData = structure_set( 'ImpactMaterialAndData', tag = 'PNAM', size = 8, null = True )


class ImpactMaterialAndData(Subrecord):
    mattFormid = reference_field( 'MATT' )
    ipctFormid = reference_field( 'IPCT' )


########################
@record_type('ARMA')

class Armature(Record):
    editorid = subrecord_group( u'EDITORID' )
    body_template = subrecord_group( u'BODY_TEMPLATE', null = True )
    rnam     = scalar( tag = 'RNAM', data_type = esp.Integer, size = 4, null = True )
    type     = structure( 'TypeDnam', tag = 'DNAM', size = 12, null = True )
    model2   = scalar( tag = 'MOD2', data_type = esp.String, null = True )
    modelData2 = scalar( tag = 'MO2T', data_type = esp.Blob, null = True )
    mo2s     = scalar( tag = 'MO2S', data_type = esp.Blob, null = True )
    model3   = scalar( tag = 'MOD3', data_type = esp.String, null = True )
    modelData3 = scalar( tag = 'MO3T', data_type = esp.Blob, null = True )
    mo3s     = scalar( tag = 'MO3S', data_type = esp.Blob, null = True )
    model4   = scalar( tag = 'MOD4', data_type = esp.String, null = True )
    modelData4 = structure( 'ModelData4Mo4t', tag = 'MO4T', size = 12, null = True )
    modelData4s = scalar( tag = 'MO4S', data_type = esp.Blob, null = True )
    model5   = scalar( tag = 'MOD5', data_type = esp.String, null = True )
    modelData5 = structure( 'ModelData5', tag = 'MO5T', size = 12, null = True )
    baseMaleTexture = reference( tag = 'NAM0', refers_to = 'TXST', null = True )
    baseFemaleTexture = reference( tag = 'NAM1', refers_to = 'TXST', null = True )
    baseMale1stTexture = reference( tag = 'NAM2', refers_to = 'FLST', null = True )
    baseFemale1stTexture = reference( tag = 'NAM3', refers_to = 'FLST', null = True )
    includedRace = reference_set( tag = 'MODL', refers_to = 'RACE', null = True )
    footstepSound = reference( tag = 'SNDD', refers_to = 'FSTS', null = True )


class TypeDnam(Subrecord):
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )
    unknown4bytes3 = field( data_type = esp.Float )


class ModelData4Mo4t(Subrecord):
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


class ModelData5(Subrecord):
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


########################
@record_type('ECZN')

class EncounterZone(Record):
    editorid = subrecord_group( u'EDITORID' )
    ecznData = structure( 'EcznData', tag = 'DATA', null = True )


class EcznData(Subrecord):
    factFormid = reference_field( 'FACT' )
    lctnFormid = reference_field( 'LCTN' )
    unknown  = field( data_type = esp.UnsignedByte )
    zoneLevel = field( data_type = esp.UnsignedByte )
    unknown  = field( data_type = esp.UnsignedByte )
    unknown  = field( data_type = esp.UnsignedByte )


########################
@record_type('LCTN')

class LocationData(Record):
    editorid = subrecord_group( u'EDITORID' )
    uniqueRefs = reference_set( tag = 'LCPR', refers_to = 'ACHR', null = True )
    actorNpc_ = reference_set( tag = 'LCUN', refers_to = 'NPC_', null = True )
    staticRefs = reference_set( tag = 'LCSR', refers_to = 'LCRT', null = True )
    encounter = reference_set( tag = 'LCEC', refers_to = 'WRLD', null = True )
    ref      = reference_set( tag = 'LCID', refers_to = 'REFR', null = True )
    actorEnablePoints = reference_set( tag = 'LCEP', refers_to = 'ACHR', null = True )
    fullname = subrecord_group( u'FULLNAME' )
    keywords = subrecord_group( u'KEYWORDS', null = True )
    parentLocation = reference( tag = 'PNAM', refers_to = 'LCTN', null = True )
    faction  = reference( tag = 'FNAM', refers_to = 'FACT', null = True )
    music    = reference( tag = 'NAM1', refers_to = 'MUSC', null = True )
    marker   = reference( tag = 'MNAM', refers_to = 'REFR', null = True )
    rnam     = scalar( tag = 'RNAM', data_type = esp.Float, size = 4, null = True )
    ref      = reference( tag = 'NAM0', refers_to = 'REFR', null = True )
    color    = scalar( tag = 'CNAM', data_type = esp.Color, null = True )


########################
@record_type('MESG')

class Message(Record):
    editorid = subrecord_group( u'EDITORID' )
    ingameMessageDescription = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    fullname = subrecord_group( u'FULLNAME' )
    inam     = scalar( tag = 'INAM', data_type = esp.Integer, size = 4, null = True )
    quest    = reference( tag = 'QNAM', refers_to = 'QUST', null = True )
    descriptionType = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )
    messageType = scalar( tag = 'TNAM', data_type = esp.Integer, size = 4, null = True )
    message_7 = subrecord_group_set( 'Message_7', null = True )


class Message_7(SubrecordGroup):
    buttonText = scalar_set( tag = 'ITXT', data_type = esp.LString, size = 4, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )


########################
@record_type('DOBJ')

class DynamicObject(Record):
    dnam     = scalar( tag = 'DNAM', data_type = esp.Blob, null = True )


########################
@record_type('LGTM')

class LGTM(Record):
    editorid = subrecord_group( u'EDITORID' )
    data     = scalar( tag = 'DATA', data_type = esp.Blob, null = True )
    dalc     = scalar( tag = 'DALC', data_type = esp.Blob, null = True )


########################
@record_type('MUSC')

class MusicFile(Record):
    editorid = subrecord_group( u'EDITORID' )
    musicFilePath = scalar( tag = 'FNAM', data_type = esp.LString, size = 4, null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    wnam     = scalar( tag = 'WNAM', data_type = esp.Float, size = 4, null = True )
    musicTemplate = reference_set( tag = 'TNAM', refers_to = 'MUST', null = True )


########################
@record_type('FSTP')

class Footstep(Record):
    editorid = subrecord_group( u'EDITORID' )
    impactData = reference( tag = 'DATA', refers_to = 'IPDS', null = True )
    actionName = scalar( tag = 'ANAM', data_type = esp.String, null = True )


########################
@record_type('FSTS')

class FootstepSet(Record):
    editorid = subrecord_group( u'EDITORID' )
    setCount = structure( 'SetCount', tag = 'XCNT', size = 20, null = True )
    footstepSets = reference_set( tag = 'DATA', refers_to = 'FSTP', null = True )


class SetCount(Subrecord):
    walkForwardCount = field( data_type = esp.Integer )
    runForwardCount = field( data_type = esp.Integer )
    walkForwardAlternateCount = field( data_type = esp.Integer )
    runForwardAlternateCount = field( data_type = esp.Integer )
    walkForwardAlternate2Count = field( data_type = esp.Integer )


########################
@record_type('SMBN')

class StoryManagerBranchNode(Record):
    editorid = subrecord_group( u'EDITORID' )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    snam     = scalar( tag = 'SNAM', data_type = esp.Integer, size = 4, null = True )
    citc     = scalar( tag = 'CITC', data_type = esp.Integer, size = 4, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )
    xnam     = scalar( tag = 'XNAM', data_type = esp.Integer, size = 4, null = True )


########################
@record_type('SMQN')

class StoryManagerQuestNode(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    storyManagerQuestNode = reference( tag = 'SNAM', refers_to = 'SMQN', null = True )
    citc     = scalar( tag = 'CITC', data_type = esp.Integer, size = 4, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )
    xnam     = scalar( tag = 'XNAM', data_type = esp.Integer, size = 4, null = True )
    mnam     = scalar( tag = 'MNAM', data_type = esp.Integer, size = 4, null = True )
    qnam     = scalar( tag = 'QNAM', data_type = esp.Integer, size = 4, null = True )
    storymanagerquestnode_9 = subrecord_group_set( 'StoryManagerQuestNode_9', null = True )


class StoryManagerQuestNode_9(SubrecordGroup):
    quest    = reference_set( tag = 'NNAM', refers_to = 'QUST', null = True )
    fnam     = scalar_set( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    rnam     = scalar_set( tag = 'RNAM', data_type = esp.Float, size = 4, null = True )


########################
@record_type('SMEN')

class StoryManagerEventNode(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    storyManagerEventNode = reference( tag = 'SNAM', refers_to = 'SMEN', null = True )
    citc     = scalar( tag = 'CITC', data_type = esp.Integer, size = 4, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )
    xnam     = scalar( tag = 'XNAM', data_type = esp.Integer, size = 4, null = True )
    enam     = scalar( tag = 'ENAM', data_type = esp.Str4, size = 4, null = True )


########################
@record_type('DLBR')

class DLBR(Record):
    editorid = subrecord_group( u'EDITORID' )
    quest    = reference( tag = 'QNAM', refers_to = 'QUST', null = True )
    tnam     = scalar( tag = 'TNAM', data_type = esp.Integer, size = 4, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )
    dialog   = reference( tag = 'SNAM', refers_to = 'DIAL', null = True )


########################
@record_type('MUST')

class MusicTrack(Record):
    editorid = subrecord_group( u'EDITORID' )
    trackType = scalar( tag = 'CNAM', data_type = esp.UnsignedInteger )
    fltv     = scalar( tag = 'FLTV', data_type = esp.Float, size = 4, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Float, null = True )
    anam     = scalar( tag = 'ANAM', data_type = esp.String, null = True )
    lnam     = structure( 'LnamLnam', tag = 'LNAM', size = 12, null = True )
    bnam     = scalar( tag = 'BNAM', data_type = esp.Blob, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Blob, null = True )
    citc     = scalar( tag = 'CITC', data_type = esp.Integer, size = 4, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    musicTrack = reference_set( tag = 'SNAM', refers_to = 'MUST', null = True )


class LnamLnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Integer )


########################
@record_type('DLVW')

class DialogView(Record):
    editorid = subrecord_group( u'EDITORID' )
    quest    = reference( tag = 'QNAM', refers_to = 'QUST', null = True )
    topic    = reference_set( tag = 'TNAM', refers_to = 'DIAL', null = True )
    dialogBranch = reference_set( tag = 'BNAM', refers_to = 'DLBR', null = True )
    enam     = scalar( tag = 'ENAM', data_type = esp.Integer, size = 4, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.UnsignedByte, size = 1, null = True )


########################
@record_type('WOOP')

class WordOfPower(Record):
    concept  = subrecord_group( u'CONCEPT' )
    tnam     = scalar( tag = 'TNAM', data_type = esp.LString, size = 4, null = True )


########################
@record_type('SHOU')

class Shout(Record):
    concept  = subrecord_group( u'CONCEPT' )
    inventoryModel = reference( tag = 'MDOB', refers_to = 'STAT', null = True )
    description = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    shoutData = structure_set( 'ShoutData', tag = 'SNAM', size = 12, null = True )


class ShoutData(Subrecord):
    wordOfPower = reference_field( 'WOOP' )
    spell    = reference_field( 'SPEL' )
    recharge = field( data_type = esp.Float )


########################
@record_type('EQUP')

class EQUP(Record):
    editorid = subrecord_group( u'EDITORID' )
    handReference = reference_set( tag = 'PNAM', refers_to = 'EQUP', null = True )
    occupiesSlot = scalar( tag = 'DATA', data_type = esp.Integer, size = 4, null = True )


########################
@record_type('RELA')

class Relationship(Record):
    editorid = subrecord_group( u'EDITORID' )
    actorData = structure( 'ActorData', tag = 'DATA', size = 16, null = True )


class ActorData(Subrecord):
    npc_Formid1 = reference_field( 'NPC_' )
    npc_Formid2OrPlayer7 = reference_field( 'NPC_' )
    disposition = field( data_type = esp.Integer )
    astpFormid = reference_field( 'ASTP' )


class SCEN_SCHR(SubrecordGroup):
    schr     = structure( 'SCEN_SCHR_0_SchrSchr', tag = 'SCHR', size = 20, null = True )
    quest    = reference( tag = 'QNAM', refers_to = 'QUST', null = True )
    separator = structure( 'SCEN_SCHR_2_SeparatorNext', tag = 'NEXT', null = True )
    scda     = scalar( tag = 'SCDA', data_type = esp.Blob, null = True )
    sctx     = scalar( tag = 'SCTX', data_type = esp.Blob, null = True )
    quest    = reference( tag = 'SCRO', refers_to = 'QUST', null = True )


class SCEN_SCHR_0_SchrSchr(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )


class SCEN_SCHR_2_SeparatorNext(Subrecord):
    pass


########################
@record_type('SCEN')

class Scene(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    scripts  = subrecord_group( u'SCRIPTS' )
    scene_2  = subrecord_group_set( 'Scene_2', null = True )
    scene_3  = subrecord_group_set( 'Scene_3', null = True )
    vnam     = structure( 'Scene_4_VnamVnam', tag = 'VNAM', size = 16, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )


class Scene_2(SubrecordGroup):
    wnam     = scalar_set( tag = 'WNAM', data_type = esp.LString, size = 4, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    hnam     = structure( 'HnamHnam', tag = 'HNAM', null = True )
    nam0     = scalar( tag = 'NAM0', data_type = esp.String, null = True )
    scene_2_4 = subrecord_group_set( 'Scene_2_4', null = True )
    scen_schr = subrecord_group_set( u'SCEN_SCHR', null = True )


class HnamHnam(Subrecord):
    pass


class Scene_2_4(SubrecordGroup):
    seperator = structure( 'Seperator', tag = 'NEXT', null = True )
    conditional = subrecord_group( u'CONDITIONAL', null = True )


class Seperator(Subrecord):
    pass


class Scene_3(SubrecordGroup):
    wnam     = scalar_set( tag = 'WNAM', data_type = esp.LString, size = 4, null = True )
    alid     = scalar( tag = 'ALID', data_type = esp.Integer, size = 4, null = True )
    inam     = scalar( tag = 'INAM', data_type = esp.Integer, size = 4, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    lnam     = scalar( tag = 'LNAM', data_type = esp.Integer, size = 4, null = True )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Integer, size = 4, null = True )
    hnam     = structure( 'Scene_3_6_HnamHnam', tag = 'HNAM', null = True )
    snam     = scalar( tag = 'SNAM', data_type = esp.Integer, size = 4, null = True )
    enam     = scalar( tag = 'ENAM', data_type = esp.Integer, size = 4, null = True )
    dialog   = reference( tag = 'DATA', refers_to = 'DIAL', null = True )
    hnam     = structure( 'Scene_3_10_HnamHnam', tag = 'HNAM', null = True )
    nam0     = scalar( tag = 'NAM0', data_type = esp.String, null = True )
    htid     = scalar( tag = 'HTID', data_type = esp.Integer, size = 4, null = True )
    dmax     = scalar( tag = 'DMAX', data_type = esp.Float, size = 4, null = True )
    dmin     = scalar( tag = 'DMIN', data_type = esp.Float, size = 4, null = True )
    demo     = scalar( tag = 'DEMO', data_type = esp.Integer, size = 4, null = True )
    deva     = scalar( tag = 'DEVA', data_type = esp.Integer, size = 4, null = True )
    anam     = scalar_set( tag = 'ANAM', data_type = esp.Blob, null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Integer, size = 4, null = True )
    scen_schr = subrecord_group_set( u'SCEN_SCHR', null = True )


class Scene_3_6_HnamHnam(Subrecord):
    pass


class Scene_3_10_HnamHnam(Subrecord):
    pass


class Scene_4_VnamVnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


########################
@record_type('ASTP')

class Relationshipassociation(Record):
    editorid = subrecord_group( u'EDITORID' )
    maleParentTitle = scalar( tag = 'MPRT', data_type = esp.String, null = True )
    femaleParentTitle = scalar( tag = 'FPRT', data_type = esp.String, null = True )
    maleChildTitle = scalar( tag = 'MCHT', data_type = esp.String, null = True )
    femaleChildTitle = scalar( tag = 'FCHT', data_type = esp.String, null = True )
    data     = scalar( tag = 'DATA', data_type = esp.Integer, size = 4, null = True )


########################
@record_type('OTFT')

class Outfit(Record):
    editorid = subrecord_group( u'EDITORID' )
    item     = structure( 'Item', tag = 'INAM', null = True )


class Item(Subrecord):
    armor    = reference_field_set( 'ARMO', null = True )
    leveledItem = reference_field_set( 'LVLI', null = True )


########################
@record_type('ARTO')

class ARTO(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    base_model = subrecord_group( u'BASE_MODEL' )
    dnam     = scalar( tag = 'DNAM', data_type = esp.Integer, null = True )


########################
@record_type('MATO')

class MaterialObject(Record):
    editorid = subrecord_group( u'EDITORID' )
    model    = scalar( tag = 'MODL', data_type = esp.String, null = True )
    dnam     = scalar_set( tag = 'DNAM', data_type = esp.Blob, null = True )
    data     = scalar( tag = 'DATA', data_type = esp.Blob, null = True )


########################
@record_type('MOVT')

class MOVT(Record):
    editorid = subrecord_group( u'EDITORID' )
    mnam     = scalar( tag = 'MNAM', data_type = esp.String, null = True )
    speedData = structure( 'SpeedDataSped', tag = 'SPED', size = 44 )
    inam     = structure( 'MOVT_3_InamInam', tag = 'INAM', size = 12, null = True )


class SpeedDataSped(Subrecord):
    strafe1MinSpeed = field( data_type = esp.Float )
    strafe1MaxSpeed = field( data_type = esp.Float )
    strafe2MinSpeed = field( data_type = esp.Float )
    strafe2MaxSpeed = field( data_type = esp.Float )
    forwardMinSpeed = field( data_type = esp.Float )
    forwardMaxSpeed = field( data_type = esp.Float )
    backMinSpeed = field( data_type = esp.Float )
    backMaxSpeed = field( data_type = esp.Float )
    direction1 = field( data_type = esp.Float )
    direction2 = field( data_type = esp.Float )
    direction3 = field( data_type = esp.Float )


class MOVT_3_InamInam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


########################
@record_type('SNDR')

class SoundReference(Record):
    editorid = subrecord_group( u'EDITORID' )
    unknown  = scalar( tag = 'CNAM', data_type = esp.Integer )
    soundCategory = reference( tag = 'GNAM', refers_to = 'SNCT', null = True )
    sound    = reference( tag = 'SNAM', refers_to = 'SNDR', null = True )
    anam     = scalar_set( tag = 'ANAM', data_type = esp.String, null = True )
    soundOutputMarker = reference( tag = 'ONAM', refers_to = 'SOPM', null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    conditional = subrecord_group_set( u'CONDITIONAL', null = True )
    lnam     = scalar( tag = 'LNAM', data_type = esp.Integer, size = 4, null = True )
    bnam     = structure( 'SoundReference_9_BnamBnam', tag = 'BNAM', size = 6, null = True )


class SoundReference_9_BnamBnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Short )


########################
@record_type('DUAL')

class DualCast(Record):
    editorid = subrecord_group( u'EDITORID' )
    object_bounds = subrecord_group( u'OBJECT_BOUNDS', null = True )
    data     = structure( 'DualCast_2_DataData', tag = 'DATA', size = 24, null = True )


class DualCast_2_DataData(Subrecord):
    projFormid = reference_field( 'PROJ' )
    explFormid = reference_field( 'EXPL' )
    efshFormid = reference_field( 'EFSH' )
    artoFormid = reference_field( 'ARTO' )
    unknown4bytes1 = field( data_type = esp.Integer )
    unknown4bytes2 = field( data_type = esp.Integer )


########################
@record_type('SNCT')

class SNCT(Record):
    concept  = subrecord_group( u'CONCEPT' )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    soundCategory = reference( tag = 'PNAM', refers_to = 'SNCT', null = True )
    vnam     = scalar( tag = 'VNAM', data_type = esp.Short, size = 2, null = True )
    unam     = scalar( tag = 'UNAM', data_type = esp.Short, size = 2, null = True )


########################
@record_type('SOPM')

class SOPM(Record):
    editorid = subrecord_group( u'EDITORID' )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    nam1     = scalar( tag = 'NAM1', data_type = esp.Integer, size = 4, null = True )
    mnam     = scalar( tag = 'MNAM', data_type = esp.Integer, size = 4, null = True )
    cnam     = scalar( tag = 'CNAM', data_type = esp.Integer, size = 4, null = True )
    snam     = structure( 'SOPM_5_SnamSnam', tag = 'SNAM', size = 16, null = True )
    onam     = structure( 'OnamOnam', tag = 'ONAM', size = 24, null = True )
    anam     = structure( 'SOPM_7_AnamAnam', tag = 'ANAM', size = 20, null = True )


class SOPM_5_SnamSnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Short )
    unknown1 = field( data_type = esp.Short )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )


class OnamOnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Short )
    unknown3 = field( data_type = esp.Short )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )


class SOPM_7_AnamAnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Float )


########################
@record_type('COLL')

class CollisionLayer(Record):
    editorid = subrecord_group( u'EDITORID' )
    inckDescription = scalar( tag = 'DESC', data_type = esp.LString, null = True )
    bnam     = scalar( tag = 'BNAM', data_type = esp.Integer, size = 4, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )
    gnam     = scalar( tag = 'GNAM', data_type = esp.Integer, size = 4, null = True )
    mnam     = scalar( tag = 'MNAM', data_type = esp.String, null = True )
    countOfInteractables = scalar( tag = 'INTV', data_type = esp.Integer, size = 4, null = True )
    interactableCollisionLayer = reference_set( tag = 'CNAM', refers_to = 'COLL', null = True )


########################
@record_type('CLFM')

class CLFM(Record):
    concept  = subrecord_group( u'CONCEPT' )
    color    = scalar( tag = 'CNAM', data_type = esp.Color, null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.Integer, size = 4, null = True )


########################
@record_type('REVB')

class ReverbParameter(Record):
    editorid = subrecord_group( u'EDITORID' )
    data     = structure( 'ReverbParameter_1_DataData', tag = 'DATA', size = 14, null = True )


class ReverbParameter_1_DataData(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Short )


########################
@record_type('NAVI')

class NavmeshData(Record):
    nver     = scalar( tag = 'NVER', data_type = esp.Integer, size = 4, null = True )
    navmeshDataIfUnsortedDataExistsBelowZposWillBeInaccurate = structure_set( 'NavmeshDataIfUnsortedDataExistsBelowZposWillBeInaccurate', tag = 'NVMI', null = True )
    cumulativeNavmeshData = scalar( tag = 'NVPP', data_type = esp.Blob, null = True )


class NavmeshDataIfUnsortedDataExistsBelowZposWillBeInaccurate(Subrecord):
    actualNavmFormid = reference_field( 'NAVM' )
    allAre0020Or40 = field( data_type = esp.UnsignedInteger )
    navmXpos = field( data_type = esp.Float )
    navmYpos = field( data_type = esp.Float )
    navmZpos = field( data_type = esp.Float )
    preferredMergesFlag = field( data_type = esp.UnsignedInteger )
    ofNavmsMergedto = field( data_type = esp.UnsignedInteger )
    mergedtoNavmFormid = reference_field( 'NAVM' )
    ofPreferredMerges = field( data_type = esp.UnsignedInteger )
    linkedDoors = field( data_type = esp.UnsignedInteger )
    islandFlag = field( data_type = esp.UnsignedByte )
    alwaysA5e9a03c = field( data_type = esp.UnsignedInteger )
    linkedtoNavmFormid = reference_field( 'NAVM' )
    cellgridOrCellFormid = field( data_type = esp.UnsignedInteger )
    unsortedData = field( data_type = esp.Blob )


########################
@record_type('CELL')

class Cell(Record):
    concept  = subrecord_group( u'CONCEPT' )
    data     = scalar( tag = 'DATA', data_type = esp.Blob, null = True )
    cellgridLocationInWrld = structure( 'CellgridLocationInWrld', tag = 'XCLC', size = 12, null = True )
    tvdt     = scalar( tag = 'TVDT', data_type = esp.Blob, null = True )
    mhdt     = scalar( tag = 'MHDT', data_type = esp.Blob, null = True )
    interiorCellLighting = scalar( tag = 'XCLL', data_type = esp.Blob, null = True )
    lightingTemplate = reference( tag = 'LTMP', refers_to = 'LGTM', null = True )
    lnam     = scalar( tag = 'LNAM', data_type = esp.Integer, size = 4, null = True )
    waterrelated = scalar( tag = 'XCLW', data_type = esp.Float, size = 4, null = True )
    xwcs     = scalar( tag = 'XWCS', data_type = esp.Integer, size = 4, null = True )
    cell_10  = subrecord_group_set( 'Cell_10', null = True )
    cell_11  = subrecord_group_set( 'Cell_11', null = True )


class CellgridLocationInWrld(Subrecord):
    x        = field( data_type = esp.Integer )
    y        = field( data_type = esp.Integer )
    externalUnknown = field( data_type = esp.Integer )


class Cell_10(SubrecordGroup):
    region   = reference_set( tag = 'XCLR', refers_to = 'REGN', null = True )
    xnam     = scalar( tag = 'XNAM', data_type = esp.UnsignedByte, null = True )


class Cell_11(SubrecordGroup):
    imageSpace = reference( tag = 'XCIM', refers_to = 'IMGS', null = True )
    locationOfThisCell = reference( tag = 'XLCN', refers_to = 'LCTN', null = True )
    music    = reference( tag = 'XCMO', refers_to = 'MUSC', null = True )
    acousticSpace = reference( tag = 'XCAS', refers_to = 'ASPC', null = True )
    interiorCellClimate = reference( tag = 'XCCM', refers_to = 'REGN', null = True )
    factionOwnership = reference( tag = 'XOWN', refers_to = 'FACT', null = True )
    formList = reference( tag = 'XILL', refers_to = 'FLST', null = True )
    xwcn     = scalar( tag = 'XWCN', data_type = esp.Integer, size = 4, null = True )
    xwcu     = scalar( tag = 'XWCU', data_type = esp.Blob, null = True )
    encounterZone = reference( tag = 'XEZN', refers_to = 'ECZN', null = True )
    water    = reference( tag = 'XCWT', refers_to = 'WATR', null = True )
    xwem     = scalar( tag = 'XWEM', data_type = esp.String, null = True )


########################
@record_type('REFR')

class ObjectReference(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    scripts  = subrecord_group( u'SCRIPTS' )
    baseObject = scalar( tag = 'NAME', data_type = esp.Reference, size = 4, null = True )
    objectBounds = structure( 'ObjectBoundsXmbo', tag = 'XMBO', size = 12, null = True )
    xcvl     = structure( 'Xcvl', tag = 'XCVL', size = 12, null = True )
    xhtw     = scalar( tag = 'XHTW', data_type = esp.Float, size = 4, null = True )
    objectreference_6 = subrecord_group_set( 'ObjectReference_6', null = True )
    fnam     = scalar( tag = 'FNAM', data_type = esp.UnsignedByte, size = 1, null = True )
    fullname = subrecord_group( u'FULLNAME' )
    tnam     = scalar( tag = 'TNAM', data_type = esp.Short, size = 2, null = True )
    xwcn     = scalar( tag = 'XWCN', data_type = esp.Integer, size = 4, null = True )
    xwcu     = structure( 'XwcuXwcu', tag = 'XWCU', size = 48, null = True )
    xspc     = reference( tag = 'XSPC', refers_to = 'REFR', null = True )
    objectreference_13 = subrecord_group_set( 'ObjectReference_13', null = True )
    objectreference_14 = subrecord_group_set( 'ObjectReference_14', null = True )
    xfvc     = scalar( tag = 'XFVC', data_type = esp.Float, size = 4, null = True )
    xocp     = structure( 'Xocp', tag = 'XOCP', size = 36, null = True )
    referenceMarker = structure( 'ReferenceMarker', tag = 'XRMR', size = 4, null = True )
    lightingTemplate = reference( tag = 'LNAM', refers_to = 'LGTM', null = True )
    imagespace = reference( tag = 'INAM', refers_to = 'IMGS', null = True )
    locationRoomMarker = reference_set( tag = 'XLRM', refers_to = 'REFR', null = True )
    xmbp     = structure( 'Xmbp', tag = 'XMBP', null = True )
    scale    = scalar( tag = 'XSCL', data_type = esp.Float, size = 4, null = True )
    onam     = structure( 'ObjectReference_23_OnamOnam', tag = 'ONAM', null = True )
    positionAndRotation = structure( 'PositionAndRotation', tag = 'DATA', size = 24, null = True )


class ObjectBoundsXmbo(Subrecord):
    x1       = field( data_type = esp.Short )
    y1       = field( data_type = esp.Short )
    z1       = field( data_type = esp.Short )
    x2       = field( data_type = esp.Short )
    y2       = field( data_type = esp.Short )
    z2       = field( data_type = esp.Short )


class Xcvl(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Integer )


class ObjectReference_6(SubrecordGroup):
    locationRef = reference( tag = 'XLRT', refers_to = 'LCRT', null = True )
    linkedRef = reference_set( tag = 'XLKR', refers_to = 'KYWD', null = True )
    lightRelated = scalar( tag = 'XRDS', data_type = esp.Float, size = 4, null = True )
    enableScriptPoint = structure( 'EnableScriptPoint', tag = 'XESP', null = True )
    xmrk     = structure( 'XmrkXmrk', tag = 'XMRK', null = True )


class EnableScriptPoint(Subrecord):
    formid   = reference_field( 'REFR' )
    range    = field( data_type = esp.Float )


class XmrkXmrk(Subrecord):
    pass


class XwcuXwcu(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )
    unknown9 = field( data_type = esp.Integer )
    unknown10 = field( data_type = esp.Integer )
    unknown11 = field( data_type = esp.Integer )


class ObjectReference_13(SubrecordGroup):
    xact     = scalar( tag = 'XACT', data_type = esp.Integer, size = 4, null = True )
    doorTeleport = structure( 'DoorTeleport', tag = 'XTEL', size = 32, null = True )


class DoorTeleport(Subrecord):
    doorRefrFormid = reference_field( 'REFR' )
    xPosition = field( data_type = esp.Float )
    yPosition = field( data_type = esp.Float )
    zPosition = field( data_type = esp.Float )
    xRotation = field( data_type = esp.Float )
    yRotation = field( data_type = esp.Float )
    zRotation = field( data_type = esp.Float )
    unknown4bytes = field( data_type = esp.Integer )


class ObjectReference_14(SubrecordGroup):
    messagebox = reference( tag = 'XTNM', refers_to = 'MESG', null = True )
    xmbr     = reference( tag = 'XMBR', refers_to = 'REFR', null = True )
    xrgb     = structure( 'Xrgb', tag = 'XRGB', size = 12, null = True )
    xalp     = scalar( tag = 'XALP', data_type = esp.Short, size = 2, null = True )
    xltw     = reference( tag = 'XLTW', refers_to = 'REFR', null = True )
    ragDollData = scalar( tag = 'XRGD', data_type = esp.Blob, null = True )
    leveledItemBase = reference( tag = 'XLIB', refers_to = 'LVLI', null = True )
    encounterZone = reference( tag = 'XEZN', refers_to = 'ECZN', null = True )
    itemCount = scalar( tag = 'XCNT', data_type = esp.Integer, size = 4, null = True )
    objectreference_14_9 = subrecord_group( 'ObjectReference_14_9', null = True )
    objectreference_14_10 = subrecord_group_set( 'ObjectReference_14_10', null = True )
    xrnk     = scalar( tag = 'XRNK', data_type = esp.Integer, size = 4, null = True )
    xis2     = structure( 'Xis2', tag = 'XIS2', null = True )
    lightRelated = scalar( tag = 'XRDS', data_type = esp.Float, size = 4, null = True )
    xtri     = scalar( tag = 'XTRI', data_type = esp.Integer, size = 4, null = True )
    enableScriptPoint = structure( 'EnableScriptPointXesp', tag = 'XESP', null = True )
    placementOfMarker = structure( 'PlacementOfMarker', tag = 'XPRM', size = 32, null = True )
    lockInformation = structure( 'LockInformation', tag = 'XLOC', size = 20, null = True )
    locationRef = reference( tag = 'XLRT', refers_to = 'LCRT', null = True )
    xczc     = reference( tag = 'XCZC', refers_to = 'CELL', null = True )
    xcza     = scalar( tag = 'XCZA', data_type = esp.Integer, size = 4, null = True )
    factionOwnership = reference( tag = 'XOWN', refers_to = 'FACT', null = True )
    xlcm     = scalar( tag = 'XLCM', data_type = esp.Integer, size = 4, null = True )
    locationOfThisCell = reference( tag = 'XLCN', refers_to = 'LCTN', null = True )
    doorNavmesh = structure( 'DoorNavmesh', tag = 'XNDP', size = 8, null = True )
    activationPointFlags = scalar( tag = 'XAPD', data_type = esp.String, null = True )
    activationPoint = structure_set( 'ActivationPoint', tag = 'XAPR', size = 8, null = True )
    linkedRef = reference_set( tag = 'XLKR', refers_to = 'KYWD', null = True )
    portalDestination = structure( 'PortalDestination', tag = 'XPOD', size = 8, null = True )


class Xrgb(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )


class ObjectReference_14_9(SubrecordGroup):
    lightRelated = scalar( tag = 'XRDS', data_type = esp.Float, size = 4, null = True )
    emittance = reference( tag = 'XEMI', refers_to = 'LIGH', null = True )
    xpwr     = reference_set( tag = 'XPWR', refers_to = 'REFR', null = True )
    lightData = structure( 'LightDataXlig', tag = 'XLIG', size = 16, null = True )


class LightDataXlig(Subrecord):
    unknownFloat1 = field( data_type = esp.Float )
    unknownFloat2 = field( data_type = esp.Float )
    unknownFloat3 = field( data_type = esp.Float )
    unknownFloat4 = field( data_type = esp.Float )


class ObjectReference_14_10(SubrecordGroup):
    xprd     = scalar( tag = 'XPRD', data_type = esp.Float, size = 4 )
    xppa     = structure( 'Xppa', tag = 'XPPA', null = True )
    imagespace = reference( tag = 'INAM', refers_to = 'IMGS', null = True )
    schr     = structure( 'ObjectReference_14_10_3_SchrSchr', tag = 'SCHR', size = 20, null = True )
    sctx     = structure( 'ObjectReference_14_10_4_SctxSctx', tag = 'SCTX', null = True )
    pdto     = structure( 'ObjectReference_14_10_5_PdtoPdto', tag = 'PDTO', size = 8, null = True )


class Xppa(Subrecord):
    pass


class ObjectReference_14_10_3_SchrSchr(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )


class ObjectReference_14_10_4_SctxSctx(Subrecord):
    pass


class ObjectReference_14_10_5_PdtoPdto(Subrecord):
    unknown  = field( data_type = esp.Integer )
    dialFormid = reference_field( 'DIAL' )


class Xis2(Subrecord):
    pass


class EnableScriptPointXesp(Subrecord):
    formid   = reference_field( 'REFR' )
    range    = field( data_type = esp.Float )


class PlacementOfMarker(Subrecord):
    boundsx  = field( data_type = esp.Float )
    boundsy  = field( data_type = esp.Float )
    boundsz  = field( data_type = esp.Float )
    placementx = field( data_type = esp.Float )
    placementy = field( data_type = esp.Float )
    placementz = field( data_type = esp.Float )
    unknown  = field( data_type = esp.Float )
    unknown  = field( data_type = esp.Integer )


class LockInformation(Subrecord):
    unknownFlags = field( data_type = esp.UnsignedInteger )
    keymFormid = reference_field( 'KEYM' )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )


class DoorNavmesh(Subrecord):
    navmFormid = reference_field( 'NAVM' )
    unknown4bytes = field( data_type = esp.Integer )


class ActivationPoint(Subrecord):
    formid   = reference_field( 'REFR' )
    unknownFloat = field( data_type = esp.Float )


class PortalDestination(Subrecord):
    originFormid = reference_field( 'REFR' )
    destinationFormid = reference_field( 'REFR' )


class Xocp(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )
    unknown4 = field( data_type = esp.Float )
    unknown5 = field( data_type = esp.Float )
    unknown6 = field( data_type = esp.Float )
    unknown7 = field( data_type = esp.Float )
    unknown8 = field( data_type = esp.Float )


class ReferenceMarker(Subrecord):
    count    = field( data_type = esp.UnsignedShort )
    flags    = field( data_type = esp.UnsignedShort )


class Xmbp(Subrecord):
    pass


class ObjectReference_23_OnamOnam(Subrecord):
    pass


class PositionAndRotation(Subrecord):
    xPosition = field( data_type = esp.Float )
    yPosition = field( data_type = esp.Float )
    zPosition = field( data_type = esp.Float )
    xRotation = field( data_type = esp.Float )
    yRotation = field( data_type = esp.Float )
    zRotation = field( data_type = esp.Float )


########################
@record_type('WRLD')

class WorldSpace(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    rnam     = scalar_set( tag = 'RNAM', data_type = esp.Blob, null = True )
    mhdt     = scalar( tag = 'MHDT', data_type = esp.Blob, null = True )
    fullname = subrecord_group( u'FULLNAME' )
    wctr     = scalar( tag = 'WCTR', data_type = esp.Integer, size = 4, null = True )
    lightingTemplate = reference( tag = 'LTMP', refers_to = 'LGTM', null = True )
    encounterZone = reference( tag = 'XEZN', refers_to = 'ECZN', null = True )
    locationOfThisWrld = reference( tag = 'XLCN', refers_to = 'LCTN', null = True )
    parentWorldspace = reference( tag = 'WNAM', refers_to = 'WRLD', null = True )
    pnam     = scalar( tag = 'PNAM', data_type = esp.Short, size = 2, null = True )
    climateData = reference( tag = 'CNAM', refers_to = 'CLMT', null = True )
    nam2     = scalar( tag = 'NAM2', data_type = esp.Integer, size = 4, null = True )
    nam3     = scalar( tag = 'NAM3', data_type = esp.Integer, size = 4, null = True )
    nam4     = scalar( tag = 'NAM4', data_type = esp.Float, size = 4, null = True )
    dnam     = structure( 'WorldSpace_14_DnamDnam', tag = 'DNAM', size = 8, null = True )
    worldBounds = structure( 'WorldBounds', tag = 'MNAM', size = 16, null = True )
    onam     = structure( 'WorldSpace_16_OnamOnam', tag = 'ONAM', size = 16, null = True )
    nama     = scalar( tag = 'NAMA', data_type = esp.Float, size = 4, null = True )
    data     = scalar( tag = 'DATA', data_type = esp.UnsignedByte, size = 1, null = True )
    nam0     = structure( 'WorldSpace_19_Nam0Nam0', tag = 'NAM0', size = 8, null = True )
    nam9     = structure( 'Nam9Nam9', tag = 'NAM9', size = 8, null = True )
    musicType = reference( tag = 'ZNAM', refers_to = 'MUSC', null = True )
    tnam     = structure( 'WorldSpace_22_TnamTnam', tag = 'TNAM', size = 53, null = True )
    unam     = structure( 'WorldSpace_23_UnamUnam', tag = 'UNAM', size = 55, null = True )
    ofst     = scalar( tag = 'OFST', data_type = esp.Blob, null = True )


class WorldSpace_14_DnamDnam(Subrecord):
    unknownFloat1 = field( data_type = esp.Float )
    unknownFloat2 = field( data_type = esp.Float )


class WorldBounds(Subrecord):
    width    = field( data_type = esp.Integer )
    height   = field( data_type = esp.Integer )
    nwCellX  = field( data_type = esp.Short )
    nwCellY  = field( data_type = esp.Short )
    seCellX  = field( data_type = esp.Short )
    seCellY  = field( data_type = esp.Short )


class WorldSpace_16_OnamOnam(Subrecord):
    unknown  = field( data_type = esp.Float )
    unknown1 = field( data_type = esp.Float )
    unknown2 = field( data_type = esp.Float )
    unknown3 = field( data_type = esp.Float )


class WorldSpace_19_Nam0Nam0(Subrecord):
    unknownFloat1 = field( data_type = esp.Float )
    unknownFloat2 = field( data_type = esp.Float )


class Nam9Nam9(Subrecord):
    unknownFloat1 = field( data_type = esp.Float )
    unknownFloat2 = field( data_type = esp.Float )


class WorldSpace_22_TnamTnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )
    unknown9 = field( data_type = esp.Integer )
    unknown10 = field( data_type = esp.Integer )
    unknown11 = field( data_type = esp.Integer )
    unknown12 = field( data_type = esp.Integer )
    unknown13 = field( data_type = esp.Short )


class WorldSpace_23_UnamUnam(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )
    unknown5 = field( data_type = esp.Integer )
    unknown6 = field( data_type = esp.Integer )
    unknown7 = field( data_type = esp.Integer )
    unknown8 = field( data_type = esp.Integer )
    unknown9 = field( data_type = esp.Integer )
    unknown10 = field( data_type = esp.Integer )
    unknown11 = field( data_type = esp.Integer )
    unknown12 = field( data_type = esp.Integer )
    unknown13 = field( data_type = esp.Short )
    unknown14 = field( data_type = esp.Short )


########################
@record_type('LAND')

class Landscape(Record):
    data     = scalar( tag = 'DATA', data_type = esp.Integer, size = 4, null = True )
    vertexNormals = scalar( tag = 'VNML', data_type = esp.Blob, size = 3267, null = True )
    vertexHeight = scalar( tag = 'VHGT', data_type = esp.Blob, size = 1096, null = True )
    vertexColorshading = scalar( tag = 'VCLR', data_type = esp.Blob, size = 3267, null = True )
    landscape_4 = subrecord_group_set( 'Landscape_4', null = True )


class Landscape_4(SubrecordGroup):
    baseTextureByQuardrant = structure( 'BaseTextureByQuardrant', tag = 'BTXT', size = 8, null = True )
    landscape_4_1 = subrecord_group_set( 'Landscape_4_1', null = True )


class BaseTextureByQuardrant(Subrecord):
    ltexFormid = reference_field( 'LTEX' )
    quadrant = field( data_type = esp.Short )
    bufferflag = field( data_type = esp.Short )


class Landscape_4_1(SubrecordGroup):
    additionalTexture = structure( 'AdditionalTexture', tag = 'ATXT', size = 8 )
    vtxt     = scalar( tag = 'VTXT', data_type = esp.Blob )


class AdditionalTexture(Subrecord):
    ltexFormid = reference_field( 'LTEX' )
    unknown4bytes = field( data_type = esp.Integer )


########################
@record_type('PHZD')

class PlacedHazard(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    scripts  = subrecord_group( u'SCRIPTS' )
    baseFormOfHazard = reference( tag = 'NAME', refers_to = 'HAZD', null = True )
    placedhazard_3 = subrecord_group_set( 'PlacedHazard_3', null = True )
    positionAndRotation = structure( 'PositionAndRotationData', tag = 'DATA', size = 24, null = True )


class PlacedHazard_3(SubrecordGroup):
    scale    = scalar( tag = 'XSCL', data_type = esp.Float, size = 4, null = True )
    enableScriptPoint = structure( 'PlacedHazard_3_1_EnableScriptPointXesp', tag = 'XESP', size = 8, null = True )


class PlacedHazard_3_1_EnableScriptPointXesp(Subrecord):
    refrFormid = reference_field( 'REFR' )
    unknown  = field( data_type = esp.Float )


class PositionAndRotationData(Subrecord):
    xPosition = field( data_type = esp.Float )
    yPosition = field( data_type = esp.Float )
    zPosition = field( data_type = esp.Float )
    xRotation = field( data_type = esp.Float )
    yRotation = field( data_type = esp.Float )
    zRotation = field( data_type = esp.Float )


########################
@record_type('PGRE')

class PlacedGrenade(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    baseFormOfGrenade = reference( tag = 'NAME', refers_to = 'PROJ', null = True )
    scale    = scalar( tag = 'XSCL', data_type = esp.Float, size = 4, null = True )
    placedgrenade_3 = subrecord_group_set( 'PlacedGrenade_3', null = True )
    positionAndRotation = structure( 'PlacedGrenade_4_PositionAndRotationData', tag = 'DATA', size = 24, null = True )


class PlacedGrenade_3(SubrecordGroup):
    factionOwnership = reference( tag = 'XOWN', refers_to = 'FACT', null = True )
    enableScriptPoint = structure( 'PlacedGrenade_3_1_EnableScriptPointXesp', tag = 'XESP', size = 8, null = True )


class PlacedGrenade_3_1_EnableScriptPointXesp(Subrecord):
    refrFormid = reference_field( 'REFR' )
    unknown4bytes = field( data_type = esp.Integer )


class PlacedGrenade_4_PositionAndRotationData(Subrecord):
    xPosition = field( data_type = esp.Float )
    yPosition = field( data_type = esp.Float )
    zPosition = field( data_type = esp.Float )
    xRotation = field( data_type = esp.Float )
    yRotation = field( data_type = esp.Float )
    zRotation = field( data_type = esp.Float )


########################
@record_type('ACHR')

class ActorReference(Record):
    editorid = subrecord_group( u'EDITORID', null = True )
    scripts  = subrecord_group( u'SCRIPTS' )
    baseFormOfActorNpc_ = reference( tag = 'NAME', refers_to = 'NPC_', null = True )
    actorreference_3 = subrecord_group_set( 'ActorReference_3', null = True )
    scale    = scalar( tag = 'XSCL', data_type = esp.Float, size = 4, null = True )
    positionAndRotation = structure( 'ActorReference_5_PositionAndRotationData', tag = 'DATA', size = 24, null = True )


class ActorReference_3(SubrecordGroup):
    xlcm     = scalar( tag = 'XLCM', data_type = esp.Integer, size = 4, null = True )
    ragDollData = scalar( tag = 'XRGD', data_type = esp.Blob, null = True )
    xrgb     = structure( 'XrgbXrgb', tag = 'XRGB', size = 12, null = True )
    locationOfThisRef = reference( tag = 'XLCN', refers_to = 'LCTN', null = True )
    factionOwnership = reference( tag = 'XOWN', refers_to = 'FACT', null = True )
    locationRef = reference( tag = 'XLRT', refers_to = 'LCRT', null = True )
    linkedRef = reference_set( tag = 'XLKR', refers_to = 'KYWD', null = True )
    activationPointFlags = scalar( tag = 'XAPD', data_type = esp.String, null = True )
    xis2     = structure( 'Xis2Xis2', tag = 'XIS2', null = True )
    activationPoint = structure_set( 'ActivationPointXapr', tag = 'XAPR', size = 8, null = True )
    enableScriptPoint = structure( 'ActorReference_3_10_EnableScriptPointXesp', tag = 'XESP', size = 8, null = True )
    actorreference_3_11 = subrecord_group_set( 'ActorReference_3_11', null = True )
    encounterZone = reference( tag = 'XEZN', refers_to = 'ECZN', null = True )
    ownedHorseRef = reference( tag = 'XHOR', refers_to = 'ACHR', null = True )


class XrgbXrgb(Subrecord):
    r        = field( data_type = esp.Float )
    g        = field( data_type = esp.Float )
    b        = field( data_type = esp.Float )


class Xis2Xis2(Subrecord):
    pass


class ActivationPointXapr(Subrecord):
    formid   = reference_field( 'REFR' )
    unknownFloat = field( data_type = esp.Float )


class ActorReference_3_10_EnableScriptPointXesp(Subrecord):
    refrFormid = reference_field( 'REFR' )
    unknown4bytes = field( data_type = esp.Integer )


class ActorReference_3_11(SubrecordGroup):
    xprd     = scalar( tag = 'XPRD', data_type = esp.Float, size = 4 )
    xppa     = structure( 'XppaXppa', tag = 'XPPA', null = True )
    imagespace = reference( tag = 'INAM', refers_to = 'IMGS', null = True )
    schr     = structure( 'ActorReference_3_11_3_SchrSchr', tag = 'SCHR', size = 20, null = True )
    dialog   = structure( 'DialogPdto', tag = 'PDTO', size = 8, null = True )


class XppaXppa(Subrecord):
    pass


class ActorReference_3_11_3_SchrSchr(Subrecord):
    unknown  = field( data_type = esp.Integer )
    unknown1 = field( data_type = esp.Integer )
    unknown2 = field( data_type = esp.Integer )
    unknown3 = field( data_type = esp.Integer )
    unknown4 = field( data_type = esp.Integer )


class DialogPdto(Subrecord):
    unknown4bytes = field( data_type = esp.Integer )
    dialFormid = reference_field( 'DIAL' )


class ActorReference_5_PositionAndRotationData(Subrecord):
    xPosition = field( data_type = esp.Float )
    yPosition = field( data_type = esp.Float )
    zPosition = field( data_type = esp.Float )
    xRotation = field( data_type = esp.Float )
    yRotation = field( data_type = esp.Float )
    zRotation = field( data_type = esp.Float )


########################
@record_type('NAVM')

class NavmeshReference(Record):
    navmeshGeometry = structure( 'NavmeshGeometry', tag = 'NVNM', null = True )
    unknownOnam = reference_set( tag = 'ONAM', refers_to = 'STAT', null = True )
    unknownPnam = scalar( tag = 'PNAM', data_type = esp.Blob, null = True )
    unknownNnam = scalar( tag = 'NNAM', data_type = esp.Blob, null = True )


class NavmeshGeometry(Subrecord):
    unknownValue1 = field( data_type = esp.UnsignedInteger )
    possiblyLocationMarker = field( data_type = esp.UnsignedInteger )
    worldSpace = reference_field( 'WRLD' )
    cellOrGrid = field( data_type = esp.UnsignedInteger )
    vertexCount = field( data_type = esp.Integer )
    vertexXposContinues = field( data_type = esp.Float )
    vertexYposUntilBefore = field( data_type = esp.Float )
    vertexZposFfsStart = field( data_type = esp.Float )
    unknwon500sNearEndStartsTris = field( data_type = esp.Blob )

