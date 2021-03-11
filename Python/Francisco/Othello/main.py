#!/usr/bin/env python3
#coding:utf-8

#
# HEADER
side_char = "#"
void = "."
white = "0"
black = "X"
 #
#

class Plateaux():
    def __init__(self):
        self.row = 8
        self.column = 8
        self.placed_white = list()
        self.placed_black = list()
        self.plateau = list()
        self.create_plateau()

    def create_plateau(self):
        for a in range(self.row):
            row = list()
            for b in range(self.column):
                row.append(void)
            self.plateau.append(row)

    def print_played(self):
        print("")
        placed_white = list()
        placed_black = list()
        for a in range(len(self.plateau)):
            for b in range(len(self.plateau[a])):
                if self.plateau[a][b] == white:
                    bb = self.num_to_alpha(b+1)
                    aa = a+1
                    placed_white.append(f"W:{aa},{bb}")

                elif self.plateau[a][b] == black:
                    bb = self.num_to_alpha(b+1)
                    aa = a+1
                    placed_black.append(f"B:{aa},{bb}")
        for item in placed_white:
            print(item)
        for item in placed_black:
            print(item)

    def print_plateau(self):
        print("")
        print("X  ", end="")
        for a in range(len(self.plateau[0])):
            if a + 1 == len(self.plateau[0]):
                a = self.num_to_alpha(a + 1)
                print(a)
            else:
                a = self.num_to_alpha(a + 1)
                print(f"{a} ", end="")
        for a in range(len(self.plateau)):
            for b in range(len(self.plateau[a])):
                if b+1 == len(self.plateau[a]):
                    print(f"{self.plateau[a][b]}")
                elif b == 0:
                    if a + 1 < 10 :
                        print(f"{a+1}  {self.plateau[a][b]} ", end="")
                    else:
                        print(f"{a+1} {self.plateau[a][b]} ", end="")
                else:
                    print(f"{self.plateau[a][b]} ", end="")
        self.print_played()
        print(self.placed_white)
        print(self.placed_black)

    def check_already_placed(self, pos):
        if pos not in self.placed_black and pos not in self.placed_white:
            return True
        else:
            return False

    def play(self, player, entryX, entryY):
        axeX = entryX - 1
        axeY = self.alpha_to_num(entryY) - 1
        if player == white:
            axeXY = f"{axeX}{axeY}"
            if self.check_already_placed(axeXY):
                try:
                    self.plateau[axeX][axeY] = white
                    self.placed_white.append(axeXY)
                except IndexError:
                    print("Error: choice out-of-range")
                    self.turn -= 1
            else:
                print("Error: choice already played")
                self.turn -= 1
        elif player == black:
            axeXY = f"{axeX}{axeY}"
            if self.check_already_placed(axeXY):
                try:
                    self.plateau[axeX][axeY] = black
                    self.placed_black.append(axeXY)
                except IndexError:
                    print("Error: choice out-of-range")
                    self.turn -= 1
            else:
                print("Error: choice already played")
                self.turn -= 1


    def alpha_to_num(self, alpha):
        alpha = alpha.upper()
        return ord(alpha) - 64

    def num_to_alpha(self, num):
        return chr(64+num)

    def sanitarize_input(self):
        if len(self.entry) > 2:
            print("Error: Wrong Choice")
            self.turn -= 1
        else:
            pos1 = self.entry[0]
            pos2 = self.entry[1]
            try:
                pos1 = int(pos1)
            except ValueError:
                pos2 = int(pos2)
            if type(pos1) == type(int()):
                self.entryX = pos1
                self.entryY = pos2
            else:
                self.entryX = pos2
                self.entryY = pos1

    def game(self):
        self.playing = True
        self.turn = 0
        while self.playing:
            self.turn += 1
            if self.turn % 2:
                self.entry = input("W-> ")
                self.sanitarize_input()
                self.play(white, self.entryX, self.entryY)
                self.print_plateau()
            else:
                self.entry = input("B-> ")
                self.sanitarize_input()
                self.play(black, self.entryX, self.entryY)
                self.print_plateau()

if __name__ == "__main__":
    p1 = Plateaux()
    p1.game()
