"""
	Ce module contient:
		La classe packetend : gère la fin de partie (victoire, défaite)

"""

from .System import packet as packet
from .Game import game as game


class PacketEnd(packet.Packet):

#initialisation du paquet
    def __init__(self, server, args):
        super(PacketEnd, self).__init__(server, args)
        self.state = self.args[0]

#Définie le client gagnant
    def run(self, ctx):
        game.Game.Instance.won = True
        if self.state == "win":
            game.Game.Instance.player.winner = True
        else:
            game.Game.Instance.player.winner = False



