
'''Core TES/GameBryo game and plugin access.
'''

import os, os.path, re, weakref
from datetime import datetime

path_join = os.path.join


class Game:
    def __init__(self, name = None):
        self.name = name or self.__class__.__name__
        self.install_path = self.get_game_path()
        self.data_path = self.install_path + "Data"
        self.user_data_path = self.get_user_data_path()
        self.plugins = self.get_plugins()

    def get_game_path(self, key = None):
        import _winreg

        if key is None:
            key = self.REG_GAME_PATH
        with _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, key[0]) as reg_key:
            return _winreg.QueryValueEx(reg_key, key[1])[0]

    def get_user_data_path(self):
        return path_join(os.getenv("LOCALAPPDATA"), self.USER_SUBPATH)

    def get_plugins(self):
        raise NotImplementedError



class PluginRegistry(object):
    '''Represents ESP/ESP plugins registered and enabled with the game.

    Alows reading and writing of the load order.

    Currently this is implemented for Skyrim (new style loadorder.txt) only.


    Sources of info:
        PT plugins.txt
        LO loadorder.txt
        FS skyrim Data dir (*.esp, *.esm)
        RU Runtime plugin registry

        When in FS and not elsewhere, add
        when not in FS but present elsewhere, remove internal

        Do we maintain a loadorder cache?

        () == not present

        PT LO FS (RU)       add to RU
        PT LO (FS) (RU)     remove from lo, pt
        PT LO (FS)  RU      remove from lo, ru

        PT (LO) FS (RU)     add to RU, LO (end?)
        PT (LO) FS  RU      add to LO (end?)
        PT (LO) (FS) (RU)   remove from PT
        PT (LO) (FS)  RU    add to PT, LO

        (PT) LO FS (RU)     add to PT, RU
        (PT) LO FS  RU      add to PT
        (PT) LO (FS) (RU)
        (PT) LO (FS)  RU

        (PT) (LO) FS (RU)
        (PT) (LO) FS  RU
        (PT) (LO) (FS) (RU)
        (PT) (LO) (FS)  RU

    '''
    def __init__(self, game):
        self.game = game
        self.by_name = {}  # plugin name -> Plugin
        self.by_order = [] # INCLUDES game master(s)
        self.modified_date = None

        self.dirty_order = False
        self.dirty_active = False

        self.plugins_txt_path = path_join(game.user_data_path, self.PLUGINS_FILE)

        # activate
        self.read_load_order()
        self.read_active()

    PLUGINS_FILE = "plugins.txt"

    def get(self, name):
        return self.by_name.get(name)

    def add_plugin(self, plugin):
        plugin.registry = weakref.ref(self)
        self.by_name[plugin.name] = plugin
        self.by_order.append(plugin)

    # Load Order
    def read_load_order(self):
        '''Must be overridden to populate current load order.
        '''
        raise NotImplementedError

    def write_load_order(self):
        raise NotImplementedError

    # Active
    def read_active(self):
        '''Must return currently active list.
        '''
        raise NotImplementedError

    def write_active(self):
        raise NotImplementedError

    # Filesystem

    def get_plugin_files(self):
        for fname in os.listdir(self.game.data_path):
            loname = fname.lower()
            if loname.endswith(".esp") or loname.endswith(".esm"):
                yield fname

    # Queries

    def __iter__(self):
        return iter(self.by_order)

    def iterate_order(self):
        '''Generates (index, load order (or None), plugin obj) tuples.
        '''

        next_order = iter(range(len(self.by_order))).next

        for index, plugin in enumerate(self.by_order):
            order = next_order() if plugin.active else None
            yield (index, order, plugin)

    # Changes
    def sync(self, force = False):
        '''Update game's current state to match our internal state.
        '''
        if force or self.dirty_order:
            self.write_load_order()

        if force or self.dirty_active:
            self.write_active()

        self.dirty_order = False
        seld.dirty_active = False


class Plugin(object):
    def __init__(self, game, name, registered, active):
        self.game = game
        self.name = name
        self.full_path = path_join(game.data_path, name)
        self.registered = registered
        self.active = active

    generated = False

    def __repr__(self):
        return "<Plugin %s>" % (repr(self.name),)

    ### Query

    def order(self):
        return self.game.plugins.by_order.find(self)

    def is_master(self):
        raise NotImplementedError

    def exists(self):
        try:
            os.stat(self.full_path)
            return True
        except OSError:
            return False

    def modified_date(self):
        return datetime.fromtimestamp(os.path.getmtime(self.full_path))

    ####

    def open(self, mode='rb'):
        return open(self.full_path, mode)


    def set_name(self, new_name):
        # validate name for structure and uniqueness
        if not plugin_name_match(new_name):
            raise ValueError, "Invalid plugin name"

        plugins = self.registry()

        for plugin in plugins:
            if plugin.name == new_name:
                raise ValueError, "Duplicate plugin name"

        # Change physical name
        old_path = self.full_path
        new_path = path_join(self.game.data_path, new_name)

        os.rename(self.old_path, self.new_path)

        # Update registry
        del registry.by_name[self.name]
        self.name = new_name
        registry.by_name[new_name] = self
        registry.save()


    def set_active(self, active = True):
        if active == self.active:
            return

        self.active = active
        registry.sync(True)


