#!/usr/bin/env python3

import os
from random import randrange
from math import ceil

moneyStarting = 1500

retry = True

while retry == True:
    currentMoney = moneyStarting
    while currentMoney > 0:
        os.system("cls")

        numberChoiceCheck = False
        numberChoice = ""

        while numberChoiceCheck == False:

            numberChoice = int(input("Choose a number (1-50):"))
            if numberChoice < 1 or numberChoice > 50:
                print("failed")
                numberChoiceCheck = False
            else:
                print("pass")
                numberChoiceCheck = True

        inbetChoiceCheck = False
        inbetChoice = ""

        while inbetChoiceCheck == False:
            print("How many do you wan't to bet (current money :", currentMoney, ")")
            inbetChoice = int(input())
            
            if inbetChoice > currentMoney:
                print("Not enought money")
                inbetChoiceCheck = False
            else:
                print("Let's bet", inbetChoice, "on the", numberChoice)
                currentMoney = currentMoney - inbetChoice
                inbetChoiceCheck = True

        print("Rolling the table ...")
        os.system("timeout 2 > nul")

        number = int(randrange(50))

        numberColor=""
        if number % 2 == 0:
            numberColor="BLACK"
        else:
            numberColor="RED"
        
        choiceColor=""
        if numberChoice % 2 == 0:
            choiceColor="BLACK"
        else:
            choiceColor="RED"

        print("The number is", number, "and the color is", numberColor)
        print("You Choose", numberChoice, "and your color was", choiceColor)

        if numberChoice == number:
            print("You rewarded X3 of your bet")
            print("(", inbetChoice, "X 3 =", inbetChoice *3, ")")
            print("Money before :", currentMoney)
            print("Money after  :", currentMoney + inbetChoice * 3)
        elif choiceColor == numberColor:
            print("You are rewarded by an half of your bet")
            print("(", inbetChoice, "/ 2 =", inbetChoice / 2, ")")
            print("Money before :", currentMoney)
            print("Money after  :", currentMoney + inbetChoice / 2)
        else:
            print("You have losing your bet")   
        os.system("timeout 2 > nul")
    print("You have lose ")

    retryChoiceCheck = False
    retryChoice=""

    while retryChoiceCheck == False:
        retryChoice = input("Retry ? (Y/n)")
        

    os.system("pause > nul")
