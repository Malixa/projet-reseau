"""
    Ce module contient:
        La classe PacketGetScore: Paquet gerant une demande de score
"""

from System.packet import Packet
from packetscore import PacketScore

class PacketGetScore(Packet):
    """
        Packet envoye par le client demandant au serveur de renvoyer le score des differents joueurs
    """

    def run(self, ctx):
        score = PacketScore(self.target, None)
        score.send()
