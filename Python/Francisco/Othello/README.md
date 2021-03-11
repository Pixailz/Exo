# Othello

## Sujet : créer un programme permettant de jouer au jeu Othello

Le jeu de société Othello (ou Reversi) est un jeu abstrait ancien à deux joueurs, qui se joue avec des
pions sur une grille (chaque joueur à une couleur de pions).
Le jeu se joue de la manière suivante : à son tour, un joueur ajoute un pion de sa couleur sur une
case vide de la grille. Si deux pions de sa couleur encadrent des pions de la couleur adverse, les pions
adverses changent de couleur. La partie est gagnée quand tous les pions du plateau sont de la même
couleur.

Les règles du jeu de base se trouvent [ici](http://www.ffothello.org/othello/regles-du-jeu/)

Le code doit être commenté correctement et doit être le plus efficace possible.
Le programme et son évaluation sont séparés en 4 parties. L’ensemble des parties n’est pas
obligatoire pour avoir la note maximale !
Il est conseillé de finir une partie entièrement avant de passer à la suivante. Les parties 3a et 3b sont
au choix (vous faites l’une ou l’autre).

## Partie 1
Pour cette partie, l’affichage se fera dans la console, les coups seront choisis dans un menu (poser
un pion x, poser un pion o, ou passer). On ne fera pas de vérification que le coup est valide
(transformation obligatoire).
- Afficher une grille d’Othello de taille 8x8 (voir schéma)
- Afficher des pions de différentes couleurs (x ou o) et afficher la position de départ
Vous devez avoir quelque chose d’équivalent à cela ->
- Permettre de jouer un pion (x ou o) uniquement si la case est vide
- Retourner les pions adverses si besoin
- Lancer la fin de partie si tous les pions sont de la même
couleur et afficher le gagnant

## Partie 2

Dans cette partie, on implémentera toutes les règles du jeu et certaines variantes.
- Vérification de la validité du coup avant de l’afficher, sinon on redemande un coup
- Gestion des tours : on doit jouer alternativement !
- Demande de la taille du plateau au début de la partie
Pour la partie 3, vous devez choisir entre la 3a (interface graphique avec TkInter) ou la 3b (utilisation
de concepts objet).

## Partie 3

### A
Cette partie consiste à utiliser le module TkInter pour créer une interface graphique pour votre
projet. L’interface graphique doit comprendre deux écrans :
- Un écran d’accueil avec un bouton de lancement d’une partie et un champ pour
sélectionner la taille de la grille
- Un écran de jeu avec la grille et les pions affichés. Pour jouer un coup, vous avez le choix
entre laisser le joueur entrer le numéro de la case dans un champ de texte, ou utiliser le clic
de souris sur une case.

### B
Cette partie consiste à modifier votre code pour utiliser les concepts de la programmation objet.
Vous devez faire les modifications suivantes :
- Ajout d’une classe Partie qui gère le déroulement global de la partie en cours
- Ajout d’une classe Plateau qui est chargée de la vérification des coups, des modifications de
pièces et de la vérification de fin de partie
- Ajout d’une classe Case qui représente une case du plateau, et qui peut contenir un pion x,
un pion o, ou rien. Chaque Plateau est constitué de plusieurs Cases.
Vous pouvez rajouter d’autres classes si vous en ressentez le besoin.

## Partie 4 (bonus)

Dans cette partie, vous pouvez améliorer votre jeu de plusieurs manières. Chaque nouvelle
fonctionnalité rapportera des points ! Quelques exemples de fonctionnalités (dans le désordre) :
- Possibilité de charger ou d’enregistrer une partie (dans un fichier .txt ou JSON)
- Possibilité d’annuler un coup
- Mise en surbrillance des cases où le joueur actif peut jouer de manière légale

Documentation et références
- Documentation de Python 3 : https://docs.python.org/fr/3/
- Cours dans LinkedIn Learning sur Python 3 et l’objet :
  - https://www.linkedin.com/learning/l-essentiel-de-python-3/bienvenue-dans-lessentiel-de-python-3
  - https://www.linkedin.com/learning/decouvrir-python-3/bienvenue-dans-decouvrirpython-3
- Cours sur OpenClassrooms sur l’objet en Python
  - https://openclassrooms.com/fr/courses/4302126-decouvrez-la-programmationorientee-objet-avec-python
- Documentation sur TkInter :
  - voir fichiers “InterfacesGraphiques.pdf” et “tp4_python.pdf” sur la page de cours
MyLearningBox
  - sur OpenClassRooms (intro à TkInter) :
https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-enpython/234859-creez-des-interfaces-graphiques-avec-tkinter


## TODO
- sanitarize more
- add statements if two point are surounded by other player

