#!/usr/bin/python3
import sys

def reverseString(string:str) -> str:
    return string[::-1]

def checkPolindrom(string:str) -> str:
    if (string != reverseString(string)):
        return "this string is not a polindrom"
    else:
        return "this string is a polindrom"

if len(sys.argv) == 1:
    stringInput = str(input("please enter as string as you didnt provide one: "))
else:
    stringInput = str(sys.argv[1])

print("The inputted string is: " , stringInput)

print("Right now we are going to print the reversed string")

print("Here is the reversed string :" +reverseString(stringInput))

print("we are going to check if the string is a polindrom")

print(stringInput +" "+ reverseString(stringInput)+" :"+checkPolindrom(stringInput))





