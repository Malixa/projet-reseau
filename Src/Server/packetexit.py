from System.packet import Packet
from System.client import Client
from Game.player import Player
from Game.game import Game

from packetdisconnected import PacketDisconnected

class PacketExit(Packet):
    """
        Represente un paquet demandant au serveur de deconnecter
        l'expediteur proprement
    """

    def __init__(self, target, args):
        super(PacketExit, self).__init__(target, args)

    def do(self, ctx):
        is_player = False

        if Game.Instance.get_player_with_client(self.target) is not None:
            is_player = True

        if Game.Instance.remove_entity(self.target):
            self.target.send("OK")
        else:
            # Ca ne devrait jamais arriver en jeu
            self.target.send("NOP")

        if is_player:
            # Si le deconnecte etait un joueur, on envoie
            # a tout le monde qu'il est parti
            for player in Game.Instance.players:
                if player is None:
                    continue
                packet = PacketDisconnected(player.client, [self.target.ip_address])
                packet.send()
            for observers in Game.Instance.observers:
                packet = PacketDisconnected(observers.client, [self.target.ip_address])
                packet.send()

        self.target.disconnect()


