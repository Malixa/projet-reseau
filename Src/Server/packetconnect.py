from System.packet import Packet
from System.client import Client
from Game.player import Player

class PacketConnect(Packet):
    """
        Represente un paquet demandant au serveur d'enregistrer
        un client en tant que joueur si possible, ou observateur sinon.
    """

    def __init__(self, target, args):
        super(PacketConnect, self).__init__(target, args)

    def do(self, ctx):
        players = ctx["players"]
        observers = ctx["observers"]
        for player in players:
            if player.client == self.target:
                self.target.send("NOP")
                return
        for observer in observers:
            if observer.client == self.target:
                self.target.send("NOP")
                return
        if len(players) < 2:
            player = Player(len(players)+1, self.target)
            players.append(player)
        else:
            # TODO: Implementer les observateurs
            pass
        self.target.send("OK")



