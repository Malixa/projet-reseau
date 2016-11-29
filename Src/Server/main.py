from System.networker import Networker
from System.packetfactory import PacketFactory

from Game.game import Game

from packetconnect import PacketConnect
from packetexit import PacketExit
from packetplace import PacketPlace
from packetgetstate import PacketGetState
from packetgetscore import PacketGetScore


def register_proto():
    """
        Associe les differents types de paquets a leur commande.
    """
    PacketFactory.register("CONNECT", PacketConnect)
    PacketFactory.register("EXIT", PacketExit)
    PacketFactory.register("PLACE", PacketPlace)
    PacketFactory.register("GETSTATE", PacketGetState)
    PacketFactory.register("GETSCORE", PacketGetScore)


def main():
    """
        Lance le serveur est gere la routine
        de base
    """
    server = Networker()
    server.listen()

    # Lancement d'une nouvelle partie
    Game.restart()
    while True:
        clients = server.watch()
        for client in clients:
            #Etablissement du paquet
            data = client.receive()
            if len(data) == 0:
                data = "EXIT" #Force la creation d'un paquet exit pour de fermer proprement la cnx
                continue
            try:
                packet = PacketFactory.examine_and_create(data, client)
                packet.run(None)
            except KeyError:
                #Le paquet envoye n'existe pas pour le serveur, on renvoit Nop au client
                client.send("NOP")


register_proto()
main()
