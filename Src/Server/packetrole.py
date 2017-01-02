"""
    Ce module contient:
        La classe PacketRole:  indique a un participant son role dans la partie
"""

from .Game import roles as roles
from .System import packet as packet


class PacketRole(packet.Packet):
    """
        Indique a un participant son role dans la partie
    """

    def __init__(self, target, args):
        super(PacketRole, self).__init__(target, args)
        self.role = args[0]
        if self.role == roles.Roles.Player:
            self.player_index = str(args[1])

    def send(self):
        msg = "ROLE " + self.role
        if self.role == roles.Roles.Player:
            msg = msg+" "+self.player_index
        self.target.send(msg)
