"""
    Ce module contient:
        La classe Player: Represente un joueur capable d'interragir avec le jeu.
"""

from .entity import Entity
from .game import Game

class Player(Entity):
    """
        Represente un joueur capable d'interragir avec
        le jeu.
    """

    def __init__(self, unit, client):
        Entity.__init__(self, client)
        self.unit = unit
        self.score = 0

    def play(self, cell):
        """
            Permet au joueur de jouer un coup
            sur la cellule cell.
            Retourne True si le joueur a pu jouer,
            False sinon.
        """
        if Game.Instance.is_ready() is False or self is not Game.Instance.get_current_player():
            return False
        return Game.Instance.grid.place(self.unit, cell)


        