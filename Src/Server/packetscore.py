from System.packet import Packet 
from Game.player import Player
from Game.game import Game

"""
    Module contenant la class PacketScore
"""

class PacketScore(Packet):
    """
        Classe permettant au serveur d'envoyer a un de ses clients
        le score des differents joueurs en jeu
    """


    def __init__(self, target, args):
        super(PacketScore, self).__init__(target, args)

    def send(self):
        msg = "SCORE "
        #Normalement les joueurs sont ordonnes dans le bon ordre:
        #joueur 1 a l'index 0, j2 a l'index 1 etc...
        for player in Game.Instance.players:
            msg = msg + str(player.score) +","
        msg = msg[:-1] #On supprime le dernier ","
        self.target.send(msg)

