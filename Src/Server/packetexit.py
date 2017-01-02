"""
    Ce module contient:
        La classe PacketExit: Paquet gerant la deconnexion d'un client
"""



from .System import packet as packet
from .Game import game as game

from . import server
from . import packetdisconnected
from . import packetend

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

            # Si le nombre de joueurs tombe a 0, on finit la partie et on la relance
            if game.Game.Instance.get_real_players_number() <= 0:
                for observer in game.Game.Instance.observers:
                    pkt = packetend.PacketEnd(observer.client, None)
                    pkt.send()
                game.Game.restart()
            else:
                # On lance un timer si le joueur n'est pas revenu dans 3 minutes
                # la partie est relancee
                server.Server.set_timer(3*60, server.Server.start)

        self.target.disconnect()