plugin_name_match = re.compile('^[\\w\d\\s_\\.-]+\\.[eE][sS][pPmM]$').match


class Skyrim(Game):
    REG_GAME_PATH = ("Software\\Bethesda Softworks\\Skyrim", "Installed Path")
    USER_SUBPATH = "Skyrim"
    MASTER_PLUGIN = "Skyrim.esm"

    def get_plugins(self):
        return SkyrimPluginRegistry(self)


#########

class SkyrimPluginRegistry(PluginRegistry):
    '''New textfile-based load order for Skyrim.
    '''
    def __init__(self, game):
        print "GAME:", game
        self.loadorder_path = path_join(game.user_data_path, self.ORDER_FILE)

        super(SkyrimPluginRegistry, self).__init__(game)

    ORDER_FILE = "loadorder.txt"

    def read_load_order(self):
        with open(self.loadorder_path) as plugf:
            for order_idx, plugin_name in enumerate(plugf.readlines()):
                plugin_name = plugin_name.strip()

                if not plugin_name or plugin_name.startswith('#'):
                    # blank lines and comments.
                    continue

                plugin = Plugin( game = self.game,
                                name = plugin_name,
                                registered = True,
                                active = (plugin_name == self.game.MASTER_PLUGIN))
                self.add_plugin(plugin)


    def write_load_order(self):
        '''Write out loadorder.txt.
        '''
        new_file = self.loadorder_path + ".new"
        with open(new_file, "w") as out:
            for p in self.by_order:
                out.write("%s\n" % (p.name,))


    def read_active(self):
        '''Reads plugins.txt.
        '''
        with open(self.plugins_txt_path) as plugf:
            for order_idx, plugin_name in enumerate(plugf.readlines()):
                plugin_name = plugin_name.strip()
                plugin = self.get(plugin_name)
                if plugin is not None:
                    plugin.active = True
                else:
                    plugin = Plugin( game = self.game,
                                    name = plugin_name,
                                    registered = True,
                                    active = True)
                    self.add_plugin(plugin)


    def write_active(self):
        '''Write out plugins.txt.
        '''
        new_file = self.plugins_txt_path + ".new"
        with open(new_file, "w") as out:
            for p in self.by_order:
                if p.active and p.name != game.MASTER_PLUGIN and p.exists():
                    out.write("%s\n" % (p.name,))


class TimestampOrderedPluginRegistry(PluginRegistry):
    '''Modified-timestamp-based load order, for games before Skyrim.
    '''
    def read_load_order(self):
        plugins = (Plugin(self.game,
                        fname,
                        registered  = True,
                        active      = False)
            for fname in self.get_plugin_files())

        sorted_order = (s_plugin for (dt, s_plugin) in
                            sorted((p.modified_date(), p)
                                        for p in plugins))

        for plugin in sorted_order:
            self.add_plugin(plugin)

    def write_load_order(self):
        raise NotImplementedError


    def read_active(self):
        '''Reads plugins.txt.
        '''
        with open(self.plugins_txt_path) as plugf:
            for order_idx, plugin_name in enumerate(plugf.readlines()):
                plugin_name = plugin_name.strip()

                if not plugin_name or plugin_name.startswith('#'):
                    # blank lines and comments.
                    continue

                plugin = self.get(plugin_name)
                if plugin is not None:
                    plugin.active = True
                else:
                    plugin = Plugin( game = self.game,
                                    name = plugin_name,
                                    registered = True,
                                    active = True)
                    self.add_plugin(plugin)

    def write_active(self):
        '''Write out plugins.txt.
        '''
        names = sorted(p.name for p in self.by_order
                        if p.active
                            and p.name != game.MASTER_PLUGIN
                            and p.exists())

        new_file = self.plugins_txt_path + ".new"

        with open(new_file, "w") as out:
            out.write( "# This file is used to tell %s which data files to load.\n\n"
                        % self.game.name)

            for name in names:
                out.write("%s\n" % (name,))

        # TODO replace old file with new one on success.



#####################
### Specific plugins


class DynamicPlugin(Plugin):
    generated = True


class SkyProcPatch(DynamicPlugin):
    pass


class PluginASIS(SkyProcPatch):
    RUNNER_PATH = "SkyProc Patchers\\ASIS"
    JAR_EXE = "ASIS.jar"

    def update(self):
        run_path = path_join(game.data_path, self.RUNNER_PATH)
        old_cwd = os.getcwd()
        try:
            os.chdir(run_path)
        finally:
            os.chdir(old_cwd)


class PluginBashedPatch(DynamicPlugin):
    pass


##############

if __name__ == '__main__':
    game = Skyrim()
    print game.name, "is installed in", game.install_path
    print game.user_data_path
    for (order, p) in enumerate(game.plugins):
        print "%02X" % order, p.name,":\t", p.active, p.exists()
