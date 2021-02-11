#coding:utf-8

def printliste():
    
    for value in liste:
        print(value, end="#")

import random

liste = list()


for x in range(1, 100+1):

    liste.append(x)

printliste()
print("")

while len(liste) != 0:


