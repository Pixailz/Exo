#!/usr/bin/env python3
#coding:utf-8

#
# HEADER
row = 8
column = 8

void = "."
white = "0"
black = "X"
 #
#

#
# GLOBAL SCOPE VAR
plateau = list()
turn = int()
entry = str()
entryX = str()
entryY = str()

sanitarize_input_error = False
playing = True
#
#

def init():
    global row
    for a in range(row):
        row = list()
        for b in range(column):
            row.append(void)
        plateau.append(row)

def sanitarize_input():
    global entry, entryX, entryY, sanitarize_input_error
    global turn

    entry_len = len(entry)
    entry_count_alpha = 0
    entry_count_num = 0
    check_pass = False

    for char in entry:
        if char in "abcdefghijklmnopqrstuvvwxyz":
            entry_count_alpha += 1

        if char in "0123456789":
            entry_count_num += 1

    if entry_count_alpha + entry_count_num != entry_len:
        print("Error: Choice have bad char")

    elif entry_count_alpha > entry_len / 2:
        print("Error: Too many Alpha")

    elif entry_count_num > entry_len / 2:
        print("Error: Too many Numeric")

    else:
        check_pass = True

    if check_pass:
        pos1 = entry[0]
        pos2 = entry[1]

        try:
            pos1 = int(pos1)

        except ValueError:
            pos2 = int(pos2)

        if type(pos1) == type(int()):
            entryX = pos1
            entryY = pos2

        else:
            entryX = pos2
            entryY = pos1

    else:
        print("Exemple : 1a")
        sanitarize_input_error = True

def alpha_to_num(alpha):
    alpha = alpha.upper()
    return ord(alpha) - 64

def num_to_alpha(num):
    return chr(64+num)

def check_already_placed(x, y):
    if plateau[x][y] == void:
        return True
    else:
        return False

def play(player, entryX, entryY):
    global turn
    axeX = entryX - 1
    axeY = alpha_to_num(entryY) - 1

    if player == white:
        if check_already_placed(axeX, axeY):
            try:
                plateau[axeX][axeY] = white

            except IndexError:
                print("Error: choice out-of-range")
                turn -= 1

        else:
            print("Error: choice already played")
            turn -= 1

    elif player == black:
        if check_already_placed(axeX, axeY):
            try:
                plateau[axeX][axeY] = black

            except IndexError:
                print("Error: choice out-of-range")
                turn -= 1

        else:
            print("Error: choice already played")
            turn -= 1

def print_plateau():
    print("")
    print("X  ", end="")
    for a in range(len(plateau[0])):
        if a + 1 == len(plateau[0]):
            a = num_to_alpha(a + 1)
            print(a)

        else:
            a = num_to_alpha(a + 1)
            print(f"{a} ", end="")

    for a in range(len(plateau)):
        for b in range(len(plateau[a])):
            if b+1 == len(plateau[a]):
                print(f"{plateau[a][b]}")

            elif b == 0:
                if a + 1 < 10 :
                    print(f"{a+1}  {plateau[a][b]} ", end="")

                else:
                    print(f"{a+1} {plateau[a][b]} ", end="")

            else:
                print(f"{plateau[a][b]} ", end="")

def game():
    while playing:
        global turn, entry, entryX, entryY, sanitarize_input
        turn += 1
        print_plateau()

        if turn % 2:
            entry = input("W-> ")
            sanitarize_input()

            if not sanitarize_input_error:
                play(white, entryX, entryY)
            else:
                turn -= 1

        else:
            entry = input("B-> ")
            sanitarize_input()

            if not sanitarize_input_error:
                play(black, entryX, entryY)
            else:
                turn -= 1

init()
game()
