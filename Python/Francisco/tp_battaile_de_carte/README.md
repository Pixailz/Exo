# TP BATAILLE DE CARTES
## Un jeu de 32 cartes constituer de :
<br>

- 8 cartes de la __couleur__ Trèfles
- 8 cartes de la __couleur__ Carreau
- 8 cartes de la __couleur__ Coeur
- 8 cartes de la __couleur__ Pique.

## Les 8 cartes de chaque couleur sont :
<br>

- Sept (valeur associée : 7)
- Huit (valeur associée : 8)
- Neuf (valeur associée : 9)
- Dix (valeur associée : 10)
- Valet (valeur associée : 11)
- Dame (valeur associée : 12)
- Roi (valeur associée : 13)
- As  (valeur associée : 14)


## Deroulement
Le jeu de la bataille (physique) se déroule ainsi : le jeu de
<br>
32 cartes est mélangé, puis réparti entre les deux joueurs
<br>
(qui ont donc au début 16 cartes chacun, empilées faces
<br>
cachées).
Chaque joueur retourne la première carte de sa
<br>pile, et celui qui affiche la carte de plus grande valeur
<br>
remporte les deux cartes : il positionne ces deux cartes à
<br>
la fin de sa pile de carte (l’ordre dans lequel ces deux
<br>
cartes sont rangées étant quelconque).
Si les deux cartes
<br>
affichées sont de même valeur, on dit alors qu’il y a
<br>
__bataille__ : chaque joueur retourne à nouveau la première <br>
carte de sa pile et la positionne sur la carte qu’il a <br>
précédemment jouée, et ainsi de suite jusqu’à ce que les
<br>
deux valeurs affichées soient différentes. Le joueur ayant
<br>
finalement affiché la carte de plus grande valeur remporte
<br>
la bataille et positionne toutes les cartes qui viennent
<br>
d’être jouées à la fin de sa pile (encore dans un ordre
<br>
quelconque).
Le jeu continue jusqu’à ce qu’un des
<br>
deux joueurs n’ait plus de carte à jouer, et celui-ci a alors
<br>
perdu la partie.

## Affichage

L’affichage d’une étape simple de la partie se fera selon
<br>
le modèle suivant :
```
Joueur A : Huit de Pique Joueur B : Valet de Trèfle
Le joueur B remporte les cartes.
```
L’affichage d’une bataille se fera selon le modèle suivant :
```
Joueur A : Huit de Pique Joueur B : Huit de Trèfle
Joueur A : Valet de Coeur Joueur B : Valet de Trèfle
Joueur A : Dix de Pique Joueur B : Sept de Trèfle
Le joueur A remporte les cartes.
```
A la fin de la partie, on affichera le gagnant (ou, cas très
<br>
rare : match nul).
