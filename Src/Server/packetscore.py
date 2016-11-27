from System.packet import Packet 
from Game.player import Player

"""
    Module contenant la class PacketScore
"""

class PacketScore(Packet):
    """
        Classe permettant au serveur d'envoyer a un de ses clients
        le score des differents joueurs en jeu
    """


    def __init__(self, target, args):
        #args[0][0] car si cette commande est recu c'est qu'un joueur est connecte
        #et est donc dans la liste
        if not isinstance(args[0][0], Player):
            raise TypeError("args doit etre un tableau contenant une liste de joueurs a l'index 0'")
        super(PacketScore, self).__init__(target, args)
        self.players = args[0]

    def send(self):
        msg = "SCORE "
        #Normalement les joueurs sont ordonnes dans le bon ordre:
        #joueur 1 a l'index 0, j2 a l'index 1 etc...
        for player in self.players:
            msg = msg + str(player.score) +","
        msg = msg[:-1] #On supprime le dernier ","
        self.target.send(msg)

