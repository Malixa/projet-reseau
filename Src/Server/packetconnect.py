from System.packet import Packet
from System.client import Client
from Game.player import Player

class PacketConnect(Packet):

    def __init__(self, target, args):
        if isinstance(target, Client) == False:
            raise Error("Ce paquet attend une target de type client.")
        super().__init__(target, args)

    def do(self, ctx):
        players = ctx["players"]
        observers = ctx["observers"]
        print(str(self.target)+" connecté!")
        if len(players) < 2:
            player = Player(len(players)+1, self.target)
            players.append(player)
        else:
            # Implémenter les observateurs
            pass