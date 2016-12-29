#!/usr/bin/python3

import sys

from System import server as server
from System import packetfactory as packetfactory

import packetconnect as packetconnect
import packetrole as packetrole

def register_proto():
    """
        Associe les differents types de paquets pouvant etre recus a leur commande.
    """
    packetfactory.PacketFactory.register("ROLE", packetrole.PacketRole)
    pass

def player():
    print('player')
    while True:
        data = server.Server.Instance.receive()
        if len(data) == 0:
            #Force la creation d'un paquet shutdown pour de fermer proprement la cnx
            data = "SHUTDOWN"
        try:
            packet = packetfactory.PacketFactory.examine_and_create(data, server.Server.Instance)
            packet.run(None)
        except KeyError:
            #Le paquet envoye n'existe pas pour le client, on exit
            #TODO: gerer exit
            pass
        
    pass

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
        player()
    elif role.is_observer():
        observer()



register_proto()
main()
