
# Skyrim mod file utilities
# Sirtaj Singh Kang

import os, os.path
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


class Skyrim(Game):
    REG_GAME_PATH = ("Software\\Bethesda Softworks\\Skyrim", "Installed Path")
    USER_SUBPATH = "Skyrim"
    MASTER_PLUGIN = "Skyrim.esm"

    def get_plugins(self):
        return Plugins(self)


#########

class Plugins:
    '''Represents ESP/ESP plugins registered and enabled with the game.

    Alows reading and writing of the load order.

    Currently this is implemented for Skyrim (new style loadorder.txt) only.
    '''
    def __init__(self, game):
        self.game = game
        self.loadorder_path = path_join(game.user_data_path, self.ORDER_FILE)
        self.plugins_txt_path = path_join(game.user_data_path, self.PLUGINS_FILE)
        self.by_name = {}
        self.by_order = [] # INCLUDES game master

        self.read_load_order()
        self.read_active_plugins()

    PLUGINS_FILE = "plugins.txt"
    ORDER_FILE = "loadorder.txt"

    def get(self, name):
        return self.by_name.get(name)

    def read_load_order(self):
        with open(self.loadorder_path) as plugf:
            for order_idx, plugin_name in enumerate(plugf.readlines()):
                plugin_name = plugin_name.strip()
                plugin = Plugin( game = self.game, name = plugin_name,
                        registered = True,
                        active = (plugin_name == self.game.MASTER_PLUGIN))

                self.by_name[plugin_name] = plugin
                self.by_order.append(plugin)

    def read_active_plugins(self):
        with open(self.plugins_txt_path) as plugf:
            for order_idx, plugin_name in enumerate(plugf.readlines()):
                plugin_name = plugin_name.strip()
                plugin = self.get(plugin_name)
                if plugin is not None:
                    plugin.active = True
                else:
                    plugin = Plugin( game = self.game, name = plugin_name,
                            registered = True, active = True)
                    self.by_name[plugin_name] = plugin
                    self.by_order.append(plugin)

    def get_plugin_files(self):
        for fname in os.listdir(self.game.data_path):
            loname = fname.lower()
            if loname.endswith(".esp") or loname.endswith(".esm"):
                yield fname

    def sync_order(self):
        '''Write out plugins.txt and loadorder.txt
        '''
        # Order
        new_file = self.loadorder_path + ".new"
        with open(new_file, "w") as out:
            for p in self.by_order:
                out.write("%s\n" % (p.name,))
        # Active
        new_file = self.plugins_txt_path + ".new"
        with open(new_file, "w") as out:
            for p in self.by_order:
                if p.active and p.name != game.MASTER_PLUGIN and p.exists():
                    out.write("%s\n" % (p.name,))

    def __iter__(self):
        return iter(self.by_order)


########### ES* Files

class Plugin:
    def __init__(self, game, name, registered, active):
        self.game = game
        self.name = name
        self.full_path = path_join(game.data_path, name)
        self.registered = registered
        self.active = active

    generated = False

    def __repr__(self):
        return "<Plugin %s>" % (repr(self.name),)


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

    def open(self, mode='rb'):
        return open(self.full_path, mode)
        
### Specific plugins

class PluginASIS(Plugin):
    generated = True
    RUNNER_PATH = "SkyProc Patchers\\ASIS"
    JAR_EXE = "ASIS.jar"

    def update(self):
        run_path = path_join(game.data_path, self.RUNNER_PATH)
        old_cwd = os.getcwd()
        try:
            os.chdir(run_path)
        finally:
            os.chdir(old_cwd)



##############
if __name__ == '__main__':
    game = Skyrim()
    print game.name, "is installed in", game.install_path
    print game.user_data_path
    for (order, p) in enumerate(game.plugins):
        print "%02X" % order, p.name,":\t", p.active, p.exists()
