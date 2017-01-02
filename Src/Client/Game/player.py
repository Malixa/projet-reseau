from . import grid as grid

class Player(object):

    def __init__(self, unit, gri):
        self.unit = unit
        self.grid = gri
        self.discovered = list()
        self.winner = None
        print("Vous etes le joueur "+str(unit)+". Symbole: "+grid.Grid.SYMBOLS[self.unit])


    def can_play(self, cell): 
        if cell in self.discovered:
            return False
        if self.grid.cells[cell] == self.unit:
            return False
        if self.grid.can_play(self.unit, cell) is False:
            return False
        return True

    def discover(self, cell):
        self.discovered.append(cell)

    def play(self, cell):
        if cell in self.discovered:
            return False
        if self.grid.cells[cell] == self.unit:
            return False
        if self.grid.can_play(self.unit, cell) is False:
            return False
        return self.grid.play(self.unit, cell)

    def is_winner(self):
        return self.grid.winner(self.unit)

    def display_grid(self):
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

