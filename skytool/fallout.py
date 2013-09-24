
'''Game and plugins for Fallout 3 and New Vegas.
'''

from game import Game, TimestampOrderedPluginRegistry

import os, os.path, re
from datetime import datetime

path_join = os.path.join

class FalloutNV(Game):
    REG_GAME_PATH = ("Software\\Bethesda Softworks\\FalloutNV", "Installed Path")
    USER_SUBPATH = "FalloutNV"
    MASTER_PLUGIN = "FalloutNV.esm"

    def get_plugins(self):
        return TimestampOrderedPluginRegistry(self)



##############

if __name__ == '__main__':
    game = Fallout()
    print game.name, "is installed in", game.install_path
    print game.user_data_path
    for (order, p) in enumerate(game.plugins):
        print "%02X" % order, p.name,":\t", p.active, p.exists()
