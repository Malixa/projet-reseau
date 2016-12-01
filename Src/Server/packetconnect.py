"""
    Ce module contient:
        La classe PacketConnect: Paquet gerant une nouvelle connexion
"""

from System.packet import Packet

from Game.game import Game
from Game.roles import Roles

from packetturn import PacketTurn
from packetrole import PacketRole


class PacketConnect(Packet):
    """
        Represente un paquet demandant au serveur d'enregistrer
        un client en tant que joueur si possible, ou observateur sinon.
    """

    def __init__(self, target, args):
        super(PacketConnect, self).__init__(target, args)

    def run(self, ctx):
        role = Game.Instance.insert_entity(self.target)
        if role is None:
            self.target.send("NOP")
            return
        packet = PacketRole(self.target, [role])
        packet.send()

        # Lancement de la partie si tout est pret, Si le jeu est pret et que l'on a ajoute un joueur
        if Game.Instance.is_ready() and role == Roles.Player:
            client = Game.Instance.get_current_player().client
            packet = PacketTurn(client, None)
            packet.send()
