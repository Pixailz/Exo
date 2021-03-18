#!/usr/bin/env python3
#coding:utf-8

#
# HEADER

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
                plateau.plateau_set_opponent("white")

            else:
                self.current_player = "black"
                plateau.plateau_set_opponent("black")

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

                elif plateau_return_code == "CannotPlay":
                    print(f"Error: La case {self.entry} ne contient pas de case ennemie adjacentes")
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
        self.rules_error = str()
        self.plateau_check_entry()
        self.plateau_create()

    def plateau_set_opponent(self, player):
        self.player = player

        if player == "white":
            self.opponent = "black"

        else:
            self.opponent = "white"

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

    def plateau_rules_already_played(self, axeX, axeY):
        if self.plateau[axeX][axeY].case_return_type() not in "void":
            return True
        else:
            return False

    def plateau_rules_can_play(self, axeX, axeY):

        check = 0

        for a in range(-1, 1+1):
            for b in range(-1, 1+1):
                if self.plateau[axeX+a][axeY+b].case_return_type() == self.opponent:
                    check += 1

        return bool(check)

    def plateau_rules_check_dir(self, dirX, dirY):
        to_turn = list()
        have_to_turn = 0
        axeX = self.axeX + dirX
        axeY = self.axeY + dirY

        if self.plateau[axeX + dirX][axeY + dirY].case_return_type() == self.player:

            print("To be turned")
            print(f"{axeX},{axeY}\t{self.plateau[axeX][axeY].case_return_type()}")
            to_turn.append((axeX, axeY))
            have_to_turn += 1

        elif self.plateau[axeX + dirX][axeY + dirY].case_return_type() == self.opponent:

            axeX = axeX + dirX
            axeY = axeY + dirY

            to_borderX = (self.entry - 1) - (axeX)
            to_borderY = (self.entry - 1) - (axeY)

            if to_borderX <= to_borderY:
                min_to_border = to_borderX

            elif to_borderX > to_borderY:
                min_to_border = to_borderY

            is_first = True
            for a in range(min_to_border):
                if self.plateau[axeX + dirX * a][axeY + dirY * a].case_return_type() == self.player:
                    if is_first:
                        to_turn.append((axeX, axeY))
                        to_turn.append((axeX + dirX * a, axeY + dirY * a))
                        is_first = False
                        have_to_turn += 1
                    else:
                        to_turn.append((axeX + dirX * a, axeY + dirY * a))
                        have_to_turn += 1

                if self.plateau[axeX + dirX * a][axeY + dirY * a].case_return_type() == self.opponent:

                    if is_first:
                        to_turn.append((axeX - dirX, axeY - dirY))
                        to_turn.append((axeX + dirX * a, axeY + dirY * a))
                        is_first = False
                    else:
                        to_turn.append((axeX + dirX * a, axeY + dirY * a))
        if bool(have_to_turn):
            return(True, to_turn)
        else:
            return False


    def plateau_rules_return_pawn(self):

        self.to_turn = list()
        self.dir_to_check = list()

        for a in range(-1, 1 + 1):
            for b in range(-1, 1 + 1):
                if self.plateau[self.axeX+a][self.axeY+b].case_return_type() == self.opponent:
                    self.dir_to_check.append((a, b))

        for a in self.dir_to_check:
            have_to_turn = self.plateau_rules_check_dir(a[0], a[1])
            if have_to_turn:
                for b in have_to_turn[1]:
                    self.to_turn.append((b[0], b[1]))

        for a in self.to_turn:
            self.plateau[a[0]][a[1]].case_type_set(self.player)

    def plateau_play(self, player, axeX, axeY):
        self.player = player
        self.axeX = axeX
        self.axeY = axeY

        if self.plateau_rules_already_played(self.axeX, self.axeY):
            return "AlreadyPlayed"

        else:
            if self.plateau_rules_can_play(self.axeX, self.axeY):
                self.plateau[axeX][axeY].case_type_set(self.player)
                self.plateau_rules_return_pawn()

            else:
                return "CannotPlay"

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

    def case_legal_set(self):
        pass

    def case_legal_unset(self):
        pass

    def case_return_char(self):
        return self.case_char

    def case_return_type(self):
        return self.case_type

    def case_type_set(self, t):
        self.case_type = t
        self.case_parse_type()

p1 = Partie()
