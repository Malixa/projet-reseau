"""
    Ce module contient:
        La classe PacketPlace: Paquet gerant une demande de placement sur la grille
"""

import System.packet as packet
import Game.game as game

import Game.ends as ends

import packetturn
import packetstate
import packetend

class PacketPlace(packet.Packet):
    """
        Represente un paquet demandant au serveur de
        jouer un coup a une cellule donnee
    """

    def __init__(self, target, args):
        super(PacketPlace, self).__init__(target, args)
        self.cell = None
        try: # On renvoie nop si l'argument est invalide
            self.cell = int(args[0])
        except ValueError:
            self.target.send("NOP")

    def run(self, ctx):
        # Si le parametre de la commande est invalide,
        # On ne fait rien
        if self.cell is None:
            return
        ply = game.Game.Instance.get_player_with_client(self.target)
        #print(Game.Instance.get_real_players_number())
        if ply is None or game.Game.Instance.is_ready() is False:
            self.target.send("NOP")
            return

        if ply.play(self.cell):
            # Envoie validation au joueur
            self.target.send("OK")
            # Test de la fin de la partie
            if game.Game.Instance.won(ply):
                # Envoi de win au gagnant
                pkt = packetend.PacketEnd(ply.client, [ends.Ends.Win])
                pkt.send()
                ply = game.Game.Instance.get_other_player(ply)
                if ply is None:
                    raise RuntimeError("Pas assez de joueurs pour gagner la partie")
                # Envoi de loose au perdant
                pkt = packetend.PacketEnd(ply.client, [ends.Ends.Loose])
                pkt.send()
                game.Game.restart()
                return
            # Changement de tour
            game.Game.Instance.turn()
            pkt = packetturn.PacketTurn(game.Game.Instance.get_current_player().client, None)
            pkt.send()
            for observer in game.Game.Instance.observers:
                pkt = packetstate.PacketState(observer.client, None)
                pkt.send()

        else:
            self.target.send("NOP")
