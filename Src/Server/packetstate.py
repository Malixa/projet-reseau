from System.packet import Packet
from Game.grid import Grid
from Game.game import Game
"""
    Module contenant le paquet state
"""

class PacketState(Packet):
    """
        Paquet contenant l'etat actuel du jeu
    """

    def __init__(self, target, args):
        super(PacketState, self).__init__(target, args)

    def send(self, to_all=False):
        msg = "STATE "+str(",").join(Game.Instance.grid.history)
        if to_all:
            self.target.shout(msg)
        self.target.send(msg)
