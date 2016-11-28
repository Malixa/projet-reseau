from System.packet import Packet
from System.client import Client
from Game.player import Player
from Game.game import Game

class PacketPlace(Packet):
    """
        Represente un paquet demandant au serveur de
        jouer un coup a une cellule donnee
    """

    def __init__(self, target, args):
        super(PacketPlace, self).__init__(target, args)
        self.cell = None
        try:
            self.cell = int(args[0])
        except ValueError:
            self.target.send("NOP")

    def do(self, ctx):
        # Si le parametre de la commande est invalide,
        # On ne fait rien
        if self.cell is None:
            return
        player = Game.Instance.get_player_with_client(self.target)
        if player is None:
            self.target.send("NOP")
            return

        if Game.Instance.grid.play(player, self.cell):
            self.target.send("OK")
            return
        else:
            self.target.send("NOP")



