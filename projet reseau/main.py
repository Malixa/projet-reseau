#!/usr/bin/python3

from grid import *
import  random
import time
import socket
import select

#creation des sockets, écoute, connexion
ip = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0) 
#ip.setsockopt(socket.SOL_SOCKEET, socket.SO_REUSEADDR,1)
ip.bind('',) #serveur, port, nom machine ?
ip.listen(1)


def main():
    grids = [grid(), grid(), grid()]
    current_player = J1
    grids[J1].display()
    while grids[0].gameOver() == -1:
        if current_player == J1:
            shot = -1
            while shot <0 or shot >=NB_CELLS:
                shot = int(input ("quel case allez-vous jouer ?"))
        else:
            shot = random.randint(0,8)
            while grids[current_player].cells[shot] != EMPTY:
                shot = random.randint(0,8)
        if (grids[0].cells[shot] != EMPTY):
            grids[current_player].cells[shot] = grids[0].cells[shot]
        else:
            grids[current_player].cells[shot] = current_player
            grids[0].play(current_player, shot)
            current_player = current_player%2+1
        if current_player == J1:
            grids[J1].display()
    print("game over")
    time.sleep(2)
    grids[0].display()
    time.sleep(4)
    if grids[0].gameOver() == J1:
        print("You win !")
        time.sleep(2)
    else:
        print("you loose !")
        time.sleep(2)


main()
