#!usr/bin/python
import sys

listnames={}

try:
    filename=sys.argv[1]
    with open(filename,"r") as file:
        nameslist=file.read().split()

    for names in nameslist:
        if names in listnames:
            listnames[names]+=1
        else:
            listnames[names]=1


    print(listnames)
except:
    print ("no such file found unlucky")