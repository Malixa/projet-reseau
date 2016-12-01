"""
    Ce module contient:
        La classe PacketConnect: Paquet communiquant a un joueur que c'est son tour de jouer
"""

import System.packet as packet

class PacketTurn(packet.Packet):
    """
        Paquet indiquant a un joueur que c'est a son tour de jouer
    """

    def send(self):
        msg = "TURN"
        self.target.send(msg)
    