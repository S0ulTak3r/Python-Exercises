#!/usr/bin/python
import sys

def drawBoardInput():
    inpt=int(input("input what board size you want to draw, aka 3x3 and etc, give 1 number: "))

    counter=0

    while (counter!=inpt):
        print(" --- " * inpt)
        print("|   |" * inpt)
        print(" --- " * inpt)
        counter+=1 


drawBoardInput()