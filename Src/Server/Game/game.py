"""
    Ce module contient:
        La classe Game: Gere le deroulement d'une partie
"""

from . import entity
from . import player
from . import grid
from . import roles

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
        Game.Instance = None
        Game.Instance = Game()

    def __init__(self):
        if not Game.Instance is None:
            raise Exception("Il ne peut y avoir qu'une seule instance de game a la fois.")
        self.playing = 0 #Le joueur 1 commence
        self.players = list()
        self.players_registry = dict()
        self.observers = list()
        self.grid = grid.Grid()
        self.is_full = False

    def get_player_with_client(self, client):
        """
            Renvoie le joueur
            possedant le client donne
            en parametre
        """
        for ply in self.players:
            if ply.client == client:
                return ply

        return None

    def get_other_player(self, ply):
        """
            Retourne un autre joueur que celui passe
            en parametre
        """
        for ele in self.players:
            if ele != ply and not ele is None:
                return ele
        return None

    def get_current_player(self):
        """
            Retourne le joueur dont c'est le tour de jouer
        """
        return self.players[self.playing]

    def get_real_players_number(self):
        """
            Retourne le nombre de joueurs
            rellement dans la partie dans la partie
        """
        total = 0
        for ply in self.players:
            if not ply is None:
                total = total + 1
        return total

    def is_ready(self):
        """
            Retourne si les joueurs peuvent jouer
        """
        if self.get_real_players_number() < 2:
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
        for ply in self.players:
            if ply is not None and ply.client == client:
                #print("Game: deja enregistre")
                return None

        for observer in self.observers:
            if observer.client == client:
                #print("Game: deja enregistre")
                return None

        if client.ip_address[0] in self.players_registry:
            # Si le joueur n'est pas deja dans la liste de joueur (jeu local)
            if not self.players_registry[client.ip_address[0]] in self.players:
                #print("Game: Retour de "+str(self.players_registry[client.ip_address[0]]))
                saved = self.players_registry[client.ip_address[0]]
                saved.client = client # Mise a jour du socket
                # restauration du joueur a son ancien index pour preserver l'ordre de jeu
                self.players[saved.unit - 1] = saved
                #print("Restaure en "+str(saved.unit - 1))
                return roles.Roles.Player

        if self.is_full is False:
            ply = player.Player(len(self.players)+1, client)
            self.players_registry[client.ip_address[0]] = ply
            self.players.append(ply)
            if len(self.players) >= 2:
                self.is_full = True
            #print("Game: ajout du joueur "+str(player))
            return roles.Roles.Player
        else:
            observer = entity.Entity(client)
            self.observers.append(observer)
            return roles.Roles.Observer

    def remove_entity(self, client):
        """
            Permet de supprimer un joueur/observateur de la partie
        """
        for i in range(0, len(self.players)):
            ply = self.players[i]
            if ply.client == client:
                #print("Game: "+str(player)+" quitte la partie")
                self.players[i] = None
                return True

        for observer in self.observers:
            if observer.client == client:
                #print("Game: "+str(player)+" quitte la partie")
                self.observers.remove(observer)
                return True

        return False

    def won(self, ply):
        """
            Indique True si la partie est finie, False sinon
        """
        return self.grid.won(ply.unit)
        