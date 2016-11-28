from .player import Player
from .grid import Grid

"""
    Module contenant la classe Game
"""

class Game(object):
    """
        Classe gerant le deroulement d'une partie
        Singleton
    """

    Instance = None

    @staticmethod
    def restart():
        """
            Permet de lancer une nouvelle partie unique
        """
        Game.Instance = Game()

    def __init__(self):
        if not Game.Instance is None:
            raise Exception("Il ne peut y avoir qu'une seule instance de game a la fois.")

        self.players = list()
        self.players_registry = dict()
        self.observers = list()
        self.grid = Grid()
        self.is_full = False

    def get_player_with_client(self, client):
        """
            Renvoie le joueur
            possedant le client donne
            en parametre
        """
        for player in self.players:
            if player.client == client:
                return player

        return None

    def insert_entity(self, client):
        """
            Permet d'ajouter un nouveau joueur/observateur a la partie
            Si le joueur se reconnecte, on lui reaffecte ses donnes
        """
        for player in self.players:
            if player.client == client:
                print("Game: deja enregistre")
                return False

        for observer in self.observers:
            if observer.client == client:
                print("Game: deja enregistre")
                return False

        if client.ip_address[0] in self.players_registry:
            # Si le joueur n'est pas deja dans la liste de joueur (jeu local)
            if not self.players_registry[client.ip_address[0]] in self.players:
                print("Game: Retour de "+str(self.players_registry[client.ip_address[0]]))
                self.players.append(self.players_registry[client.ip_address[0]])
                return True

        if self.is_full is False:
            player = Player(len(self.players)+1, client)
            self.players_registry[client.ip_address[0]] = player
            self.players.append(player)
            if len(self.players) >= 2:
                self.is_full = True
            print("Game: ajout du joueur "+str(player))
            return True
        else:
            # TODO: implementer les observateurs
            pass

    def remove_entity(self, client):
        """
            Permet de supprimer un joueur/observateur de la partie
        """
        for player in self.players:
            if player.client == client:
                print("Game: "+str(player)+" quitte la partie")
                self.players.remove(player)
                return True

        for observer in self.observers:
            if observer.client == client:
                print("Game: "+str(player)+" quitte la partie")
                self.observers.remove(observer)
                return True

        return False

        