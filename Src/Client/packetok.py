"""
	Ce module contient:
		La classe packetok : gère l'implémentation de la commande ok permettant l'acquittement de la part du serveur

"""

from .System import packet as packet


class PacketOk(packet.Packet):

    def run(self, ctx):
        pass
