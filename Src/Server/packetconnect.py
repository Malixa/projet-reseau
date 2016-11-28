from System.packet import Packet
from System.client import Client
from Game.player import Player
from Game.game import Game

from packetturn import PacketTurn

class PacketConnect(Packet):
    """
        Represente un paquet demandant au serveur d'enregistrer
        un client en tant que joueur si possible, ou observateur sinon.
    """

    def __init__(self, target, args):
        super(PacketConnect, self).__init__(target, args)

    def do(self, ctx):
        if Game.Instance.insert_entity(self.target):
            self.target.send("OK")
        else:
            self.target.send("NOP")

        # Lancement de la partie si tout est pret
        if Game.Instance.is_ready():
            client = Game.Instance.get_current_player().client
            packet = PacketTurn(client, None)
            packet.send()





