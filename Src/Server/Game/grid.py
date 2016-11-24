class Grid:

    def __init__(self):
        self.map = list()
        self.history = list()
        for i in range(0, 8):
            self.map.append(0)

    def play(self, player, cell):
        if self.map[cell] == 0:
            self.map[cell] = player.unit
            self.history.append(cell)
            return True
        return False

    def won(self, player):
        for y in range(3): 
            if self.map[y*3] == player.unit and self.map[y*3+1] == player.unit and self.map[y*3+2] == player.unit:
                    return True
        for x in range(3): 
            if self.map[x] == player.unit and self.map[3+x] == player.unit and self.map[6+x] == player.unit:
                    return True
        if self.map[0] == player.unit and self.map[4] == player.unit and self.map[8] == player.unit:
            return True
        if self.map[2] == player.unit and self.map[4] == player.unit and self.map[6] == player.unit:
            return True
        return False
        
            
