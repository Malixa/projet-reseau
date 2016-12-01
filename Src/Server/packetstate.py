"""
    Ce module contient:
        La classe PacketConnect: Paquet communiquant l'etat du jeu
"""

import System.packet as packet
import Game.game as game

class PacketState(packet.Packet):
    """
        Paquet contenant l'etat actuel du jeu
    """

    def __init__(self, target, args):
        super(PacketState, self).__init__(target, args)

    def send(self):
        msg = "STATE "+str(",").join(game.Game.Instance.grid.history)
        self.target.send(msg)
