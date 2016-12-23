#!/usr/bin/python3

import socket
import select
import sys
import re
import ../Src/Serveur/Game/grid

TURN = re.compile('^TURN')
OK = re.compile('^OK')
NOP = re.compile('^NOP')
STATE = re.compile('^STATE')
SCORE = re.compile('^SCORE')
DISCO = re.compile('^DISCONNECTED')
OFF = re.compile('^SHUTDOWN')
PLAYER = re.compile('^ROLE player')
OBS = re.compile('^ROLE observer')

CONNECT = "CONNECT"
GETSTATE = "GETSTATE"
GETSCORE = "GETSCORE"
EXIT = "EXIT"
PLACE = "PLACE"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.connect(('',argv[1]))

sock.send(CONNECT.encode("utf-8"))
data = sock.recv(1024)
new_data = data.decode("utf-8")
if re.match(NOP, new_data):
    print("Invalid connection (error server / already connected)")
elif re.match(PLAYER, new_data):
    print("Vous êtes un joueur")
    num = new_data.split(" ")
    sock.send(GETSTATE.encode("utf-8"))
    data = sock.recv(1024)
    new_data = data.decode("utf-8")
    tab = new_data.split(" ")
    tab = tab[1].split(",")
    __init__(tab)
    data = sock.recv(1024)
    new_data = data.decode("utf-8")
    if re.match(TURN, new_data)
        place = -1
        while re.match(OK, new_data)==false
            while place <0 or place >8
                print("placer votre pion")
                place = input()
                if place = "exit"
                    sock.send("EXIT")
            sock.send("PLACE ",place)
            data = sock.recv(1024)
            new_data = data.decode("utf-8")
            if re.match(OK, new_data)
                print("a l'autre joueur")
            else
                print("cette case est déjà occupée, replacer votre pion")
                
else
    print("Vous êtes un observateur")
    sock.send(GETSCORE.encode("utf-8"))
    data = sock.recv(1024)
    new_data = data.decode("utf-8")
    if re.match(SCORE,new_data)
        tab = new_data.split(',')
        print("Voici le score des 2 joueurs : ",tab[0]," / ",tab[1])
        while true
            sock.send(GETSTATE.encode("utf-8"))
            data = sock.recv(1024)
            new_data = data.decode("utf-8")
            if re.match(STATE,new_data)
                tab = new_data.split(',')
                __init__(tab[1..9])
            
            
        
            
            


       
