"""
	Ce module contient:
		La classe packetgetstate : gère l'implémentation de la commande getstate permettant l'envoi de la commande getstate au serveur

"""

from .System import packet as packet

from .Game import game as game

class PacketGetState(packet.Packet):

#Envoi de la commande GETSTATE au serveur
    def send(self):
        data = "GETSTATE"
        self.server.send(data)

        state = self.server.wait_packet()
        state.run(None)
