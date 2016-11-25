from System.networker import Networker
from System.client import Client
from System.packetfactory import PacketFactory
from Game.player import Player

from packetconnect import PacketConnect


def registerProto():
    PacketFactory.Register("CONNECT", PacketConnect)
    pass


def main():
    players = list()
    observers = list()
    server = Networker()
    server.listen()
    while True:
        clients = server.watch()
        for client in clients:
            #Etablissement du paquet
            data = client.receive()
            print(data)
            if len(data) == 0:
                client.disconnect()
                continue
            packet = PacketFactory.ExamineAndCreate(data, client)
            packet.do({"players" : players, "observers" : observers})
            print(players)
    pass


registerProto()
main()