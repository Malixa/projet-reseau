"""
    Ce module contient:
        La classe Game: Gere le deroulement d'une partie
"""

from .entity import Entity
from .player import Player
from .grid import Grid
from .roles import Roles

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
        self.playing = 0 #Le joueur 1 commence
        self.players_number = 0
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

    def get_current_player(self):
        """
            Retourne le joueur dont c'est le tour de jouer
        """
        return self.players[self.playing]

    def is_ready(self):
        """
            Retourne si les joueurs peuvent jouer
        """
        if self.players_number < 2:
            return False
        return True

    def turn(self):
        """
            Lance un nouveau tour
        """
        self.playing = (self.playing + 1) % 2

    def insert_entity(self, client):
        """
            Permet d'ajouter un nouveau joueur/observateur a la partie
            Si le joueur se reconnecte, on lui reaffecte ses donnes
        """
        for player in self.players:
            if player is not None and player.client == client:
                print("Game: deja enregistre")
                return None

        for observer in self.observers:
            if observer.client == client:
                print("Game: deja enregistre")
                return None

        if client.ip_address[0] in self.players_registry:
            # Si le joueur n'est pas deja dans la liste de joueur (jeu local)
            if not self.players_registry[client.ip_address[0]] in self.players:
                print("Game: Retour de "+str(self.players_registry[client.ip_address[0]]))
                saved = self.players_registry[client.ip_address[0]]
                saved.client = client # Mise a jour du socket
                # restauration du joueur a son ancien index pour preserver l'ordre de jeu
                self.players[saved.unit - 1] = saved
                print("Restaure en "+str(saved.unit - 1))
                self.players_number = self.players_number + 1
                return Roles.Player

        if self.is_full is False:
            player = Player(len(self.players)+1, client)
            self.players_registry[client.ip_address[0]] = player
            self.players.append(player)
            self.players_number = self.players_number + 1
            if len(self.players) >= 2:
                self.is_full = True
            print("Game: ajout du joueur "+str(player))
            return Roles.Player
        else:
            observer = Entity(client)
            self.observers.append(observer)
            return Roles.Observer

    def remove_entity(self, client):
        """
            Permet de supprimer un joueur/observateur de la partie
        """
        for i in range(0, len(self.players)):
            player = self.players[i]
            if player.client == client:
                print("Game: "+str(player)+" quitte la partie")
                self.players[i] = None
                self.players_number = self.players_number + 1
                return True

        for observer in self.observers:
            if observer.client == client:
                print("Game: "+str(player)+" quitte la partie")
                self.observers.remove(observer)
                return True

        return False

        