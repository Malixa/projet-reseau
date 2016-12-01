"""
    Point d'entree du programme de serveur
"""


import System.networker as networker
import System.packetfactory as packetfactory

import Game.game as game

import packetconnect
import packetexit
import packetplace
import packetgetstate
import packetgetscore


def register_proto():
    """
        Associe les differents types de paquets a leur commande.
    """
    packetfactory.PacketFactory.register("CONNECT", packetconnect.PacketConnect)
    packetfactory.PacketFactory.register("EXIT", packetexit.PacketExit)
    packetfactory.PacketFactory.register("PLACE", packetplace.PacketPlace)
    packetfactory.PacketFactory.register("GETSTATE", packetgetstate.PacketGetState)
    packetfactory.PacketFactory.register("GETSCORE", packetgetscore.PacketGetScore)


def main():
    """
        Lance le serveur est gere la routine
        de base
    """
    server = networker.Networker()
    server.listen()

    # Lancement d'une nouvelle partie
    game.Game.restart()
    while True:
        clients = server.watch()
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


register_proto()
main()
