"""
    Ce module contient:
        La classe PacketDisconnect: Paquet communiquant une deconnexion
"""

import System.packet as packet

class PacketDisconnected(packet.Packet):
    """
        Paquet indiquant a son recepteur que l'un des joueurs
        s'est deconnecte
    """
    def __init__(self, target, args):
        super(PacketDisconnected, self).__init__(target, args)
        self.other_ip = args[0][0]

    def send(self):
        msg = "DISCONNECTED "+self.other_ip
        self.target.send(msg)
