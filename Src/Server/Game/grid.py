"""
    Ce module contient:
        La classe Grid: Represente la grille en jeu.
"""

class Grid(object):
    """
        Represente la grille de jeu.
        Grille pouvant etre remplie par les deux joueurs
        successivement.
    """

    def __init__(self):
        self.map = list()
        self.history = list()
        # On simule le fait que le joueur 2 ai joue en dernier
        # On attend ainsi que le joueur 1 joue en premier
        self.lastplayer = 2
        for _ in range(0, 9):
            self.map.append(0)

    def place(self, unit, cell):
        """
            Place un symbole sur la grille.
            Retourne True si le coup a bien pu etre joue
            Retourne False sinon.
        """
        if cell < 0 or cell > 8:
            return False
        if self.map[cell] == 0:
            self.map[cell] = unit
            self.history.append(str(cell))
            self.lastplayer = unit
            return True
        return False

    def abort_turn(self, unit):
        """
            Indique a la grille que le joueur unit a passe son tour
        """
        self.lastplayer = unit
        self.history.append("-1")

    def won(self, unit):
        """
            Determine si le joueur player
            a gagne la partie.
            Retourne True si oui,
            False sinon
        """
        for col in range(3):
            if self.map[col*3] == unit and self.map[col*3+1] == unit and self.map[col*3+2] == unit:
                return True
        for line in range(3):
            if self.map[line] == unit and self.map[3+line] == unit and self.map[6+line] == unit:
                return True
        if self.map[0] == unit and self.map[4] == unit and self.map[8] == unit:
            return True
        if self.map[2] == unit and self.map[4] == unit and self.map[6] == unit:
            return True
        return False


