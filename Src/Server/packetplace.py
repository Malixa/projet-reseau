from System.packet import Packet
from System.client import Client
from Game.player import Player

class PacketPlace(Packet):
    """
        Represente un paquet demandant au serveur de
        jouer un coup a une cellule donnee
    """

    def __init__(self, target, args):
        super(PacketPlace, self).__init__(target, args)
        self.cell = int(args[0])

    def do(self, ctx):
        players = ctx["players"]
        grid = ctx["grid"]
        player = None
        for pla in players:
            if pla.client == self.target:
                player = pla
        if player is None:
            self.target.send("NOP")
            return

        if grid.play(player, self.cell):
            self.target.send("OK")
            return
        else:
            self.target.send("NOP")



