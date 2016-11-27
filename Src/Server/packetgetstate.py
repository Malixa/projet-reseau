from System.packet import Packet
from packetstate import PacketState

"""
       Paquet contenant le paquet 'GetState'
"""

class PacketGetState(Packet):
    """
        Paquet envoye par le client signalant au serveur qu'il
        doit envoyer l'etat courant du jeu
    """

    def do(self, ctx):
        state = PacketState(self.target, [ctx['grid']])
        state.send()



