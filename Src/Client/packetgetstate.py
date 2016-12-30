from System import packet as packet

from Game import game as game

class PacketGetState(packet.Packet):

    def send(self):
        data = "GETSTATE"
        self.server.send(data)

        state = self.server.wait_packet()
        state.run(None)
