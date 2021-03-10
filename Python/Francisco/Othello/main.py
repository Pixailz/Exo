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

def alpha_to_num(alpha):

    alpha = alpha.upper()
    return ord(alpha) - 64

def num_to_alpha(num):

    return chr(64+num)

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
                    bb = num_to_alpha(b+1)
                    aa = a+1
                    placed_white.append(f"W:{aa},{bb}")

                elif self.plateau[a][b] == black:
                    bb = num_to_alpha(b+1)
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
                a = num_to_alpha(a + 1)
                print(a)
            else:
                a = num_to_alpha(a + 1)
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

    def play(self, player, *pos):

        axeX = pos[0] - 1
        axeY = alpha_to_num(pos[1]) - 1

        if player == white:
            self.check()
            self.plateau[axeX][axeY] = white
            axeXY = f"{axeX}{axeY}"
            self.placed_white.append(axeXY)

        elif player == black:
            self.plateau[axeX][axeY] = black
            axeXY = f"{axeX}{axeY}"
            self.placed_black.append(axeXY)
            self.check()



if __name__ == "__main__":
    p1 = Plateaux()
    p1.print_plateau()
    p1.play(white, 2, "a")
    p1.print_plateau()
    p1.play(black, 2, "a")
    p1.print_plateau()
