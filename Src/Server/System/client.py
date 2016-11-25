class Client: 

    def __init__(self, server, socket, ip):
        self.server = server
        self.socket = socket
        self.ip = ip
    
    """
        fileno:
        Permet d'utiliser le client avec select
    """
    def fileno(self):
        return self.socket.fileno()

    """def interact(self):
        data = self.socket.recv(1024)
        if len(data) == 0:
            print(str(self.socket)+" disconnected")
            return False

        return True"""

    def receive(self):
        data = self.socket.recv(1024)
        data = data.decode("utf-8") # COnversion des bytes en string  
        return data.replace("\n", "") #Suppression d'un éventuel retour à la ligne 


    def disconnect(self):
        self.server.remove_client(self)

    
        