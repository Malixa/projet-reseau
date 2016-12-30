from System import packet as packet
from Game import game as game

import packetexit as packetexit
import packetgetstate as packetgetstate
import packetplace as packetplace
import packetok as packetok
import packetend as packetend

class PacketTurn(packet.Packet):

    def run(self, ctx):

        # Met a jour l'etat de la grille de jeu
        getstate = packetgetstate.PacketGetState(self.server)
        getstate.send()

        # Permet au joueur de jouer
        place = -1
        print("Entrez l'indice de la case que vous souhaitez jouer [0-8]")
        place = input()

        if place.upper() == "EXIT":
            exi = packetexit.PacketExit(self.server)
            exi.send()

        place = int(place)

        if game.Game.Instance.player.play(place) is True:
            place = packetplace.PacketPlace(self.server, [place])
            place.send()

            pkt = self.server.wait_packet()
            if isinstance(pkt, packetok.PacketOk):
                # Affichage de la grille une fois que le joueur a joue
                game.Game.Instance.display_grid()
                print("C'est au tour de l'autre joueur.")
                return
            elif isinstance(pkt, packetend.PacketEnd):
                pkt.run(None)
                return

        print("Impossible de jouer cette case.")
        self.run(ctx) #On redemande au joueur de placer
        return

