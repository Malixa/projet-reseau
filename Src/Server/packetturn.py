from System.packet import Packet 

class PacketTurn(Packet):
    """
        Paquet indiquant a un joueur que c'est a son tour de jouer
    """

    def send(self):
        msg = "TURN"
        self.target.send(msg)
    