"""
    Ce module contient:
        La classe PacketConnect: Paquet communiquant l'etat du jeu
"""

from .System import packet as packet
from .Game import game as game

class PacketState(packet.Packet):
    """
        Paquet contenant l'etat actuel du jeu
    """

    def __init__(self, target, args):
        super(PacketState, self).__init__(target, args)

    def send(self):
        msg = "STATE "+str(",").join(game.Game.Instance.grid.history)
        self.target.send(msg)
