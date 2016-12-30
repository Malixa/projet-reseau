from .System import packet as packet

class PacketPlace(packet.Packet):

    def send(self):
        place = self.args[0]
        data = "PLACE "+str(place)
        self.server.send(data)
