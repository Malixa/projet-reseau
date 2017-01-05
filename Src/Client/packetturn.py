"""
	Ce module contient:
		La classe packetturn : gere l'affectation du tours du client

"""

from .System import packet as packet
from .Game import game as game


from . import packetexit as packetexit
from . import packetgetstate as packetgetstate
from . import packetplace as packetplace
from . import packetok as packetok
from . import packetnop as packetnop
from . import packetend as packetend
from . import packetpass as packetpass

class PacketTurn(packet.Packet):
    """
        La commande turn averti le client que c'est a son tour de jouer
    """

    def run(self, ctx):
        """
            gere le deroulement d'un tour
        """
        print("=====================NOUVEAU TOUR")
        # Met a jour l'etat de la grille de jeu
        getstate = packetgetstate.PacketGetState(self.server)
        getstate.send()

        # Permet au joueur de jouer
        place = -1
        print("Entrez l'indice de la case que vous souhaitez jouer [0-8]")
        print("Ou quittez la partie en entrant 'EXIT'")

        place = input()

        if "EXIT" in place.upper():
            exi = packetexit.PacketExit(self.server)
            exi.send()
            exit()

        try:
            place = int(place)
        except:
            self.run(ctx)
            return
            
        if game.Game.Instance.player.can_play(place) is True:
            pkt = packetplace.PacketPlace(self.server, [place])
            pkt.send()

            pkt = self.server.wait_packet()
            if isinstance(pkt, packetok.PacketOk):
                game.Game.Instance.player.play(place)
                # Affichage de la grille une fois que le joueur a joue
                game.Game.Instance.display_grid()
                print("C'est au tour de l'autre joueur.")
                print("=====================FIN TOUR")
                return
            elif isinstance(pkt, packetend.PacketEnd): #la partie est finie
                game.Game.Instance.display_grid()
                print("=====================FIN TOUR")
                pkt.run(None)
                return
            elif isinstance(pkt, packetpass.PacketPass): #On recoit pass, la case ne pouvait etre joue
                game.Game.Instance.player.discover(place)
                game.Game.Instance.display_grid()
                print("La case est deja occupee. Vous perdez la main.")
                print("=====================FIN TOUR")
                return
            elif isinstance(pkt, packetnop.PacketNop): #On recoit nop, on recommence
                pkt.run(None)
            else:
                pkt.run(None) #Autre paquet (deconnexion etc...)
                return

        print("Impossible de jouer cette case.")
        print("--------------------")
        self.run(ctx) #On redemande au joueur de placer
        return

