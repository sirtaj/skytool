
import game as game_

if __name__ == '__main__':
    game = game_.Skyrim()
    master = game.plugins.get(game.MASTER_PLUGIN)
    print master
