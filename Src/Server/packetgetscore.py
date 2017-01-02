"""
    Ce module contient:
        La classe PacketGetScore: Paquet gerant une demande de score
"""
from .System import packet as packet
from . import packetscore

class PacketGetScore(packet.Packet):
    """
        Packet envoye par le client demandant au serveur de renvoyer le score des differents joueurs
    """

    def run(self, ctx):
        score = packetscore.PacketScore(self.target, None)
        score.send()
