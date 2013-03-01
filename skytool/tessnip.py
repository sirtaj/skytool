
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
    def __repr__(self): return "<Record %s: %s>" % (repr(self.desc), repr(self.name))
    def names(self): return [self.desc, self.name]



class Group(object):
    '''
        Contained by: Group, Record, Records
        Contains: ['Subrecord', 'Group']
    '''
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    id = typed_property('id', 'ident')

    repeat = typed_property('repeat', 'bool', False)
    optional = typed_property('optional', 'bool', False)

    children = typed_collection('children', ['Subrecord', 'Group'])

    def __iter__(self): return iter(self.children)
    def __repr__(self): return "<Group %s>" % (repr(self.id))
    def names(self): return [self.id]


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

    name = typed_property('name', 'ident')
    desc = typed_property('desc', 'text')

    repeat = typed_property('repeat', 'bool', False)
    optional = typed_property('optional', 'bool', False)

    size = typed_property('size', 'int')

    condid = typed_property('condid', 'int')          # TODO
    condition = typed_property('condition', 'ident')  # TODO
    condvalue = typed_property('condvalue', 'ident')  # TODO

    notininfo = typed_property('notininfo', 'int', 0) # TODO

    elements = typed_collection('elements', ['Element'])

    def __iter__(self): return iter(self.elements)
    def __repr__(self): return "<Subrecord %s: %s>" % (repr(self.desc), repr(self.name))
    def names(self): return [self.desc or self.name, self.desc, self.name,
                                self.desc + "_" + self.name]

    def is_scalar(self): return len(self.elements) == 1


class Element(object):
    '''
        Contained by: Subrecord
    '''
    def __init__(self, name, type, **kwargs):
        self.name = name
        self.type = type
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    name = typed_property('name', 'text')
    type = typed_property('type', 'ident')

    desc = typed_property('desc', 'text')
    reftype = typed_property('reftype', 'ident')
    repeat = typed_property('repeat', 'bool', False)
    optional = typed_property('optional', 'bool', False)

    multiline = typed_property('multiline', 'bool', False) # TODO
    condid = typed_property('condid', 'int') # TODO
    options = typed_property('options', 'text') # TODO
    flags = typed_property('flags', 'text') # TODO

    hexview = typed_property('hexview', 'ident') # TODO
    notininfo = typed_property('notininfo', 'bool', False) # TODO

    calculated = typed_property('isCalculated', 'bool', False) # TODO
    fixedValue = typed_property('fixedValue', 'text') # TODO
    default = typed_property('default', 'text') # TODO


    def __iter__(self): return iter([])
    def __repr__(self): return "<Element %s (%s)>" % (repr(self.name), self.type)
