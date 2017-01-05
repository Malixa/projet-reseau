"""
	Ce module contient:
		La classe packetconnect : gère l'implémentation de la commande connect permettant la connexion du client

"""

from .System import packet as packet

class PacketConnect(packet.Packet):

	"""
		La commande connect permet au client de se connecter au serveur
	"""
    def send(self):
	"""
		envoie de la commande connect au serveur
	"""
        data = "CONNECT"
        self.server.send(data)
