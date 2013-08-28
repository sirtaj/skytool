#/usr/bin/env python
# vim:ts=4:sw=4:et:ff=unix

__doc__=\
'''Steam Workshop subscribed mods.

Format for SteamModList.txt:

    * of:
        lines of:
            esp name
            Mod name
            Unknown integer (always 1?)

'''

import os.path

from files import DumbModCollection, Mod, DataFile


class SteamWorkshopMods(DumbModCollection):
    SUBSCRIPTIONS_FILE = 'SteamModList.txt'

    def __init__(self, game):
        super(SteamWorkshopMods, self).__init__(game)
        self.subscriptions_path = os.path.join(game.user_data_path, self.SUBSCRIPTIONS_FILE)

    def parse_install(self):
        for (esp, name, subs_flag) in self.read_subscriptions():
            esp = os.path.join('Data', esp)
            bsa = esp[:-4] + '.bsa'

            # TODO Some of these fields don't make sense for Steam. What do we do with them?
            mod = Mod(name, esp, None, '1.0', None)
            self.add_mod(mod)
            self.add_data_file(DataFile(esp, [mod]))
            self.add_data_file(DataFile(bsa, [mod]))


    def read_subscriptions(self):
        '''Read subscriptions and generates (esp_name, mod_name, subscription int) tuples.
        '''
        esp_name = mod_name = None

        with open(self.subscriptions_path) as subs_fd:
            for ln in subs_fd.readlines():
                ln = ln.strip()
                if esp_name is None:
                    esp_name = ln
                elif mod_name is None:
                    mod_name = ln
                else:
                    yield (esp_name, mod_name, int(ln))
                    esp_name = mod_name = None


if __name__ == '__main__':
    pass
