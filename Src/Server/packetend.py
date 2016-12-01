"""
    Ce module contient:
        La classe PacketEnd: indique aux joueurs la fin d'une partie
"""

import System.packet as packet

class PacketEnd(packet.Packet):
    """
        Indique aux joueurs la fin d'une partie
    """

    def __init__(self, target, args):
        super(PacketEnd, self).__init__(target, args)
        self.state = args[0]

    def send(self):
        msg = "END " + self.state
        self.target.send(msg)
