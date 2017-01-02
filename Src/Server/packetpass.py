"""
    Ce module contient:
        La classe PacketPass: Paquet communiquant au joueur qu'il passe son tour
"""
from .System import packet as packet

class PacketPass(packet.Packet):
    """
        Paquet indiquant a son recepteur qu'il doit passer son tour
    """

    def send(self):
        msg = "PASS"
        self.target.send(msg)
