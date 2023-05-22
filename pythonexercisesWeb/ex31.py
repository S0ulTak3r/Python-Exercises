#!usr/bin/python
import random
import sys

filename = sys.argv[1]


def generateWord(filename):
    try:
        with open(filename, "r") as file:
            wordlist = file.read().split()
        word = wordlist[random.randint(0, len(wordlist))]
    except:
        print("didnt find your file.")
        sys.exit()

    return word


def hideWord(word: str):
    hiddenWord = " _ " * len(word)
    return hiddenWord


def showHiddenWord(hiddenWord: str):
    print(hiddenWord)


def guess():
    inpt = input("guess a letter: ")
    return inpt


def checkifwordPresent(hiddenWord: str, word: str, guess: str, lives):
    if guess.upper() in word.upper():
        hiddenlst = hiddenWord.split()
        for i in range(len(hiddenlst)):
            if word[i].upper() == guess.upper():
                hiddenlst[i] = guess.upper()
        hiddenWord = ' '.join(hiddenlst)
        checkWin(hiddenWord)
    else:
        print("unlucky you guessed it wrong")
        lives = removeLife(lives)
        checkOver(lives)

    return hiddenWord, lives

def removeLife(lives):
    lives -= 1
    return lives


def checkOver(lives):
    if lives == 0:
        print("game over")
        sys.exit()
    else:
        print("lives left: " + str(lives))
        return lives

def checkWin(hiddenword:str):
    if hiddenword.count("_")==0:
        print("you have won, easy Bro")
        print("Game Over")
        sys.exit()

def rungame():
    print("""

    Welcome to guess the word

    """)

    lives = 10
    word = generateWord(filename)
    print(word)
    hideword = hideWord(word)
    print("hidden word: ")
    showHiddenWord(hideword)

    while True:
        guessing = guess()
        hideword, lives = checkifwordPresent(hideword, word, guessing, lives)
        showHiddenWord(hideword)


rungame()




