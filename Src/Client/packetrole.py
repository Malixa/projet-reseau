from System import packet as packet 

class PacketRole(packet.Packet):


    ROLES = ['player', 'observer']

    def __init__(self, server, args):
        super(PacketRole, self).__init__(server, args)
        self.role = None
        self.player_index = None


    def run(self, ctx):
        for role in PacketRole.ROLES:
            if role == self.args[0]:
                self.role = role
        if self.role == PacketRole.ROLES[0]:
            self.player_index = int(self.args[1])

    def is_player(self):
        return self.role == PacketRole.ROLES[0]

    def is_observer(self):
        return self.role == PacketRole.ROLES[1]
