import socket
from . import packetfactory as packetfactory

class Server(object):


    Instance = None

    @staticmethod
    def start():
        """
            Initialise une nouvelle instance de classe
        """
        Server.Instance = None
        Server.Instance = Server()

    def __init__(self):

        # Une ne rend possible l'instanciation que d'un seul Networker
        if Server.Instance != None:
            raise Exception("Une seule instance de Networker est possible.")

        self.socket = None

    def connect(self, address, port=6666):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.socket.connect((address, port))

    def receive(self):
        data = self.socket.recv(1024)
        data = data.decode("utf-8") # COnversion des bytes en string
        return data.replace("\n", "") #Suppression d'un eventuel retour a la ligne

    def send(self, data):
        data = data.encode("utf-8")
        self.socket.send(data)

    def wait_packet(self):
        data = self.receive()
        if len(data) == 0:
            data = "SHUTDOWN"

        packet = packetfactory.PacketFactory.examine_and_create(data, self)
        return packet

        
        