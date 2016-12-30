from System import packet as packet
from Game import game as game


class PacketState(packet.Packet):

    def run(self, ctx):
        data = list()
        for index in self.args[0].split(','):
            if len(index) > 0:
                data.append(int(index))
        game.Game.Instance.update_grid(data)
        game.Game.Instance.display_grid()


