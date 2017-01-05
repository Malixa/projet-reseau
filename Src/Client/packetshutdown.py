"""
	Ce module contient:
		La classe packetshutdown : gère le crash serveur

"""

from .System import packet as packet

from . import client as client

class PacketShutdown(packet.Packet):

	"""
		La commande shutdown informe le client que le serveur c'est arreté
		et déconnecte le client
	"""

    def run(self, ctx):
		"""
			déconnecte le client en cas d'arret du serveur
		"""
        client.Client.stop() #arret du client


