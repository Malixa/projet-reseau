"""
	Ce module contient:
		La classe packetnop : gère l'implémentation de la commande nop permettant l'acquittement négatif de la part du serveur

"""

from .System import packet as packet


class PacketNop(packet.Packet):

    def run(self, ctx):
        pass
