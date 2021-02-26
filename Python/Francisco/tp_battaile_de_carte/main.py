#!/usr/bin/env python3
#coding:utf-8

#
# HEADER
from random import randint
from random import shuffle as melange

"""
    for items in cartes_joueur_A:
        print(f"{items}")
    print("\n\n")
    for items in cartes_joueur_B:
        print(f"{items}")
"""
 #
#

def debog():

    print(f"{cartes_joueur_A[:]}")
    print(f"{cartes_joueur_A[:]}")

def creation_paquet():

    jeux_de_cartes = list()
    ## ADD CHAR INSTEAD OF INT

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

    return jeux_de_cartes

def distribuer_jeux_de_cartes(jeux_de_cartes): ## who's first()

    # affectation multiple
    cartes_joueur_A = cartes_joueur_B = list()

    # tant qu'il reste des cartes
    # ici j'utilise un petit tricks sur la taille du paquet
    while len(jeux_de_cartes) != 0:

        if bool(len(jeux_de_cartes) % 2):
            cartes_joueur_B.append(jeux_de_cartes.pop())

        else:
            cartes_joueur_A.append(jeux_de_cartes.pop())

    return cartes_joueur_A, cartes_joueur_B

def round(cartes_joueur_A, cartes_joueur_B):

    bataille, loop = False, True

    cartes_a_gagner = list()

    while loop:

        carte_joueur_A = cartes_joueur_A.pop()
        print(f"Joueur A : {carte_joueur_A[0]} de {carte_joueur_A[1]}")

        carte_joueur_B = cartes_joueur_B.pop()
        print(f"Joueur A : {carte_joueur_B[0]} de {carte_joueur_B[1]}")

        cartes_a_gagner.append(carte_joueur_A)
        cartes_a_gagner.append(carte_joueur_B)

        if carte_joueur_A[0] == carte_joueur_B[0]:

            print("BATTAILLE !!")
            gagnant = "bataille.."##

        elif carte_joueur_A[0] > carte_joueur_B[0]:
            print("Joueur A a gagner")

            for carte in cartes_a_gagner:
                cartes_joueur_A.append(carte)

            loop = False

        elif carte_joueur_A[0] < carte_joueur_B[0]:
            print("Joueur B a gagner")

            for carte in cartes_a_gagner:
                cartes_joueur_A.append(carte)

            loop = False

def play_game(cartes_joueur_A, cartes_joueur_B):

    enjeux = list()

    while cartes_joueur_A != 0 or cartes_joueur_B != 0:
        round(cartes_joueur_A, cartes_joueur_B)
        for items in cartes_joueur_A:
            print(f"{items}")
        print("\n\n")
        for items in cartes_joueur_B:
            print(f"{items}")

def main():

    # CREATION DU PAQUET DE CARTE
    jeux_de_cartes = creation_paquet()

    # MELANGATION DU PAQUET (fonction shuffle import ci-dessus)
    melange(jeux_de_cartes)

    cartes_joueur_A, cartes_joueur_B = distribuer_jeux_de_cartes(jeux_de_cartes)

    play_game(cartes_joueur_A, cartes_joueur_B)

main()
