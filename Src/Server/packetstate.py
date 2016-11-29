"""
    Ce module contient:
        La classe PacketConnect: Paquet communiquant l'etat du jeu
"""

from System.packet import Packet
from Game.game import Game

class PacketState(Packet):
    """
        Paquet contenant l'etat actuel du jeu
    """

    def __init__(self, target, args):
        super(PacketState, self).__init__(target, args)

    def send(self):
        msg = "STATE "+str(",").join(Game.Instance.grid.history)
        self.target.send(msg)
