#!/usr/bin/env python3

def menu (name="default", size=0):
    
    print(name.center(55, "-"))
    
    i = 0
    while i < size:
    
        i += 1
        print("{}. tocome...".format(i))

menu(name="Menu Principal", size=7)
