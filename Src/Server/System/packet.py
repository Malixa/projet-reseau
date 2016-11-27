"""
    Module contenant la classe Packet
"""

class Packet(object):
    """
        Un paquet correspond a une commande dans le protocole du jeu.

        Il permet d'agir sur differents elements du jeu.
    """


    def __init__(self, target, args):
        """
            Constructeur de paquet

            @param target: client associe au paquet
            @param args: La liste des arguments ajoutes a la commande associee au paquet
        """
        self.target = target
        self.args = args

    def do(self, ctx):
        """
            Demande au paquet de realier son action

            @param ctx: contexte dans lequel le paquet agis.
        """
        raise RuntimeError("N'est pas un paquet a recevoir.'")



    def send(self):
        """
            Permet au paquet d'envoyer une reponse
        """
        raise RuntimeError("N'est pas un paquet a envoyer.'")

