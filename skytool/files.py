
__doc__=\
'''
Models and views on files in filesystems.

Contained files can have arbitrary metadata added.
'''

import os, os.path

path_join = os.path.join
path_exists = os.path.exists

def all_super_dirs(fname, sep='/'):
    '''Sequence of all subpaths that make up the path to the filename.
    Filename itself (last part of fname) is assumed to be a file and ignored.
    '''
    dir_parts = fname.split(sep)[:-1]
    for count in range(len(dir_parts)):
        yield '/'.join(dir_parts[:count+1])


class FileTree:
    '''Provides a unified or filtered view of the file system
    based on present files and installed mods.
    '''
    def __init__(self, base):
        self.base = base
        self.file_tree = {}
        self.path_index = {}

    def walk(self, breadth_first = True):
        assert breadth_first, "Depth-first not implemented"
        raise NotImplementedError

    __file_metadata = ('name', 'size', 'modified_date', 'exists')

    @staticmethod
    def all_metadata_keys(self):
        keys = {}

        for c in self.__class__.__mro__.reverse():
            cdict = c.__dict__
            keys.update(cdict.get('__file_metadata', {}))

        return keys

    def exists(self, fent):
        raise NotImplementedError



class FileSource:
    def __init__(self, name, path):
        self.name = name
        self.path = path


class FileEntry:
    '''Contains information about a single file in a file tree.
    
    The metadata dict can contain metadata info from a number of different file tree types.
    '''
    def __init__(self, path, tree, metadata = None):
        self.path = path
        self.tree = tree
        self.metadata = {} if metadata is None else metadata
        self.get = self.metadata.get

    def get_data(self, key, default = None):
        return self.metadata.get(key, default)

    def full_path(self, _join = path_join):
        return _join(self.tree.base, self.path)


class MetadataOverlay:
    '''A set of logical metadata keys that can be added to a file entry.
    Keys are added to the fent prefixed with with the key prefix and ".".
    '''
    def __init__(self, key_prefix, keys, defaults = None):
        self.key_prefix = {}
        self.keys = keys
        self.defaults = defaults or dict((k, None) for k in keys)
        self.keys_complete = dict((k, ('.'.join([key_prefix, k]))) for k in keys)

    def get(self, file_entry, key):
        return file_entry.metadata.get(self.keys_complete[key], self.defaults[key])



class PhysicalFileTree(FileTree):
    def exists(self, fent):
        return path_exists(fent.full_path())
