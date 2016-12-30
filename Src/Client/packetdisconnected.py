from .System import packet as packet


class PacketDisconnected(packet.Packet):

    def __init__(self, server, args):
        super(PacketDisconnected, self).__init__(server, args)
        self.other_ip = args[0]

    def run(self, ctx):
        print("Le joueur possedant l'adresse ip " + self.other_ip + " s'est deconnecte.")
        print("En attente de sa reconnexion...")


