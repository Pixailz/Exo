#!/usr/bin/env python3
#coding:utf-8

#
# HEADER
from random import randint
from random import shuffle
from time import sleep
 #
#

def debog_print(opt=None):

    print("BEGIN\n\n")

    if opt == None:
        print("Pa cards :\n")
        for card in deck_player_a:
            print(card)
        print("\nPb cards :\n")
        for card in deck_player_b:
            print(card)

    elif opt == "deck":
        for card in pack_of_cards:
            print(card)
        print("pack")

    print("\n\nEND\n")

#
# GLOBAL VAR
pack_of_cards = list()

deck_player_a = list()
deck_player_b = list()

winner_prize = list()
time_round = 2
 #
#

def create_pack():

    grade = str()

    for x in range(7, 14 + 1):

        if x == 1:
            grade = "Un"
        elif x == 2:
            grade = "Deux"
        elif x == 3:
            grade = "Trois"
        elif x == 4:
            grade = "Quatre"
        elif x == 5:
            grade = "Cinq"
        elif x == 6:
            grade = "Six"
        elif x == 7:
            grade = "Sept"
        elif x == 8:
            grade = "Huit"
        elif x == 9:
            grade = "Neuf"
        elif x == 10:
            grade = "Dix"
        elif x == 11:
            grade = "Valet"
        elif x == 12:
            grade = "Dame"
        elif x == 13:
            grade = "Roi"
        elif x == 14:
            grade = "As"

        for y in range(1, 4+1):
            if y == 1:
                color = "Trèfle"
            elif y == 2:
                color = "Carreau"
            elif y == 3:
                color = "Cœur"
            elif y == 4:
                color = "Pique"

            name = f"{grade} de {color}"
            power = x
            pack_of_cards.append((power, name))

    return pack_of_cards

def distribute_cards():

    print("Tossing a coin to know who's first.")
    print("HEADS : Player A\nTAILS : Player B\n...")

    sleep(0.5)

    whos_first = randint(0,1)

    if whos_first:

        print("this is HEADS A begin")
        whos_first = "a"

    else:

        print("this is TAILS B begin")
        whos_first = "b"

    print(bool(len(pack_of_cards) % 2))

    while len(pack_of_cards) != 0:

        if whos_first == "a":

            if bool(len(pack_of_cards) % 2):

                deck_player_b.append(pack_of_cards.pop())

            else:

                deck_player_a.append(pack_of_cards.pop())

        elif whos_first == "b":

            if bool(len(pack_of_cards) % 2):

                deck_player_a.append(pack_of_cards.pop())

            else:

                deck_player_b.append(pack_of_cards.pop())

def reverse_deck(opt=None):
    if opt == None:

        deck_player_a.reverse()
        deck_player_b.reverse()

    elif opt == "a":

        deck_player_a.reverse()

    elif opt == "b":

        deck_player_b.reverse()

def distribute_prize(winner, prize):

    if winner == "a":
        reverse_deck("a")

        for card in prize:
            #print(f"card added to deck a : {card}")
            deck_player_a.append(card)

        reverse_deck("a")

    elif winner == "b":

        reverse_deck("b")

        for card in prize:
            #print(f"card added to deck b : {card}")
            deck_player_b.append(card)

        reverse_deck("b")

def round():

    bataille, loop = False, True
    winner_prize = list()

    while loop:

        picked_card_a = deck_player_a.pop()
        picked_card_b = deck_player_b.pop()

        print(f"Joueur A : {picked_card_a[1]} \tJoueur B : {picked_card_b[1]}")

        winner_prize.append(picked_card_a)
        winner_prize.append(picked_card_b)

        if picked_card_a[0] == picked_card_b[0]:

            if len(deck_player_a) == 0 or len(deck_player_b) == 0:

                print("Match Nul !!!")
                print("C'est SUPER SUPER rare ..")
                exit()

            pass

        elif picked_card_a[0] > picked_card_b[0]:

            print("Joueur A remporte les cartes")
            distribute_prize("a", winner_prize)
            loop = False

        elif picked_card_a[0] < picked_card_b[0]:

            print("Joueur B remporte les cartes")

            distribute_prize("b", winner_prize)
            loop = False

def play_game():

    is_running = True

    while is_running:

        winner_prize = list()

        round()
        sleep(time_round)

        if len(deck_player_a) == 0:

            print("Player A Win !!")

        elif len(deck_player_b) == 0:

            print("Player B Win !!")
        #debog_print()

        #sleep(0.5)

def main():

    create_pack()

    shuffle(pack_of_cards)

    distribute_cards()
    play_game()

main()
