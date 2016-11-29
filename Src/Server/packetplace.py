"""
    Ce module contient:
        La classe PacketPlace: Paquet gerant une demande de placement sur la grille
"""

from System.packet import Packet
from Game.game import Game

from packetturn import PacketTurn

class PacketPlace(Packet):
    """
        Represente un paquet demandant au serveur de
        jouer un coup a une cellule donnee
    """

    def __init__(self, target, args):
        super(PacketPlace, self).__init__(target, args)
        self.cell = None
        try: # On renvoie nop si l'argument est invalide
            self.cell = int(args[0])
        except ValueError:
            self.target.send("NOP")

    def run(self, ctx):
        # Si le parametre de la commande est invalide,
        # On ne fait rien
        if self.cell is None:
            return
        player = Game.Instance.get_player_with_client(self.target)
        if player is None:
            self.target.send("NOP")
            return

        if player.play(self.cell):
            # Changement de tour
            Game.Instance.turn()
            packet = PacketTurn(Game.Instance.get_current_player().client, None)
            packet.send()
            # Envoie validation au joueur
            self.target.send("OK")
            # TODO: implementer l'envoi a tout les observateurs
        else:
            self.target.send("NOP")
