"""
    Ce module contient:
        La classe PacketGetState: Paquet gerant une demande de l'etat de la partie
"""

import System.packet as packet
import packetstate

class PacketGetState(packet.Packet):
    """
        Paquet envoye par le client signalant au serveur qu'il
        doit envoyer l'etat courant du jeu
    """

    def run(self, ctx):
        state = packetstate.PacketState(self.target, None)
        state.send()
