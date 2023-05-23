#!/usr/bin/python3
import sys

#function that checks if all elements of the list are numeric, and makes sure they are int
def CheckIfAllNum(array:list) -> bool:
    for i in range(len(array)):
        if str(array[i]).isnumeric() == False:
            return False
        else:
            array[i] = int(array[i])
    return True

#function that creates a new list, manually using user input, interactive
def CreateAList () -> list:
    newlist=[]
    print("You are going to add numbers 1 by 1,to finish creation- type -1")
    while True:
        answer = input("please provide a number")
        if (answer == "-1") and (len(newlist)==0):
            print ("the list is empty, i dont create an empty list")
        elif (answer == "-1"):
            print ("created a list")
            break
        else:
            if not answer.isnumeric():
                print ("you didnt provide a valid input")
                continue
            else:
                newlist.append(int(answer))
    return newlist


#checks user arguments, creates a list if no arguments were given.
if len(sys.argv) > 2:
    print ("you provided too much arguments, please provide a single list")
    sys.exit()
elif len(sys.argv) == 2:
    if (CheckIfAllNum(sys.argv[1])) == False:
        print ("the list you provided is invalid, it continans non-numeric values")
        sys.exit()
    else:
        print ("thank you for providing a valid list")
        newlist=sys.argv[1]
else:

    print ("""
    you did not provide a list,
    do you wish to create one?
    y/n
    """)

    while True:
        answer = input()
        if (answer != "y") and (answer != "n"):
            print ("you entered an invalid answer")
            continue
        elif (answer == "y"):
            print ("ok, lets create a list")
            newlist=CreateAList()
            print("successfully created a list, the list values are: ")
            print(newlist)
            break
        else:
            print ("ok bye")
            sys.exit()


#prints all values in the list, below 5.
for num in newlist:
    if (num < 5):
        print(num)
    else:
        break


#block of code, that includes a function which creates a new list containing all numbers that are
#lower than 5, that are present in the array that we provide to the function
def newlistLowerthan5In(array:list) -> list:
    newlist = []
    for num in array:
        if (num < 5):
            newlist.append(num)
    return newlist

print (newlistLowerthan5In(newlist))



#block of code, that includes a function which does all of the above in 1 line.
def newlistLowerthan5InV2(array:list) -> list:
    newlist = [value for value in array if (value < 5)]
    return newlist

print (newlistLowerthan5InV2(newlist))




#block of code, that includes a function with user input, to check for all values below the input given.
def checkNumlowerIn(array:list) -> list:
    while True:
        answer = input("please enter a number to check for: num < input")
        if answer.isnumeric() == False:
            print ("you provided a invalid input, provide a number")
            continue
        break
    newlist = [value for value in array if ( value < int(answer) )]
    return newlist

print (checkNumlowerIn(newlist))



