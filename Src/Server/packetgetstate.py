"""
    Ce module contient:
        La classe PacketGetState: Paquet gerant une demande de l'etat de la partie
"""

from System.packet import Packet
from packetstate import PacketState

class PacketGetState(Packet):
    """
        Paquet envoye par le client signalant au serveur qu'il
        doit envoyer l'etat courant du jeu
    """

    def run(self, ctx):
        state = PacketState(self.target, None)
        state.send()
