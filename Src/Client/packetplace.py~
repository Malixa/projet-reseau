"""
	Ce module contient:
		La classe packetplace : gère l'implémentation de la fonctione place permettant le placement des pions sur la grille

"""

from .System import packet as packet

class PacketPlace(packet.Packet):

	"""
		La commande place permet au joueur de demander le placement d'un pion
		sur la grille en une case 
	"""
    def send(self):
		"""
			Permet l'envoi au serveur de la commande place plus ses arguments
		"""
        place = self.args[0]
        data = "PLACE "+str(place)
        self.server.send(data)
