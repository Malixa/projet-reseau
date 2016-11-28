from System.packet import Packet 

class PacketDisconnected(Packet):
    """
        Paquet indiquant a un joueur que l'autre joueur s'est deconnecte
    """
    def __init__(self, target, args):
        super(PacketDisconnected, self).__init__(target, args)
        self.other_ip = args[0][0]

    def send(self):
        msg = "DISCONNECTED "+self.other_ip
        self.target.send(msg)

