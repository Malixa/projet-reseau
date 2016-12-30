"""
    Ce module contient:
        La classe PacketConnect: Paquet gerant une nouvelle connexion
"""

import System.packet as packet

import Game.game as game
import Game.roles as roles

import packetturn
import packetrole


class PacketConnect(packet.Packet):
    """
        Represente un paquet demandant au serveur d'enregistrer
        un client en tant que joueur si possible, ou observateur sinon.
    """

    def __init__(self, target, args):
        super(PacketConnect, self).__init__(target, args)

    def run(self, ctx):
        role = game.Game.Instance.insert_entity(self.target)
        if role is None:
            self.target.send("NOP")
            return
        pkt = packetrole.PacketRole(self.target, role)
        pkt.send()

        # Lancement de la partie si tout est pret, Si le jeu est pret et que l'on a ajoute un joueur
        if game.Game.Instance.is_ready() and role[0] == roles.Roles.Player:
            client = game.Game.Instance.get_current_player().client
            pkt = packetturn.PacketTurn(client, None)
            pkt.send()
