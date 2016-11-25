from System.networker import Networker
from System.client import Client
from System.packetfactory import PacketFactory

from Game.player import Player
from Game.grid import Grid

from packetconnect import PacketConnect
from packetexit import PacketExit
from packetplace import PacketPlace


def registerProto():
    PacketFactory.Register("CONNECT", PacketConnect)
    PacketFactory.Register("EXIT", PacketExit)
    PacketFactory.Register("PLACE", PacketPlace)
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
            packet = PacketFactory.ExamineAndCreate(data, client)
            packet.do(context)
            print(players)
    pass


registerProto()
main()