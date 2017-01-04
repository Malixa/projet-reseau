"""
	Ce module contient:
		La classe packetexit : gère la déconnection volontaire du client

"""
from .System import packet as packet

class PacketExit(packet.Packet):

#Envoi de la commande exit au serveur
    def send(self):
        data = "EXIT"
        self.server.send(data)
