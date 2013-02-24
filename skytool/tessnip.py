
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

    def __iter__(self): return iter(self.children)


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

    def __iter__(self): return iter(self.children)



class Group(object):
    '''
        Contained by: Group, Record, Records
        Contains: ['Subrecord', 'Group']
    '''
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    repeat = typed_property('repeat', 'int', 0)
    optional = typed_property('optional', 'int', 0)
    id = typed_property('id', 'ident')

    children = typed_collection('children', ['Subrecord', 'Group'])

    def __iter__(self): return iter(self.children)


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

    condid = typed_property('condid', 'int')
    condition = typed_property('condition', 'ident')
    condvalue = typed_property('condvalue', 'ident')
    desc = typed_property('desc', 'text')
    name = typed_property('name', 'ident')
    notininfo = typed_property('notininfo', 'int', 0)
    optional = typed_property('optional', 'int', 0)
    repeat = typed_property('repeat', 'int', 0)
    size = typed_property('size', 'int')

    elements = typed_collection('elements', ['Element'])

    def __iter__(self): return iter(self.elements)


class Element(object):
    '''
        Contained by: Subrecord
    '''
    def __init__(self, name, type, **kwargs):
        self.name = name
        self.type = type
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    condid = typed_property('condid', 'int')
    desc = typed_property('desc', 'text')
    flags = typed_property('flags', 'text')
    hexview = typed_property('hexview', 'ident')
    multiline = typed_property('multiline', 'int', 0)
    name = typed_property('name', 'text')
    notininfo = typed_property('notininfo', 'int', 0)
    optional = typed_property('optional', 'int', 0)
    options = typed_property('options', 'text')
    reftype = typed_property('reftype', 'ident')
    repeat = typed_property('repeat', 'int', 0)
    type = typed_property('type', 'ident')
