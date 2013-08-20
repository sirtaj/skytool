
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


###################

class Mod(FileSource):
    def __init__(self, name, key, path, version, install_date):
        FileSource.__init__(self, name, path)

        self.key = key
        self.version = version
        self.install_date = install_date


class DataFile:
    def __init__(self, path, installing_mods):
        self.path = path
        self.installing_mods = installing_mods

    F_OK = 0
    F_MISSING = 1
    F_CHANGED = 2


class ModCollection(object):
    def __init__(self, game):
        self.game = game

    def parse_install(self):
        '''Update information on available and installed mods.

        This is a separate method since it's expected to be slow.

        Users of the collection should assume that info is not available until this is
        called.
        '''
        pass

    def has_file(self, relative_path):
        raise NotImplementedError

    def has_dir(self, relative_path):
        raise NotImplementedError


class DumbModCollection(ModCollection):
    '''Tracks paths with dictionaries
    '''
    def __init__(self, game):
        super(DumbModCollection, self).__init__(game)
        self.mods = {}
        self.data_files = {}        # relative data file name -> DataFile Object
        self.contained_dirs = {}

        # implement the lookup interface
        self.has_file = self.data_files.get
        self.has_dir = self.contained_dirs.get

    # build helpers

    def add_mod(self, mod):
        self.mods[mod.key] = mod

    def add_data_file(self, data_file):
        df_idx = data_file.path.lower().replace('\\', '/')

        self.data_files[df_idx] = data_file
        self.contained_dirs.update((sup, True) for sup in all_super_dirs(df_idx))


class FileList(DumbModCollection):
    def __init__(self, game, file_list_path):
        super(FileList, self).__init__(game)
        self.file_list_path = file_list_path

    def parse_install(self):
        with open(self.file_list_path, 'r') as fd:
            for line in fd.readlines():
                line = line.strip()
                if not line or line.startswith('#') : continue

                words = line.split()
                path = words.pop(0)
                checksum = words[0] if words else None

                if path.endswith('/'):
                    self.contained_dirs.update((sup, True) for sup in all_super_dirs(df_idx))
                else:
                    self.add_data_file(path)


class UnionCollection(ModCollection):
    '''A union of file collections.
    '''
    def __init__(self, game):
        super(UnionCollection, self).__init__(game)

        self.sub_collections = []
        self.initialized_collections = []
        self.parsed = False

    ### New Methods

    def add_collection(self, collection):
        self.sub_collections.append(collection)

        if self.parsed:
            collection.parse_install()
            self.initialized_collections.append(collection)


    ### ModCollection Interface

    def parse_install(self):
        for collection in self.sub_collections:
            if collection not in self.initialized_collections:
                collection.parse_install()
        self.parsed = True

    def has_file(self, relative_path):
        for collection in self.sub_collections:
            if collection.has_file(relative_path):
                return True
        return False

    def has_dir(self, relative_path):
        for collection in self.sub_collections:
            if collection.has_dir(relative_path):
                return True
        return False



