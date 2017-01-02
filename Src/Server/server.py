"""
    Point d'entree du programme de serveur
"""

from threading import Timer
import time

from .System import networker as networker
from .System import packetfactory as packetfactory

from .Game import game as game

from . import packetconnect
from . import packetexit
from . import packetplace
from . import packetgetstate
from . import packetgetscore

class Server(object):

    Timer = None

    @staticmethod
    def register_proto():
        """
            Associe les differents types de paquets a leur commande.
        """
        packetfactory.PacketFactory.register("CONNECT", packetconnect.PacketConnect)
        packetfactory.PacketFactory.register("EXIT", packetexit.PacketExit)
        packetfactory.PacketFactory.register("PLACE", packetplace.PacketPlace)
        packetfactory.PacketFactory.register("GETSTATE", packetgetstate.PacketGetState)
        packetfactory.PacketFactory.register("GETSCORE", packetgetscore.PacketGetScore)

    @staticmethod
    def main():
        """
            Lance le serveur est gere la routine
            de base
        """

        # Lancement de l'instance de networker
        networker.Networker.start()
        networker.Networker.Instance.listen()

        print("Server lance !")
        # Lancement d'une nouvelle partie
        game.Game.restart()
        while True:
            clients = networker.Networker.Instance.watch()
            for client in clients:
                #Etablissement du paquet
                data = client.receive()
                if len(data) == 0:
                    data = "EXIT" #Force la creation d'un paquet exit pour de fermer proprement la cnx
                try:
                    packet = packetfactory.PacketFactory.examine_and_create(data, client)
                    packet.run(None)
                except KeyError:
                    #Le paquet envoye n'existe pas pour le serveur, on renvoit Nop au client
                    client.send("NOP")

    @staticmethod
    def set_timer(amount, callback):
        Server.Timer = Timer(amount, callback)
        Server.Timer.start()

    @staticmethod
    def stop_timer():
        if Server.Timer is not None:
            Server.Timer.cancel()
        Server.Timer = None

    @staticmethod
    def start():
        Server.stop_timer()
        Server.register_proto()
        Server.main()
