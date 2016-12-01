"""
    Ce module contient:
    La classe Networker: Gere plusieurs connexions a diffrents clients
"""

import socket
import select
from .client import Client

class Networker(object):
    """
        Permet de gerer la connexion de plusieurs
        clients.
        Singleton
    """

    Instance = None

    def __init__(self):

        # Une ne rend possible l'instanciation que d'un seul Networker
        if Networker.Instance != None:
            raise Exception("Une seule instance de Networker est possible.")
        Networker.Instance = self

        # Liste des sockets des clients connectes
        self.clients = list()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('', 6666))


    def remove_client(self, client):
        """
            Permet de supprimer un client de la liste des clients
        """
        self.clients.remove(client)
        #print("removing:" + str(client))


    def listen(self):
        """
            Lance l'ecoute du socket de connexion du serveur
        """
        self.socket.listen(6)

    def send_all(self, data, sender=None):
        """
            Envoie le string data
            a tout les clients
        """
        for client in self.clients:
            if client == sender:
                continue
            client.send(data)

    def watch(self):
        """
            Gere l'ecoute des differents sockets du serveur
            @return la liste des sockets clients ayant envoye des
            donnees
        """
        ret = list()
        changes = list(self.clients)
        changes.append(self.socket)
        changes = select.select(changes, list(), list())[0]
        for change in changes:
            if change == self.socket:
                data = change.accept()
                # Creation d'un nouveau client
                cli = Client(self, data[0], data[1])
                self.clients.append(cli)
                #ret.append(client)
            else:
                ret.append(change)

        return ret
        