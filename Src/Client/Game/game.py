from . import player as player
from . import grid as grid


class Game(object):

    Instance = None

    @staticmethod
    def start(is_player=0):
        """
            Initialise une nouvelle instance de classe
        """
        Game.Instance = None
        Game.Instance = Game(is_player)

    def __init__(self, is_player):
        self.player = None
        self.grid = grid.Grid()
        self.won = False

        if is_player != 0:
            self.player = player.Player(is_player, self.grid)

    def update_grid(self, data):
        for i in range(len(data)):
            player_index = (i % 2) + 1
            self.grid.cells[data[i]] = player_index

    def display_grid(self):
        if self.player is None:
            self.grid.display()
        else:
            self.player.display_grid()

