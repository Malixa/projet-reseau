class Client: 

    def __init__(self, socket, ip):
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
        