import socket
import select

class Networker:

    Instance = None

    def __init__(self):

        # Une ne rend possible l'instanciation que d'un seul Networker
        if Networker.Instance != None:
            raise Error("Une seule instance de Networker est possible.")
        Networker.Instance = self

        # Liste des sockets des clients connectés
        self.clients = list()

        # 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('', 6666))
        pass

    """
        listen:
        Lance l'écoute du socket de connexion du serveur 
    """
    def listen(self):
        self.socket.listen(6);

    """
        watch:
        Gère l'écoute des différents sockets du serveur
        @return la liste des sockets clients ayant envoyé des 
        données 
    """
    def watch(self):
        socks = list(clients)
        socks.append(self.socket)
        changes = select.select(socks, list(), list())[0]

        