from . import player as player
from . import grid as grid


class Game(object):

    Instance = None

    MODE_PLAYER = "player"
    MODE_OBSERVER = "observer"

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
        self.mode = Game.MODE_OBSERVER

        if is_player != 0:
            self.player = player.Player(is_player, self.grid)
            self.mode = Game.MODE_PLAYER
            
    def update_grid(self, data):
        for i in range(len(data)):
            if data[i] == -1:
                continue
            player_index = (i % 2) + 1
            self.grid.cells[data[i]] = player_index

    def check_for_winner(self):
        """
            En mode observer, determine si il y a un gagnant et retourne son symbole, sinon None
        """
        # En mode observer le client ne recoit pas de end. C'est a lui meme de determiner de la fin de la partie
        if self.mode == Game.MODE_OBSERVER:
            if self.grid.winner(grid.Grid.J1):
                return grid.Grid.SYMBOLS[grid.Grid.J1]
            elif self.grid.winner(grid.Grid.J2):
                return grid.Grid.SYMBOLS[grid.Grid.J2]
            else:
                return None
        else:
            raise Exception("Unable to call this method in MODE_PLAYER")


    def display_grid(self):
        if self.mode == Game.MODE_OBSERVER:
            self.grid.display()
        else:
            self.player.display_grid()

