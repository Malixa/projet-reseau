"""
	Ce module contient:
		La classe packetend : gère la fin de partie (victoire, défaite)

"""

from .System import packet as packet
from .Game import game as game


class PacketEnd(packet.Packet):

	"""
		La commande end informe le joueur de sa victoire/défaite ou rien si le client
		est une observateur
	"""
    def __init__(self, server, args):
        super(PacketEnd, self).__init__(server, args)
        self.state = self.args[0]


    def run(self, ctx):
		"""
			Définie le client gagnant
		"""
        game.Game.Instance.won = True
        if self.state == "win":
            game.Game.Instance.player.winner = True
        else:
            game.Game.Instance.player.winner = False



