# Morpion aveugle 

## Avant-Propos

Ce projet nécessite  l'utilisation de python 3.5+ pour fonctionner (commande python3).

## TODO

- [x] Coder protocole(Clovis)
- [x] Coder serveur  (Clovis)
    * Corriger bug du tour lors de la reconnexion
- [ ] Coder client  (Célia)

### Extensions

- [x] Jouer plusieurs parties
- [ ] Ajouter bot (???)
- [X] observateurs
- [x] A la fin d'une partie, on selectionne deux nouveaux joueurs parmis les joueurs/observateurs
- [X] gérer la déconnexion
- [X] gérer les crashs du client

## Protocole 

Plusieurs commandes envoyées au serveurs, entrainant toujours une réponse (ou confirmation de sa part).
Pour confirmer le serveur renvoie "OK" au client.

| Commande client au serveur | Arguments | Effet | Réponse | Action joueur |
|----------|-----------|-------|---------|---------------|
| CONNECT | NULL | Entraine initialisation du joueur coté serveur | ROLE si réussi ou NOP si erreur | NON |
| GETSTATE | NULL | Récupération de l'état de la partie en cours | STATE 5,8,1 "La case 5 < joueur 1, la case 8 < joueur 2, la case 1 < joueur 1 | NON |
| GETSCORE | NULL | Récupération du score des joueurs | SCORE a,b "a : score joueur 1, b : score joueur 2" | NON |
| EXIT | NULL | Le joueur se déconnecte | OK | OUI |
| PLACE | a "a: numéro de la case" | Place le jeton sauf si case déja occupée | OK / NOP "OK: si placé, NOP: sinon" | OUI |


| Commande serveur au client | Arguments | Effet |
|----------------------------|-----------|-------|
| OK | NULL | Acquittement de la dernière commande | 
| NOP | NULL | Refus de la dernière commande | 
| STATE | a,b,c....n | Retourne la liste des coups joués, impair: joueur 1, pair: joueur 2 | 
| SCORE | a,b | a: score joueur 1, b: score joueur 2 |
| DISCONNECTED | ip | ip: Ip du deconnecté. L'autre joueur s'est déconnecté | 
| SHUTDOWN | NULL | Le serveur s'est arrêté |  
| TURN | NULL | C'est a ton tour de jouer (faire getState et autoriser placement) |
| ROLE | observer ou player | observer si observateur, player si joueur. Indique au client son role |
| END | win ou loose ou rien | win si le joueur a gagné, loose sinon, ou rien si envoye a un observer. Indique la fin d'une partie | 

## Gestion de plusieurs parties

Lors de la reception d'un paquet End, le client peut renvoyer CONNECT. Les deux premier CONNECT reçus par le serveur seront les joueurs. 
