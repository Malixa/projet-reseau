from System.packet import Packet
from packetscore import PacketScore

"""
    Module contenant la class PacketGetScore
"""

class PacketGetScore(Packet):
    """
        Packet envoye par le client demandant au serveur de renvoyer le score des differents joueurs
    """

    def do(self, ctx):
        score = PacketScore(self.target, None)
        score.send()

