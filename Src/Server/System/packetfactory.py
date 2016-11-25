from .packet import Packet 

class PacketFactory:

    Types = dict()

    @staticmethod
    def Register(command, typ):
        PacketFactory.Types[command] = typ

    @staticmethod
    def ExamineAndCreate(command, target):
        args = command.split(" ")
        command = args[0]
        args.pop(0) # on supprime la commande de la liste d'args
        return PacketFactory.Types[command](target, args)


    def __init__(self):
        raise Error("Impossible d'instancier une factory.")
