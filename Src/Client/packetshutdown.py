from .System import packet as packet

from . import client as client

class PacketShutdown(packet.Packet):

    def run(self, ctx):
        client.Client.stop() #arret du client


