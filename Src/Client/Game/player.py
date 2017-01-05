"""
	Ce module contient :
		La classe player : represente l'unique joueur cote client
"""
from . import grid as grid

class Player(object):
    """
        Represente le joueur.
    """

    def __init__(self, unit, gri):
        self.unit = unit
        self.grid = gri
        self.discovered = list()
		#liste de decouverte des coups adverses
        self.winner = None
        print("Vous etes le joueur "+str(unit)+". Symbole: "+grid.Grid.SYMBOLS[self.unit])


    def can_play(self, cell):
        """
            Retourne true si la case est jouable false sinon
        """
        if cell in self.discovered:
            return False
        if self.grid.cells[cell] == self.unit:
            return False
        if self.grid.can_play(self.unit, cell) is False:
            return False
        return True

    def discover(self, cell):
        """
            Ajoute une case a la decouverte du joueur (liste des cases jouees par l'ennemi)
        """
        self.discovered.append(cell)

    def play(self, cell):
        """
            Permet au joueur de jouer un coup
        """
        if cell in self.discovered:
            return False
        if self.grid.cells[cell] == self.unit:
            return False
        if self.grid.can_play(self.unit, cell) is False:
            return False
        return self.grid.play(self.unit, cell)

    def is_winner(self):
        """
            Defini le gagnant
        """
        return self.grid.winner(self.unit)

    def display_grid(self):
        """
            Permet l'affichage de la grille
        """
        for row in range(3):
            out = "|"
            for col in range(3):
                if self.grid.cells[row*3+col] == grid.Grid.EMPTY or self.grid.cells[row*3+col] == self.unit:
                    out = out + grid.Grid.SYMBOLS[self.grid.cells[row*3+col]] + "|"
                elif row*3+col in self.discovered:
                    out = out + grid.Grid.SYMBOLS[(self.unit+2)%2+1] + "|"
                else:
                    out = out + grid.Grid.SYMBOLS[grid.Grid.EMPTY] + "|"
            print(out)

