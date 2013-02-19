
'''
Tools for loading Nexus Mod Manager file install history
and comparing it with the data folder of an installed TES game.


'''

from files import FileSource, all_super_dirs
from game import Skyrim

from datetime import datetime
import os, os.path, re

path_join = os.path.join
path_exists = os.path.exists


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








################

class Nexus(DumbModCollection):
    def __init__(self, game):
        super(Nexus, self).__init__(game)
        self.install_log_path = path_join(self.game.install_path, 'Install Info', 'InstallLog.xml')
        self.mod_respository = path_join(self.game.install_path, 'Mods')

    def parse_install(self):
        from xml.etree.ElementTree import parse as xml_parse
        tree = xml_parse(self.install_log_path).getroot()
        self.parse_mods(tree)
        self.parse_files(tree)

    ### Loader helpers

    def parse_mods(self, root):
        # installed mods
        for mod_el in root.find('modList').iterfind('mod'):
            self.add_mod(Mod( mod_el.find('name').text,
                            mod_el.get('key'),
                            mod_el.get('path'),
                            mod_el.find('version'),
                            self.parse_timestamp(mod_el.find('installDate').text)))

    def parse_files(self, root):
        # installed files
        for f_el in root.find('dataFiles').iterfind('file'):
            self.add_data_file(DataFile( f_el.get('path'),
                                [self.mods[k.get('key')]
                                    for k in f_el.find('installingMods').iterfind('mod')]))



    ### physical file stuff - don't use these
    def full_path(self, data_file):
        return path_join(self.game.install_path, data_file.path)

    def file_exists(self, data_file):
        return path_exists(self.full_path(data_file))

    @staticmethod
    def parse_timestamp(stamp,
                _match = re.compile(r'^(\d+)/(\d+)/(\d+)\s+(\d+):(\d+):(\d+)\s+(AM|PM)$').match):
        m = _match(stamp)
        if not m: return None

        (month, day, year, hour, minu, sec) = (int(v) for v in m.group(1,2,3,4,5,6))

        hour %= 12
        if m.group(7) == 'PM':
            hour += 12

        return datetime(year, month, day, hour, minu, sec)



#### Queries

def untracked_files(mod_collection, data_only = True):
    game = mod_collection.game
    root = game.data_path if data_only else game.install_path
    root_len = len(game.install_path)
    d_files = mod_collection.data_files

    total_files = 0
    total_untracked = 0


    for (dirpath, dirnames, filenames) in os.walk(root):
        rel_pfx = dirpath[root_len:]
        for fnam in filenames:
            total_files += 1
            rel_name = path_join(rel_pfx, fnam)
            if rel_name.lower() not in d_files:
                total_untracked += 1
                yield rel_name

    print 'files: total:', total_files, 'untracked:', total_untracked


def missing_files(mod_collection):
    verify = mod_collection.file_exists

    for df in mod_collection.data_files.itervalues():
        if not verify(df):
                print [m.name for m in df.installing_mods], df.path

# Main

def test_run():
    game = Skyrim()
    n = Nexus(game)

    print "loading..."
    n.parse_install()
    print 'Mods:', len(n.mods)
    print 'Files:', len(n.data_files)

    print "untracked files:"
    for uf in untracked_files(n):
        print '\t', uf



if __name__ == '__main__':
    test_run()
