

import game as game_
import estest
from esp import Record, Group

def test_read(plugin):
    with plugin.open() as fd:
        while True:
            rec = Record.read_from(fd)
            if rec is None: break

            #print "=== %s: size %s ===" % (rec, rec.record_size())
            flag_list = rec.flag_list()
            #if flag_list:
            #    print "flags:", ", ".join(flag_list)
            #for f in rec.read_subrecords(fd):
            #    print "F:", f.type, repr(f.read_data(fd))
            if isinstance(rec, Group):
                rec.seek_data(fd)
                continue
            else:
                rec.skip(fd)

if __name__ == '__main__':
    game = game_.Skyrim()
    p = game.plugins.get("Skyrim.esm")
    test_read(p)
