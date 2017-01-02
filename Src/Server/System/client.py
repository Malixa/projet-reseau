"""
    Ce module contient:
    La classe Client: Represente un client connecte au serveur
"""

class Client(object):
    """
        Represente un client connecte au serveur.

        Abstraction de socket.
    """

    def __init__(self, server, socket, ip):
        self.server = server
        self.socket = socket
        self.ip_address = ip


    def fileno(self):
        """
            fileno:
            Permet d'utiliser le client avec select
        """
        return self.socket.fileno()


    def receive(self):
        """
            Recupere les informations envoyee par le client.

            Convertit les bytes en string et le retourne

            @return Donnees envoyees par le Client
        """
        data = self.socket.recv(50)
        data = data.decode("utf-8") # COnversion des bytes en string
        data = data.replace("#", "") #Suppression des caracteres de remplissage
        return data.replace("\n", "") #Suppression d'un eventuel retour a la ligne

    def send(self, data):
        """
            Envoie un string sur le socket.
        """
        #On ajoute des caracteres blancs pour remplir le buffer
        #et eviter la collision de deux paquets
        while len(data) < 50:
            data = data + "#"
        data = data.encode("utf-8")
        self.socket.send(data)

    def shout(self, data):
        """
            Envoie un string a tout les autres clients
        """
        self.server.send_all(data, self)


    def disconnect(self):
        """
            Deconnecte le client de son serveur
        """
        self.server.remove_client(self)
        self.socket.close()
 