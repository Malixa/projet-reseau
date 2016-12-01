"""
    Ce module contient:
        La classe PacketExit: Paquet gerant la deconnexion d'un client
"""

import System.packet as packet
import Game.game as game

import packetdisconnected

class PacketExit(packet.Packet):
    """
        Represente un paquet demandant au serveur de deconnecter
        l'expediteur proprement
    """

    def __init__(self, target, args):
        super(PacketExit, self).__init__(target, args)

    def run(self, ctx):
        is_player = False

        if game.Game.Instance.get_player_with_client(self.target) is not None:
            is_player = True

        if game.Game.Instance.remove_entity(self.target):
            self.target.send("OK")
        else:
            # Ca ne devrait jamais arriver en jeu
            self.target.send("NOP")

        if is_player:
            # Si le deconnecte etait un joueur, on envoie
            # a tout le monde qu'il est parti
            for player in game.Game.Instance.players:
                if player is None:
                    continue
                pkt = packetdisconnected.PacketDisconnected(player.client, [self.target.ip_address])
                pkt.send()
            for observers in game.Game.Instance.observers:
                pkt = packetdisconnected.PacketDisconnected(observers.client, [self.target.ip_address])
                pkt.send()

        self.target.disconnect()
