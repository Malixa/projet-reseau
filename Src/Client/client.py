"""
	Ce module contient :
		La classe client : 
"""
#!/usr/bin/python3

import sys

from .System import server as server
from .System import packetfactory as packetfactory

from .Game import game as game

from . import packetconnect as packetconnect
from . import packetrole as packetrole
from . import packetturn as packetturn
from . import packetstate as packetstate
from . import packetok as packetok
from . import packetnop as packetnop
from . import packetend as packetend
from . import packetshutdown as packetshutdown
from . import packetdisconnected as packetdisconnected
from . import packetpass as packetpass

class Client(object):

	"""
		Représente le client
	"""

    Running = False

    @staticmethod
    def register_proto():
        """
            Associe les differents types de paquets pouvant etre recus a leur commande.
        """
        packetfactory.PacketFactory.register("ROLE", packetrole.PacketRole)
        packetfactory.PacketFactory.register("TURN", packetturn.PacketTurn)
        packetfactory.PacketFactory.register("STATE", packetstate.PacketState)
        packetfactory.PacketFactory.register("OK", packetok.PacketOk)
        packetfactory.PacketFactory.register("NOP", packetnop.PacketNop)
        packetfactory.PacketFactory.register("END", packetend.PacketEnd)
        packetfactory.PacketFactory.register("SHUTDOWN", packetshutdown.PacketShutdown)
        packetfactory.PacketFactory.register("DISCONNECTED", packetdisconnected.PacketDisconnected)
        packetfactory.PacketFactory.register("PASS", packetpass.PacketPass)

    @staticmethod
    def player(player_index):
		"""
			Lance une partie en tant que joueur et gère la routine de jeu
		"""

        print("####################")
        print("Connecte au serveur en tant que joueur !")
        print("En attente d'un adversaire...")
        game.Game.start(player_index)
        while game.Game.Instance.won is False and Client.Running is True:
            try:
                packet = server.Server.Instance.wait_packet()
                packet.run(None)
            except KeyError:
                #Le paquet envoye n'existe pas pour le client, on exit
                print("Erreur de communication avec le serveur...")
            except Exception as e: #Affichage des erreurs
                print("Une erreur est survenue:")
                print(str(e))

        #Gestion de la fermeture de la connexion
        if Client.Running is False:
            print("La connexion a ete fermee...")
            exit()
        # Gestion de la fin de partie
        if game.Game.Instance.player.winner is True:
            print("Vous avez gagne !")
        else:
            print("Vous avez perdu...")

        entry = None
        while entry != "1" and entry != "2":
            print("Se connecter pour une nouvelle partie [1: Oui, 2: Non] ?")
            entry = input()
        if entry == "1":
            Client.main()

    @staticmethod
    def observer():
		"""
			Lance une partie en tant qu'observateur et gère la routine d'observation
		"""

        print("####################")
        print("Connecte au serveur en tant qu'observateur !")
        print("En attente des joueurs...")
        game.Game.start(0) #nouvelle partie sans joueur
        while game.Game.Instance.won is False and Client.Running is True:
            try:
                packet = server.Server.Instance.wait_packet()
                packet.run(None)
            except KeyError:
                #Le paquet envoye n'existe pas pour le client, on exit
                print("Erreur de communication avec le serveur...")
            """except Exception as e: #Affichage des erreurs
                print("Une erreur est survenue:")
                print(str(e))"""
        #Gestion de la fermeture de la connexion
        if Client.Running is False:
            print("La connexion a ete fermee...")
            exit()
        # Gestion de la fin de partie
        symb = game.Game.Instance.check_for_winner()
        print("Le joueur "+symb+" a gagne la partie !")


        entry = None
        while entry != "1" and entry != "2":
            print("Se connecter pour une nouvelle partie [1: Oui, 2: Non] ?")
            entry = input()
        if entry == "1":
            Client.main()
        pass

    @staticmethod
    def main():
		"""
			Connecte le client au serveur et définie son rôle
		"""

        server.Server.start()
        try:
            if len(sys.argv) > 2:
                server.Server.Instance.connect(sys.argv[1], int(sys.argv[2]))
            else:
                server.Server.Instance.connect(sys.argv[1])
        except: 
            print("Impossible d'atteindre le serveur.")
            return

        # Etablissement de la connexion et determination du role du client
        connection = packetconnect.PacketConnect(server.Server.Instance)
        connection.send()

        role = packetfactory.PacketFactory.examine_and_create(server.Server.Instance.receive(), server.Server.Instance)
        role.run(None)
        if role.is_player():
            Client.player(role.player_index)
        elif role.is_observer():
            Client.observer()

    @staticmethod
    def stop():
		"""
			Cause l'arret du client
		"""
        Client.Running = False

    @staticmethod
    def start():
		"""
			Permet le lancement de la partie
		"""
        Client.Running = True
        Client.register_proto()
        Client.main()

