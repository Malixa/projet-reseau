"""
    Ce module contient:
        La classe PacketScore: Paquet communiquant les scores
"""


import System.packet as packet
import Game.game as game

class PacketScore(packet.Packet):
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
        for player in game.Game.Instance.players:
            msg = msg + str(player.score) +","
        msg = msg[:-1] #On supprime le dernier ","
        self.target.send(msg)
