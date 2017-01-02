"""
    Ce module contient:
        La classe PacketConnect: Paquet gerant une nouvelle connexion
"""

from .System import packet as packet

from .Game import game as game
from .Game import roles as roles

from . import server
from . import packetturn
from . import packetrole


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
            # Il se peut qu'un timer ai ete lance
            # On l'arrete si c'est le cas
            server.Server.stop_timer()
            client = game.Game.Instance.get_current_player().client
            pkt = packetturn.PacketTurn(client, None)
            pkt.send()
