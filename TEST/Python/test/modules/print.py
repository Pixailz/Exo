#!/usr/bin/env python3
#coding:utf-8

"""Modules pour afficher en couleur (SIMPLE)"""

rouge = '\033[31m'
vert = '\033[32m'
reset = '\033[0m'

def info(text):
    print(vert + "[  INFO  ]" + reset, text)

def warning(text):
    print(rouge + "[WARNING ]" + reset, text)

if __name__ == "__main__":
    info("test_info")
    warning("test_warning")
