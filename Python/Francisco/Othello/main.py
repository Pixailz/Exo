#!/usr/bin/env python3
#coding:utf-8

#
# HEADER
<<<<<<< HEAD

 #
#

def alpha_to_num(alpha):
    alpha = alpha.upper()
    return ord(alpha) - 64

def num_to_alpha(num):
    return chr(64+num)

class Partie():

    def __init__(self):

        plateau = Plateau()

        self.playing = True
        self.turn = 0

        while self.playing:

            self.turn += 1
            self.sanitarize_input_error = str()
            self.entryX = int()
            self.entryY = int()
            plateau.plateau_print()

            if self.turn % 2:
                self.current_player = "white"
            else:
                self.current_player = "black"

            if self.current_player == "white":
                print("Au tour des Blanc")

            elif self.current_player == "black":
                print("Au tour des Noir")

            self.entry = input("-> ")
            self.sanitarize_input_error = self.sanitarize_input()

            if not self.sanitarize_input_error:
                plateau_return_code = plateau.plateau_play(self.current_player, self.entryX, self.entryY)

                if plateau_return_code == "AlreadyPlayed":
                    print(f"Error: La case {self.entry} a déja été jouer")
                    self.turn -= 1

            else:
                print("Exemple : 1A")
                self.turn -= 1

        print("Stopping ...")

    def sanitarize_input(self):
        entry_len = len(self.entry)
        entry_count_alpha = 0
        entry_count_num = 0
        check_pass = False

        for char in self.entry:
            if char in "abcdefghijklmnopqrstuvvwxyz":
                entry_count_alpha += 1

            if char in "0123456789":
                entry_count_num += 1

        if entry_count_alpha + entry_count_num != entry_len:
            print("Error: Votre choix comporte de mauvais caractères")
            return True

        elif entry_count_alpha > entry_len / 2:
            print("Error: Votre choix comporte trop de lèttres")
            return True

        elif entry_count_num > entry_len / 2:
            print("Error: Votre choix comporte trop de chiffre")
            return True

        elif entry_len == 0:
            print("Error: Votre choix est vide")
            return True

        else:
            pos1 = self.entry[0]
            pos2 = self.entry[1]

            try:
                pos1 = int(pos1)

            except ValueError:
                pos2 = int(pos2)

            if type(pos1) == type(int()):
                pos2 = alpha_to_num(pos2)
                self.entryX = pos1 - 1
                self.entryY = pos2 - 1

            else:
                pos1 = alpha_to_num(pos1)
                self.entryX = pos2 - 1
                self.entryY = pos1 - 1

class Plateau():

    def __init__(self):

        self.entry = str()
        self.plateau = list()

        self.plateau_check_entry()
        self.plateau_create()

    def plateau_check_entry(self):

        checked = False

        while not checked:

            try:
                print("Taille du plateau, nombre pair :")
                #self.entry = int(input("-> "))
                self.entry = 8

            except ValueError:
                print("Entrer un nombre")
                continue

            if self.entry % 2 == 1:
                print("Entrer un nombre pair")

            else:
                checked = True

    def plateau_create(self):

        self.plateau.clear()

        for a in range(self.entry):
            row = list()

            for b in range(self.entry):

                if (a == self.entry / 2 and b == self.entry / 2) or\
                    (a + 1 == self.entry / 2 and b + 1 == self.entry / 2 ):
                    row.append(Case("black"))

                elif (a + 1 == self.entry / 2 and b == self.entry / 2) or\
                    (a == self.entry / 2 and b + 1 == self.entry / 2):
                    row.append(Case("white"))

                else:
                    row.append(Case("void"))

            self.plateau.append(row)

    def plateau_print(self):

        print("")
        for a in range(self.entry):
            if a == 0:
                print(f"   {num_to_alpha(a+1)}", end="")

            else:
                print(f" {num_to_alpha(a+1)}", end="")

        print("")

        for a in range(self.entry):
            for b in range(self.entry):
                if b + 1 == self.entry:
                    print(f"{self.plateau[a][b].case_return_char()}")

                elif b == 0:
                    if a+1 < 10:
                        print(f"{a+1}  {self.plateau[a][b].case_return_char()} ", end="")

                    else:
                        print(f"{a+1} {self.plateau[a][b].case_return_char()} ", end="")
                else:
                    print(f"{self.plateau[a][b].case_return_char()} ", end ="")

    def plateau_play(self, player, axeX, axeY):

        if self.plateau[axeX][axeY].case_return_type() not in "void":
            return "AlreadyPlayed"

        else:
            self.plateau[axeX][axeY].type_set(player)

class Case():

    def __init__(self, t):
        self.case_type = t
        self.case_parse_type()

    def case_parse_type(self):

        if self.case_type == "void":
            self.case_char = "."

        elif self.case_type == "white":
            self.case_char = "O"

        elif self.case_type == "black":
            self.case_char = "X"

    def case_return_char(self):
        return self.case_char

    def case_return_type(self):
        return self.case_type

    def type_set(self, t):
        self.case_type = t
        self.case_parse_type()

p1 = Partie()
=======
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
>>>>>>> 4cc5c03c20a3057c3e606c050aba954aca27044a
