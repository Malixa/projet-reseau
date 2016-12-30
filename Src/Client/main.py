#!/usr/bin/python3

import sys

from System import server as server
from System import packetfactory as packetfactory

from Game import game as game

import packetconnect as packetconnect
import packetrole as packetrole
import packetturn as packetturn
import packetstate as packetstate
import packetok as packetok
import packetend as packetend





def register_proto():
    """
        Associe les differents types de paquets pouvant etre recus a leur commande.
    """
    packetfactory.PacketFactory.register("ROLE", packetrole.PacketRole)
    packetfactory.PacketFactory.register("TURN", packetturn.PacketTurn)
    packetfactory.PacketFactory.register("STATE", packetstate.PacketState)
    packetfactory.PacketFactory.register("OK", packetok.PacketOk)
    packetfactory.PacketFactory.register("END", packetend.PacketEnd)

def player(player_index):
    game.Game.start(player_index)
    while game.Game.Instance.won is False:
        try:
            packet = server.Server.Instance.wait_packet()
            packet.run(None)
        except KeyError:
            #Le paquet envoye n'existe pas pour le client, on exit
            #TODO: gerer exit
            pass
    if game.Game.Instance.player.winner is True:
        print("Vous avez gagne !")
    else:
        print("Vous avez perdu...")

    entry = None
    while entry != "1" and entry != "2":
        print("Se connecter pour une nouvelle partie [1: Oui, 2: Non] ?")
        entry = input()
    if entry == "1":
        main()

def observer():
    print('observer')

    pass

def main():
    server.Server.start()
    if len(sys.argv) > 2:
        server.Server.Instance.connect(sys.argv[1], int(sys.argv[2]))
    else:
        server.Server.Instance.connect(sys.argv[1])

    # Etablissement de la connexion et determination du role du client
    connection = packetconnect.PacketConnect(server.Server.Instance)
    connection.send()

    role = packetfactory.PacketFactory.examine_and_create(server.Server.Instance.receive(), server.Server.Instance)
    role.run(None)
    if role.is_player():
        player(role.player_index)
    elif role.is_observer():
        observer()



register_proto()
main()
