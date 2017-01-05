"""
Ce module contient:
La classe packetexit : gere la deconnexion volontaire du client

"""
from .System import packet as packet

class PacketExit(packet.Packet):
	"""
	La commande exit permet au client de se deconnecter du serveur
	"""

	def send(self):
		"""
		Envoi de la commande exit au serveur
		"""
		data = "EXIT"
		self.server.send(data)
