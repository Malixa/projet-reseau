from System.packet import Packet
from System.client import Client
from Game.player import Player

class PacketExit(Packet):
    """
        Represente un paquet demandant au serveur de deconnecter
        l'expediteur proprement
    """

    def __init__(self, target, args):
        super(PacketExit, self).__init__(target, args)

    def do(self, ctx):
        players = ctx["players"]
        observers = ctx["observers"]
        for player in players:
            if player.client == self.target:
                players.remove(player)
        for observer in observers:
            if observer.client == self.target:
                observers.remove(observer)

        self.target.send("OK")
        self.target.disconnect()


