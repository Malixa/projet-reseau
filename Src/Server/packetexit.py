from System.packet import Packet
from System.client import Client
from Game.player import Player
from Game.game import Game

class PacketExit(Packet):
    """
        Represente un paquet demandant au serveur de deconnecter
        l'expediteur proprement
    """

    def __init__(self, target, args):
        super(PacketExit, self).__init__(target, args)

    def do(self, ctx):
        if Game.Instance.remove_entity(self.target):
            self.target.send("OK")
        else:
            # Ca ne devrait jamais arriver en jeu
            self.target.send("NOP")
        self.target.disconnect()


