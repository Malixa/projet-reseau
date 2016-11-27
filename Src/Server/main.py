from System.networker import Networker
from System.client import Client
from System.packetfactory import PacketFactory

from Game.player import Player
from Game.grid import Grid

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
    pass


def main():
    players = list()
    observers = list()
    grid = Grid()
    context = {"players" : players, "observers" : observers, "grid" : grid}

    server = Networker()
    server.listen()
    while True:
        clients = server.watch()
        for client in clients:
            #Etablissement du paquet
            data = client.receive()
            print(data)
            if len(data) == 0:
                data = "EXIT" #Force la creation d'un paquet exit pour de fermer proprement la cnx
                continue
            try:
                packet = PacketFactory.ExamineAndCreate(data, client)
                packet.do(context)
            except KeyError:
                #Le paquet envoye n'existe pas pour le serveur, on renvoit Nop au client
                client.send("NOP")
            print(players)
    pass


registerProto()
main()