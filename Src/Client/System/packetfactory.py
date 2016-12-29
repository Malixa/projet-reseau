"""
    Ce module contient:
    La classe PacketFactory: Instancie des paquets
"""

class PacketFactory(object):
    """
        Classe statique chargee d'instancier
        differents paquets
    """

    Types = dict()

    @staticmethod
    def register(command, typ):
        """
            Associe un nouveau type de paquet avec
            une commande definie.
        """
        PacketFactory.Types[command] = typ

    @staticmethod
    def examine_and_create(command, target):
        """
            Instancie le bon type de paquet
            en fonction de la valeur de command.
            Retourne une instance de paquet.
        """
        args = command.split(" ")
        command = args[0]
        args.pop(0) # on supprime la commande de la liste d'args
        return PacketFactory.Types[command](target, args)


    def __init__(self):
        raise Exception("Impossible d'instancier une factory.")
