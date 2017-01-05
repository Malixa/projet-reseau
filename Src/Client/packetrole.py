"""
	Ce module contient:
		La classe packetrole : gère le role du client (joueur ou observateur)

"""

from .System import packet as packet 

class PacketRole(packet.Packet):

	"""
		La commande role indique au client s'il est joueur ou observateur
		Indique au joueur son numéro de joueur
	"""
    ROLES = ['player', 'observer']

    def __init__(self, server, args):
        super(PacketRole, self).__init__(server, args)
        self.role = None
        self.player_index = None


    def run(self, ctx):
		"""
			Règle les propriétés rôles et player_index du paquet
		"""
        for role in PacketRole.ROLES:
            if role == self.args[0]:
                self.role = role
        if self.role == PacketRole.ROLES[0]:
            self.player_index = int(self.args[1])


    def is_player(self):
		"""
			Defini le role du client : joueur
		"""
        return self.role == PacketRole.ROLES[0]


    def is_observer(self):
		"""
			defini le role du client : observateur
		"""
        return self.role == PacketRole.ROLES[1]
