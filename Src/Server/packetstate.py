from System.packet import Packet
from Game.grid import Grid
"""
    Module contenant le paquet state
"""

class PacketState(Packet):
    """
        Paquet contenant l'etat actuel du jeu
    """

    def __init__(self, target, args):
        if not isinstance(args[0], Grid):
            raise TypeError("args est une liste devant contenir une grille a l'index 0.")
        super(PacketState, self).__init__(target, args)
        self.grid = args[0]

    def send(self):
        msg = "STATE "+str(",").join(self.grid.history)
        self.target.send(msg)
