"""
	Ce module contient:
		La classe packetpass : signale au client qu'il passe son tour

"""

from .System import packet as packet

class PacketPass(packet.Packet):
	"""
		La commande pass signale au client qu'il passe son tour
	"""
	
	def run(self, ctx):
		# Ne fait rien
		return

