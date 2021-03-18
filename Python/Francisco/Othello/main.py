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

        if self.player == "white":
            self.opponent = "black"

        else:
            self.opponent = "white"

        check = 0

        for a in range(-1, 1+1):
            for b in range(-1, 1+1):
                if self.plateau[axeX+a][axeY+b].case_return_type() == self.opponent:
                    check += 1

        return bool(check)

    def plateau_rules_return_pawn(self):
        for a in range(-1, 1+1):
            for b in range(-1, 1+1):
                if self.plateau[self.axeX+a][self.axeY+b].case_return_type() == self.opponent:
                    if self.plateau[self.axeX+(a*2)][self.axeY+(b*2)].case_return_type() == self.player:
                        self.plateau[self.axeX+a][self.axeY+b].case_type_set(self.player)
        """
        if self.plateau[self.axeX+1][self.axeY].case_return_type() == self.opponent:
            # HAUT
            if self.plateau[self.axeX+2][self.axeY].case_return_type() == self.player:
                self.plateau[self.axeX+1][self.axeY].case_type_set(self.player)

        if self.plateau[self.axeX][self.axeY+1].case_return_type() == self.opponent:
            # DROITE
            if self.plateau[self.axeX][self.axeY+2].case_return_type() == self.player:
                self.plateau[self.axeX][self.axeY+1].case_type_set(self.player)

        if self.plateau[self.axeX-1][self.axeY].case_return_type() == self.opponent:
            # BAS
            if self.plateau[self.axeX-2][self.axeY].case_return_type() == self.player:
                self.plateau[self.axeX-1][self.axeY].case_type_set(self.player)

        if self.plateau[self.axeX][self.axeY-1].case_return_type() == self.opponent:
            # GAUCHE
            if self.plateau[self.axeX][self.axeY-2].case_return_type() == self.player:
                self.plateau[self.axeX][self.axeY-1].case_type_set(self.player)
                print(self.plateau[self.axeX][self.axeY-1].case_return_char())
                print(self.plateau[self.axeX][self.axeY-1].case_return_type())
                print(self.player)
        """
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

    def case_parse_legal(self):
        pass

    def case_return_char(self):
        return self.case_char

    def case_return_type(self):
        return self.case_type

    def case_type_set(self, t):
        self.case_type = t
        self.case_parse_type()

p1 = Partie()
