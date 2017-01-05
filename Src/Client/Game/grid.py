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
    EMPTY = 0
    NB_CELLS = 9
    SYMBOLS = [' ', 'O', 'X']
    J1 = 1
    J2 = 2


    def __init__(self):
        self.cells = []
        for _ in range(Grid.NB_CELLS):
            self.cells.append(Grid.EMPTY)

    def can_play(self, player, cellnum):
        """
            Definie si la case jouee est comprise dans la grille
        """
        if cellnum < 0 or cellnum >= Grid.NB_CELLS:
            return False
        return True

    def play(self, player, cellnum):
        """
            Definie si la case jouee est viable ou non 
        """
        if self.can_play(player, cellnum) is False or self.cells[cellnum] != Grid.EMPTY: 
            return False
        self.cells[cellnum] = player
        return True

    def display(self):
        """
            Affichage de la grille
        """
        for row in range(3):
            out = "|"
            for col in range(3):
                out = out + Grid.SYMBOLS[self.cells[row*3+col]] + "|"
            print(out)


    def winner(self, player):
        """
            Test si 'player' a gagne la partie
        """
        assert(player == Grid.J1 or player == Grid.J2)
        # horizontal line
        for vert in range(3):
            if self.cells[vert*3] == player and self.cells[vert*3+1] == player and self.cells[vert*3+2] == player:
                return True
        # vertical line
        for hor in range(3):
            if self.cells[hor] == player and self.cells[3+hor] == player and self.cells[6+hor] == player:
                return True
        #diagonals :
        if self.cells[0] == player and self.cells[4] == player and self.cells[8] == player:
            return True
        if self.cells[2] == player and self.cells[4] == player and self.cells[6] == player:
            return True
        return False


    def game_over(self):
        """
            Retourne l'etat du jeu
            -1 si le jeu n'est pas termine
            EMPTY si DRAW
            J1 si le joueur 1 a gagne
            J2 si le joueur 2 a gagne
        """
        if self.winner(Grid.J1):
            return Grid.J1
        if self.winner(Grid.J2):
            return Grid.J2
        for i in range(Grid.NB_CELLS):
            if self.cells[i] == Grid.EMPTY:
                return -1
        return 0
