"""
	Ce module contient:
		La classe packetshutdown : gere l'arret serveur

"""

from .System import packet as packet

from . import client as client

class PacketShutdown(packet.Packet):
	"""
		La commande shutdown informe le client que le serveur s'est arrete
		et deconnecte le client
	"""

	def run(self, ctx):
		"""
			deconnecte le client en cas d'arret du serveur
		"""
		client.Client.stop() #arret du client


