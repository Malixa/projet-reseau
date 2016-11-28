from System.networker import Networker
from System.client import Client
from System.packetfactory import PacketFactory

from Game.player import Player
from Game.grid import Grid
from Game.game import Game

from packetconnect import PacketConnect
from packetexit import PacketExit
from packetplace import PacketPlace
from packetgetstate import PacketGetState
from packetgetscore import PacketGetScore


def registerProto():
    PacketFactory.Register("CONNECT", PacketConnect)
    PacketFactory.Register("EXIT", PacketExit)
    PacketFactory.Register("PLACE", PacketPlace)
    PacketFactory.Register("GETSTATE", PacketGetState)
    PacketFactory.Register("GETSCORE", PacketGetScore)


def main():

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
                packet = PacketFactory.ExamineAndCreate(data, client)
                packet.do(None)
            except KeyError:
                #Le paquet envoye n'existe pas pour le serveur, on renvoit Nop au client
                client.send("NOP")


registerProto()
main()
