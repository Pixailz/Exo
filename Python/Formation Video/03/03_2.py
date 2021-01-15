#!/usr/bin/env python3

"""
EXERCUC PYTHON #3
> Créer un programme simulant un combat qui respecte
les contraintes suivantes :
    - Deux joueurs, auquels on demandera de choisir un pseudo
    - Les deux combattants démarrent avec 250 PV chacun
    - Le combat se déroule en 4 attaques (J1, J2, J1 et J2)
    - chaque attaque est une tentative (si elle réussit,
    le joueur infligera un nombre de dégâts entre 0 et 100,
    si elle échoue, l'attaque est ratée, et c'est au tour
    de l'autre joueur)
    - À la fin du combat (les 4 attaques), on déclare le
    gagnat (celui à qui il reste le plus de points de vie)

> Indications :
    - Le déroulement du combat doit être logique et annoncé
    à l'utilisateur (afficher du texte, décrivez ce qu'il se
    passe)
    - Coder dans un premier temps uniquement avec des 
    affichages / saisies, variables, opérations, conditions.
    - Pour les plus avancés, vous pourrez optimiser ce code
    ensuite en l'adaptant avec vos connaissances (boucles, 
    fonctions, classe, etc.)
"""

import random

class Player():
  def __init__(self, name, hp=250, isFirst=False):
    self.name = name
    self.hp = hp
    self.isFirst = isFirst

  def defend(self, attacker):
    pass
random_attack = True
random_damage = 0

print("\nLE COMBAT COMMENCE !\n")

p1 = input("Player 1 name : ")
player1 = Player(name=p1)
p2 = input("Player 2 name : ")
player2 = Player(name=p2)

swapPlayer = bool(random.randint(0, 1))

if swapPlayer == True:
  bak = player1.name
  player1.name = player2.name
  player2.name = bak

print("{} va commencer a attaquer.".format(player1.name))

i = 0
while i < 2:
  i += 1

  random_attack = bool(random.randint(0, 1))

  if random_attack == True:
    random_damage = random.randint(0, 100)
    player2.hp = player2.hp - random_damage
    print("Attaque reussi, -{} pour {}".format(random_damage, player2.name))

  else:
    print("Attaque rater !, {} a eu chaud ..".format(player2.name))

  print("{} hp : {}\n{} hp : {}".format(player1.name, player1.hp, player2.name, player2.hp))

  random_attack = bool(random.randint(0, 1))

  if random_attack == True:
    random_damage = random.randint(0, 100)
    player1.hp = player1.hp - random_damage
    print("Attaque reussi, -{} pour {}".format(random_damage, player1.name))

  else:
    print("Attaque rater !, {} a eu chaud ..".format(player1.name))

  print("{} hp : {}\n{} hp : {}".format(player1.name, player1.hp, player2.name, player2.hp))