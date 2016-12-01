"""
    Ce module contient:
        La classe Player: Represente un joueur capable d'interragir avec le jeu.
"""

from . import entity as entity
from . import game as game

class Player(entity.Entity):
    """
        Represente un joueur capable d'interragir avec
        le jeu.
    """

    def __init__(self, unit, client):
        entity.Entity.__init__(self, client)
        self.unit = unit
        self.score = 0

    def play(self, cell):
        """
            Permet au joueur de jouer un coup
            sur la cellule cell.
            Retourne True si le joueur a pu jouer,
            False sinon.
        """
        if game.Game.Instance.is_ready() is False or self is not game.Game.Instance.get_current_player():
            return False
        return game.Game.Instance.grid.place(self.unit, cell)
        