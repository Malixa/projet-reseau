"""
Ce module contient:
La classe packetdisconnect : gere la déconnection accidentelle 
ou volontaire du client

"""

from .System import packet as packet


class PacketDisconnected(packet.Packet):
	"""
	La commande disconnected informe les clients de la deconnection d'un joueur
	et renvoi l'ip de celui-ci
	"""

	def __init__(self, server, args):
		super(PacketDisconnected, self).__init__(server, args)
		self.other_ip = args[0]


	def run(self, ctx):
		"""
		Met en place les informations de déconnetion
		"""
		print("Le joueur possedant l'adresse ip " + str(self.other_ip) + " s'est deconnecte.")
		print("En attente de sa reconnexion...")
		print("S'il n'est pas de retour dans 3 minutes, le serveur sera relance.")


