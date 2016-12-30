from . import grid as grid

class Player(object):

    def __init__(self, unit, grid):
        self.unit = unit
        self.grid = grid
        self.discovered = list()
        self.winner = None

    def play(self, cell):
        if cell in self.discovered:
            return False
        if self.grid.cells[cell] == self.unit:
            return False
        if self.grid.cells[cell] != grid.Grid.EMPTY:
            self.discovered.append(cell)
            return False
        return self.grid.play(self.unit, cell)

    def is_winner(self):
        return self.grid.winner(self.unit)

    def display_grid(self):
        print("-------------")
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

