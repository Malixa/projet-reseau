import sys

from Server import server as server
from Client import client as client

def main():
	if len(sys.argv) >= 2:
		client.Client.start()
	else:
		server.Server.start()

main()
