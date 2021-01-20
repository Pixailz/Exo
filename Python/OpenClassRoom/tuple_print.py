#!/usr/bin/env python3

def afficher(*values, sep=" ", fin="\n"):
    values = list(values)
    print(len(values))
    for i, par in enumerate(values):
        values[i] = str(par)

    chaine = sep.join(values)
    chaine += fin

    print(chaine, end="")

afficher("Maeva", "Emilio", "Bruno", 1, 1000, sep=".", fin="E")
