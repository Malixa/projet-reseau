# Morpion aveugle 

## TODO

* Coder protocole(Clovis)
* Coder serveur  (Clovis)
* Coder client  (Célia)
* Ajouter bot (???)


## Protocole 

Plusieurs commandes envoyées au serveurs, entrainant toujours une réponse (ou confirmation de sa part).
Pour confirmer le serveur renvoie "OK" au client.

| Commande client au serveur | Arguments | Effet | Réponse | Action joueur |
|----------|-----------|-------|---------|---------------|
| CONNECT | NULL | Entraine initialisation du joueur coté serveur | OK | NON |
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
| DISCONNECTED | NULL | L'autre joueur s'est déconnecté | 
| SHUTDOWN | NULL | Le serveur s'est arrêté |   