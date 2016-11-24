from System.networker import Networker
from Game.player import Player



def main():
    players = list()
    server = Networker()
    server.listen()
    while True:
        clients = server.watch()
        for client in clients:
            #Etablissement du paquet
            data = client.socket.recv(1024)
            if len(data) == 0:
                server.remove_client(client)
    pass

main();