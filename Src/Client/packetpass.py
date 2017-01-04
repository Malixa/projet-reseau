"""
	Ce module contient:
		La classe packetpass : gère les cas où il ne se passe rien

"""

from .System import packet as packet 

class PacketPass(packet.Packet):

    def run(self, ctx):
        # Ne fait rien
        return

