
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


class ModLog:
    def __init__(self, nexus):
        self.nexus = nexus
        self.mods = {}
        self.data_files = {} # relative data file name -> DataFile Object
        self.contained_dirs = {}

    def add_mod(self, mod):
        self.mods[mod.key] = mod

    def add_data_file(self, data_file):
        df_idx = data_file.path.lower().replace('\\', '/')

        self.data_files[df_idx] = data_file
        self.contained_dirs.update((sup, True) for sup in all_super_dirs(df_idx))
        

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


class Nexus:
    def __init__(self, game):
        self.game = game or Skyrim()
        self.install_log_path = path_join(self.game.install_path, 'Install Info', 'InstallLog.xml')
        self.mod_respository = path_join(self.game.install_path, 'Mods')
        self.mod_log = ModLog(self)

    def parse_install(self):
        from xml.etree.ElementTree import parse as xml_parse
        log = self.mod_log

        tree = xml_parse(self.install_log_path).getroot()
        self.parse_mods(tree, log)
        self.parse_files(tree, log)

    def parse_mods(self, root, log):
        # installed mods
        for mod_el in root.find('modList').iterfind('mod'):
            log.add_mod(Mod( mod_el.find('name').text,
                            mod_el.get('key'),
                            mod_el.get('path'),
                            mod_el.find('version'),
                            self.parse_timestamp(mod_el.find('installDate').text)))

    def parse_files(self, root, log):
        # installed files
        for f_el in root.find('dataFiles').iterfind('file'):
            log.add_data_file(DataFile( f_el.get('path'),
                                [log.mods[k.get('key')]
                                    for k in f_el.find('installingMods').iterfind('mod')]))


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

    def untracked_files(self, data_only = True):
        game = self.game
        root = game.data_path if data_only else game.install_path
        root_len = len(game.install_path)
        d_files = self.mod_log.data_files

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


    def missing_files(self):
        verify = self.file_exists

        for df in self.mod_log.data_files.itervalues():
            if not verify(df):
                print [m.name for m in df.installing_mods], df.path

# Main

def test_run():
    n = Nexus()

    print "loading..."
    n.parse_install()
    print 'Mods:', len(n.mod_log.mods)
    print 'Files:', len(n.mod_log.data_files)

    print "untracked files:"
    for uf in n.untracked_files(n):
        print '\t', uf



if __name__ == '__main__':
    test_run()
