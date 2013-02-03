

import game

import os, os.path, re, datetime
path_join = os.path.join
path_exists = os.path.exists

nexus_time_re = re.compile(r'^(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)\s+(?P<hour>\d+):(?P<min>\d+):(?P<sec>\d+)\s+(?P<tod>AM|PM)$')


def parse_nexus_time(text_stamp):
    m = nexus_time_re.match(text_stamp)
    if not m:
        return None

    d = (month, day, year, hour, minu, sec) = tuple(int(v) for v in m.group(1,2,3,4,5,6))

    hour %= 12
    if m.group('tod') == 'PM':
        hour += 12

    return datetime.datetime(year, month, day, hour, minu, sec)

class ModLog:
    def __init__(self, nexus):
        self.nexus = nexus
        self.mods = {}
        self.data_files = {}

    def add_mod(self, key, mod):
        self.mods[key] = mod

    def add_data_file(self, data_file):
        self.data_files[data_file.path.lower()] = data_file



class Mod:
    def __init__(self, name, path, version, install_date):
        self.name = name
        self.path = path
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
    def __init__(self):
        self.sky = game.Skyrim()
        self.install_log_path = path_join(self.sky.install_path, 'Install Info', 'InstallLog.xml')
        self.mod_log = ModLog(self)

    def parse_install(self):
        from xml.etree.ElementTree import parse as xml_parse
        log = self.mod_log

        tree = xml_parse(self.install_log_path)

        # installed mods
        for mod_el in tree.getroot().find('modList').iterfind('mod'):
            log.add_mod( mod_el.get('key'),
                        Mod( mod_el.find('name').text,
                            mod_el.get('path'),
                            mod_el.find('version'),
                            parse_nexus_time(mod_el.find('installDate').text)))


        # installed files
        for f_el in tree.getroot().find('dataFiles').iterfind('file'):
            dfile = DataFile( f_el.get('path'),
                                [log.mods[k.get('key')]
                                    for k in f_el.find('installingMods').iterfind('mod')])
            log.add_data_file(dfile)



    def full_path(self, data_file ):
        return path_join(self.sky.install_path, data_file.path)

    def verify_file(self, data_file):
        return path_exists(self.full_path(data_file))


# queries

def missing_files(nexus):
    verify = n.verify_file

    for df in nexus.mod_log.data_files.itervalues():
        if not verify(df):
            print [m.name for m in df.installing_mods], df.path


def unhandled_files(nexus, data_only = True):
    if data_only:
        root = nexus.sky.data_path
    else:
        root = nexus.sky.install_path
    root_len = len(nexus.sky.install_path)
    d_files = nexus.mod_log.data_files

    total_files = 0
    unmanaged_files = 0


    for (dirpath, dirnames, filenames) in os.walk(root):
        rel_pfx = dirpath[root_len:]
        for fnam in filenames:
            total_files += 1
            rel_name = path_join(rel_pfx, fnam)
            if rel_name.lower() not in d_files:
                unmanaged_files += 1
                yield rel_name

    print 'files: total:', total_files, 'unmanaged:', unmanaged_files


# Main

def run():
    n = Nexus()
    n.parse_install()
    # report
    print 'Found', len(n.mod_log.mods), 'mods'
    print 'Found', len(n.mod_log.data_files), 'files'

    for uf in unhandled_files(n):
        print uf


if __name__ == '__main__':
    run()
