"""
	Ce module contient:
		La classe packetok : gere l'implementation de la commande ok
		permettant l'acquittement de la part du serveur

"""

from .System import packet as packet


class PacketOk(packet.Packet):
	"""
	La commande ok permet l'acquittement du serveur a une commande du client
	"""

	def run(self, ctx):
		pass
