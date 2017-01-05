"""
	Ce module contient:
		La classe packetnop : gere l'implémentation de la commande nop permettant l'acquittement negatif de la part du serveur

"""

from .System import packet as packet


class PacketNop(packet.Packet):
	"""
	La commande nop permet l'acquittement negatif de la part du serveur
	Refus d'execution de la commande
	"""

	def run(self, ctx):
		pass
