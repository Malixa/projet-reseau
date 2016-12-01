"""
    Ce module contient:
        La classe PacketRole:  indique a un participant son role dans la partie
"""

from System.packet import Packet


class PacketRole(Packet):
    """
        Indique a un participant son role dans la partie
    """

    def __init__(self, target, args):
        super(PacketRole, self).__init__(target, args)
        self.role = args[0]

    def send(self):
        msg = "ROLE " + self.role
        self.target.send(msg)
