
'''
    Root element: Records
'''

from xrev import typed_property, typed_collection

class Records(object):
    '''
        Contains: ['Group', 'Record']
    '''
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    children = typed_collection('children', ['Group', 'Record'])


class Record(object):
    '''
        Contained by: Records
        Contains: ['Subrecord', 'Group']
    '''
    def __init__(self, name, desc, **kwargs):
        self.name = name
        self.desc = desc
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    name = typed_property('name', 'ident')
    desc = typed_property('desc', 'text')

    children = typed_collection('children', ['Subrecord', 'Group'])


class Element(object):
    '''
        Contained by: Subrecord
    '''
    def __init__(self, name, type, **kwargs):
        self.name = name
        self.type = type
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    reftype = typed_property('reftype', 'ident')
    repeat = typed_property('repeat', 'int')
    name = typed_property('name', 'text')
    optional = typed_property('optional', 'int')
    hexview = typed_property('hexview', 'ident')
    condid = typed_property('condid', 'int')
    flags = typed_property('flags', 'text')
    notininfo = typed_property('notininfo', 'ident')
    multiline = typed_property('multiline', 'ident')
    type = typed_property('type', 'ident')
    options = typed_property('options', 'text')
    desc = typed_property('desc', 'text')


class Group(object):
    '''
        Contained by: Group, Record, Records
        Contains: ['Subrecord', 'Group']
    '''
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    repeat = typed_property('repeat', 'int')
    optional = typed_property('optional', 'int')
    id = typed_property('id', 'ident')

    children = typed_collection('children', ['Subrecord', 'Group'])


class Subrecord(object):
    '''
        Contained by: Group, Record
        Contains: ['Element']
    '''
    def __init__(self, name, desc, **kwargs):
        self.name = name
        self.desc = desc
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    repeat = typed_property('repeat', 'int')
    name = typed_property('name', 'ident')
    condid = typed_property('condid', 'int')
    condvalue = typed_property('condvalue', 'ident')
    notininfo = typed_property('notininfo', 'int')
    desc = typed_property('desc', 'text')
    optional = typed_property('optional', 'int')
    condition = typed_property('condition', 'ident')
    size = typed_property('size', 'int')

    elements = typed_collection('elements', ['Element'])

