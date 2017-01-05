"""
	Ce module contient:
		La classe packetstate : gère l'envoi des coups joués

"""

from .System import packet as packet
from .Game import game as game


class PacketState(packet.Packet):

"""
	La commande state renvoi la liste des coups joués au client permettant
	l'affichage de la grille
"""

    def run(self, ctx):
		"""
			Met en place la grille de jeu et affiche les coups joués
		"""
        data = list()
        for index in self.args[0].split(','):
		#permet de séparer la liste des coups joués et d'afficher la grille
            if len(index) > 0:
                data.append(int(index))
        game.Game.Instance.update_grid(data)
        game.Game.Instance.display_grid()
        if game.Game.Instance.mode == game.Game.MODE_OBSERVER:
            symb = game.Game.Instance.check_for_winner()
            if symb is None:
                return
            game.Game.Instance.won = True

