"""
	Ce module contient:
		La classe packetconnect : gère l'implémentation de la commande connect permettant la connexion du client

"""

from .System import packet as packet

class PacketConnect(packet.Packet):

#envoie de la commande connect au serveur
    def send(self):
        data = "CONNECT"
        self.server.send(data)
