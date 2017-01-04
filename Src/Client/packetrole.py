"""
	Ce module contient:
		La classe packetrole : gère le role du client (joueur ou observateur)

"""

from .System import packet as packet 

class PacketRole(packet.Packet):


    ROLES = ['player', 'observer']

#initialisation du paquet : création des propriétés role et player_index
    def __init__(self, server, args):
        super(PacketRole, self).__init__(server, args)
        self.role = None
        self.player_index = None

#Règle les propriétés rôles et player_index du paquet
    def run(self, ctx):
        for role in PacketRole.ROLES:
            if role == self.args[0]:
                self.role = role
        if self.role == PacketRole.ROLES[0]:
            self.player_index = int(self.args[1])

#defini le role du client : joueur
    def is_player(self):
        return self.role == PacketRole.ROLES[0]

#defini le role du client : observateur
    def is_observer(self):
        return self.role == PacketRole.ROLES[1]
