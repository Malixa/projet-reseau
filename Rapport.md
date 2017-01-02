# Rapport de réalisation - Projet Morpion en réseau

## I. Sujet/objectif du projet

L’objectif du projet est de réaliser en binômes un jeu de morpion aveugle en réseau.
Le projet doit se concrétiser sous la forme d'un logiciel python présentant deux modes de fonctionnement:
* Si l'utilisateur lance le programme sans argument, le logiciel s'exécute en mode serveur.
* Si l'utilisateur précise une adresse ip en argument, le logiciel se lance en mode client.

## II. Lexique 

| Terme | Définition |
|-|-|
| Client | ici, logiciel permettant à un utilisateur de se connecter à un serveur et d'interragir avec ce dernier, afin de participer à des parties de morpion. |
| Serveur | Logiciel chargé de mettre en comunication plusieurs clients et de gérer le déroulement de la partie. |
| Joueur | Client disposant de la possibilité de jouer au jeu du morpion sur un serveur (2 joueurs par serveur). |
| Observateur | Client ne pouvant jouer au jeu du morpion sur un serveur. A la place, il reçoit l'état de la partie à chaque fois qu'un joueur joue un coup (une infinité d'observateurs par serveur). |

## III. Règles de jeu

Chaque joueur joue tour à tour. Durant son tour de jeu, un client peut choisir de poser un jeton sur la grille ou de quitter la partie en entrant 'exit' dans l'invité de commande.   
Si le joueur pose un pion:
* Si le joueur peut jouer sur la case, alors un pion sera placé et se sera au tour du joueur suivant. 
* Sinon la case n'est pas disponible car l'autre joueur l'occupe deja.  Dans ce cas, le joueur découvre le pion adverse qui devient visible sur sa grille, et le joueur passe son tour. 

Si le joueur quitte le jeu (en tapant exit, ou pour toute autre raison), un compte-à-rebours est lancé. Le joueur a trois minute pour se reconnecter sinon, le serveur sera relancé afin de permettre à d'autres clients de jouer. 

Si un joueur arrive a placer 3 pions en ligne, colonne ou diagonale, il est déclaré vainqueur. L'autre joueur est donc perdant. Une fois la victoire annoncée, les joueurs et observateurs peuvent essayer de se reconnecter au serveur. Premier connecté, premier servit, les deux premiers clients connectés seront joueurs.

## IV. Description des modes de fonctionnement 

### Mode Serveur 

En mode serveur, le logiciel propose un point d'ancrage permettant à deux clients de jouer au morpion en ligne, ou d'observer deux joueurs s'affronter.

### Mode client 

En mode client, le logiciel peut se connecter à un serveur. Ce dernier transmet au client son status (joueur/observateur). Si il est joueur et que le nombre de joueur connecté au serveur est suffisant, le client peut transmettre des coups au serveur qui l'informe de l'état de la partie, donne la main à l'autre joueur et ainsi de suite. Si il est observateur le client recoit l'état de la partie à chaque coup placé par les joueurs.

## IV. Fonctionalité

### Fonctionalités implémentées

| Intitulé | Description |
|--|--|
| Connexion de participants/Gestion joueur/observateur | Si le nombre de joueurs est inférieur à 2, le nouveau client connecté est considéré comme joueur. Tant que le nombre de joueur est inférieur à 2, le joueur connecté est en attente. Si deux joueurs sont connecté la partie commence. Tout les clients qui se connecterons plus tard seront considérés comme observateurs. |
| Déroulement du jeu | Les clients considérés comme joueur peuvent communiquer au serveur les coups qu'ils souhaitent jouer à tour de rôle jusqu'à la fin de la partie. Lorsque la partie est terminée, les clients observateurs sont notifiés de la fin de la partie et les clients joueurs sont mis au courant de leur situation (gagnant/perdant). | 
| Possibilité de jouer plusieurs parties | Lorsqu'une partie est terminée, tout les status sont remis à zéro. Le serveur attend de nouveaux paquets 'CONNECT' de la part des clients connectés. Les deux premiers reçus seront considérés comme joueurs. En revanche, les scores ne sont pas comptés étant donné que les status joueur/observateur changent à chaque partie. Nous ne considérions pas la conservation de score comme pertinente. | 
| Gestion de l'interruption de la connexion entre les clients et le serveur (Crash ou déconnexion) | Si le client déconnecté (pour quelque raison que ce soit) est un des deux joueurs, le serveur attend un certain temps la reconnexion du joueur. Si il ne se reconnecte pas, la partie est relancée et tout les clients sont expulsés du serveur. Si le client est un simple observateur, le serveur ne réalise aucune action autre que libérer ses données. | 

#### Fonctionalités non-implémentées

| Intitulé | Description |
|--|--|
| Robot jouant aléatoirement des coups | Etant donné l'architecture de notre projet, nous avons jugé que la modification du code pour permettre l'ajout d'un robot aurait excessivement complexifié le code en générant des exceptions de traitement (cas particuliers). | 

## V. Informations technique





