

import out
import game as game_
import esp

if __name__ == '__main__':
    game = game_.Skyrim()
    p = game.plugins.get("LevelersTower.esm")
    esp.test_read(p)
