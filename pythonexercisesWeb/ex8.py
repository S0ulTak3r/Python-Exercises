#!usr/bin/python
import getpass
import sys


def rpsGame():

    P1Turn = True
    P2Turn = False
    winnername=""
    winner=False
    roundNumber=1
    startOver=False
    while True:

        while P1Turn== True:

            print("""
            
            
                Player 1 Turn
                
                
                """)
            P1answer = getpass.getpass("R/P/S")

            if (not P1answer in ["R","r","S","s","P","p"]):
                print("invalid option given")
                continue
            else:
                P1Turn=False
                P2Turn=True

        while P2Turn == True:

            print("""
            
            
                Player 2 Turn
                
                
                """)
            P2answer = getpass.getpass("R/P/S \n")

            if (not P2answer in ["R","r","S","s","P","p"]):
                print("invalid option given \n")
                continue
            else:
                P2Turn = False
                P1Turn = True

        if P1Turn==True and P2Turn==False:
            roundNumber+=1
            if (P1answer in ["P","p"] and P2answer in ["P","p"]) or (P1answer in ["S","s"] and P2answer in ["S","s"]) or (P1answer in ["R","r"] and P2answer in ["R","r"]):
                print("ITS A DRAW, nobody won yet. \n")
            elif (P1answer in ["R","r"] and P2answer in ["S","s"]):
                print ("PLAYER 1 HAS WON THE GAME, ON ROUND: " + str(roundNumber))
                winnername="Player 1 is the winnerrr"
                winner = True
                break
            elif (P1answer in ["P","p"] and P2answer in ["R","r"]):
                print("PLAYER 1 HAS WON THE GAME, ON ROUND: " + str(roundNumber))
                winnername = "Player 1 is the winnerrr"
                winner = True
                break
            elif (P1answer in ["S","s"] and P2answer in ["P","p"]):
                print("PLAYER 1 HAS WON THE GAME, ON ROUND: " + str(roundNumber))
                winnername = "Player 1 is the winnerrr"
                winner=True
                break
            elif (P2answer in ["R","r"] and P1answer in ["S","s"]):
                print ("PLAYER 2 HAS WON THE GAME, ON ROUND: " + str(roundNumber))
                winnername="Player 2 is the winnerrr"
                winner = True
                break
            elif (P2answer in ["P","p"] and P1answer in ["R","r"]):
                print("PLAYER 2 HAS WON THE GAME, ON ROUND: " + str(roundNumber))
                winnername = "Player 2 is the winnerrr"
                winner = True
                break
            elif (P2answer in ["S","s"] and P1answer in ["P","p"]):
                print("PLAYER 2 HAS WON THE GAME, ON ROUND: " + str(roundNumber))
                winnername = "Player 2 is the winnerrr"
                winner=True
                break

        if(winner==True):
            break

    print("Game Over, To start over press 1 to exit -1")
    while True:
        answer = input("Input: ")
        if answer == "-1":
            print("exiting")
            sys.exit()
        elif answer == "1":
            print("starting new game instance")
            startOver = True
            break
        else:
            print("invalid argument")
            continue
    if (startOver==True):
        rpsGame()


            



print("""
WELCOME
TO
THE

ROCK PAPER SCISSORS GAME!!!

PRESS S to start / Q to quit.
""")

while True:
    answer=input("S/Q: ")

    if not answer in ["S","s","Q","q"]:
        print ("you gave an invalid option")
        continue
    elif answer in ["S","s"]:
        rpsGame()
    else:
        sys.exit()

