from System import packet as packet

class PacketExit(packet.Packet):

    def send(self):
        data = "EXIT"
        self.server.send(data)
