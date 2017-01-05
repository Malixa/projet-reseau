"""
	Ce module contient:
		La classe packetstate : gere l'envoi des coups joues

"""

from .System import packet as packet
from .Game import game as game


class PacketState(packet.Packet):
    """
        La commande state renvoi la liste des coups joues au client permettant
        l'affichage de la grille
    """

    def run(self, ctx):
        """
            Met en place la grille de jeu et affiche les coups joues
        """
        data = list()
        for index in self.args[0].split(','):
		#permet de separer la liste des coups joues et d'afficher la grille
            if len(index) > 0:
                data.append(int(index))
        game.Game.Instance.update_grid(data)
        game.Game.Instance.display_grid()
        if game.Game.Instance.mode == game.Game.MODE_OBSERVER:
            symb = game.Game.Instance.check_for_winner()
            if symb is None:
                return
            game.Game.Instance.won = True

