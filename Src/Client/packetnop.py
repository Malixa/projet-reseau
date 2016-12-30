from .System import packet as packet


class PacketNop(packet.Packet):

    def run(self, ctx):
        pass
