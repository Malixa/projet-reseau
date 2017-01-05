"""
	Ce module contient :
		La classe serveur : gère toute la connexion et l'échange avec le serveur
"""

import socket
from . import packetfactory as packetfactory

class Server(object):
	"""
		Le serveur représente le serveur de jeu côté client
	"""

    Instance = None

    @staticmethod
    def start():
        """
            Initialise une nouvelle instance de classe
        """
        Server.Instance = None
        Server.Instance = Server()

    def __init__(self):

        # Une ne rend possible l'instanciation que d'un seul Networker
        if Server.Instance != None:
            raise Exception("Une seule instance de Networker est possible.")

        self.socket = None

    def connect(self, address, port=6666):
		"""
			Connecte le client au serveur selon l'adresse et le port
		"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.socket.connect((address, port))

    def receive(self):
		"""
			Permet le reception des données textuelles et leur conversion
		"""
        data = self.socket.recv(50)
        data = data.decode("utf-8") # COnversion des bytes en string
        data = data.replace("#", "") #Suppression des caracteres de remplissage
        return data.replace("\n", "") #Suppression d'un eventuel retour a la ligne

    def send(self, data):
		"""
			Permet l'envoi des données textuelles et leur conversion
		"""
        #On ajoute des caracteres blancs pour remplir le buffer
        #et eviter la collision de deux paquets
        while len(data) < 50:
            data = data + "#"
        data = data.encode("utf-8")
        self.socket.send(data)

    def wait_packet(self):
		""" 
			Permet l'attente des données du serveur 
		"""
        data = self.receive()
        if len(data) == 0:
            data = "SHUTDOWN"

        packet = packetfactory.PacketFactory.examine_and_create(data, self)
        return packet

        
        
