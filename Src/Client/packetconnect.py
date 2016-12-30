from .System import packet as packet

class PacketConnect(packet.Packet):

    def send(self):
        data = "CONNECT"
        self.server.send(data)
