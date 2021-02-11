#coding:utf-8

"""
32 cartes :
    - 8 cartes (1) de la « couleur » Trèfle
    - 8 cartes (2) de la « couleur » Carreau
    - 8 cartes (3) de la « couleur » Cœur
    - 8 cartes (4) de la « couleur » Pique.
"""

phase = 0

def debog():

    global phase
    phase += 1

    print(f"\nBEGIN #{phase}")

    if len(jeux_de_cartes) != 0:
        print("jeux_de_cartes\n")
        for value in jeux_de_cartes:
            print(value)

    if len(main_player_A) != 0:
        print("\nmain_player_A")
        for value in main_player_A:
            print(value)

    if len(main_player_A) != 0:
        print("\nmain_player_B")
        for value in main_player_B:
            print(value)
    
    print(f"\nEND #{phase}")

##
# HEADER

import random

jeux_de_cartes = list()

main_player_A = list()
main_player_B = list()

enjeux = list()

 #
##

def init_game():

    for x in range(7, 14 + 1):

        for y in range(1, 4+1):

            if y == 1:
                jeux_de_cartes.append((x,"Trèfle")) 
            elif y == 2:
                jeux_de_cartes.append((x,"Carreau")) 
            elif y == 3:
                jeux_de_cartes.append((x,"Cœur")) 
            elif y == 4:
                jeux_de_cartes.append((x,"Pique"))

    random.shuffle(jeux_de_cartes)

    while len(jeux_de_cartes) != 0:

        if bool(len(jeux_de_cartes) % 2):

            main_player_B.append(jeux_de_cartes.pop())

        else:

            main_player_A.append(jeux_de_cartes.pop())

def draw():

    global carte_player_A
    global carte_player_B

    carte_player_A = main_player_A.pop()
    carte_player_B = main_player_B.pop()

    print(f"Joueur A : {carte_player_A[0]} de {carte_player_A[1]}\tJoueur B : {carte_player_B[0]} de {carte_player_B[1]}")

    return (carte_player_A, carte_player_B)

def prendre_carte(player):

    if player == "A":
        
        main

    elif player == "B":
        pass

def Round():

    enjeux_A = tuple()
    enjeux_B = tuple()

    #debog()

    enjeux_A, enjeux_B = draw()

    enjeux.append(enjeux_A)
    enjeux.append(enjeux_B)


    if carte_player_A[0] > carte_player_B[0]:

        print("Le joueur A remporte les cartes")
        prendre_carte(player="A")

    elif carte_player_A[0] < carte_player_B[0]:

        print("Le joueur B remporte les cartes")
        prendre_carte(player="B")
        

    else:

        bataille = True
        print("Bataille !!!")
        #Round()

def main():

    init_game()

    while len(main_player_A) != 0 or len(main_player_A) !=0:
        Round()

main()