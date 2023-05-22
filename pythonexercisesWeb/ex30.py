#!usr/bin/python
import random
import sys

filename=sys.argv[1]

try:
    with open(filename, "r") as file:
        wordlist = file.read().split()
    print(wordlist[random.randint(0,len(wordlist))])
except:
    print ("didnt find your file.")
    


