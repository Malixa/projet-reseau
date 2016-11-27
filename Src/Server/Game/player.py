from .entity import Entity

class Player(Entity):

    def __init__(self, unit, client):
        Entity.__init__(self, client)
        self.unit = unit
        self.score = 0
        