"""
	Ce module contient:
		La classe packetexit : gère la déconnection volontaire du client

"""
from .System import packet as packet

class PacketExit(packet.Packet):

	"""
		La command eexit permet au client de se déconnecter du serveur
	"""
    def send(self):
		"""
			Envoi de la commande exit au serveur
		"""
        data = "EXIT"
        self.server.send(data)
