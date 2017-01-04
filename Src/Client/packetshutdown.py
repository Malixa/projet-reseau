"""
	Ce module contient:
		La classe packetshutdown : gère le crash serveur

"""

from .System import packet as packet

from . import client as client

class PacketShutdown(packet.Packet):

#déconnecte le client en cas d'arret du serveur
    def run(self, ctx):
        client.Client.stop() #arret du client


