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
        ret = list()
        changes = list(self.clients)
        changes.append(self.socket)
        changes = select.select(changes, list(), list())[0] #TODO: va lever une erreur, méthode à implémenter dans Client
        for change in changes: 
            if change == self.socket:
                data = change.accept()
                # Création d'un nouveau client 
                client = Client(data[0], data[1][0])
                self.clients.append(client)
                ret.append(client)
                # gérer une nouvelle connexion
            else: 
                ret.append(change)
        
        return ret

        