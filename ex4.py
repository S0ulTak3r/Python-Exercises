#!/usr/bin/python3


import sys
import random

#function that checks if all elements of the list are numeric, and makes sure they are int
def CheckIfAllNum(array:list) -> bool:
    for i in range(len(array)):
        if str(array[i]).isnumeric() == False:
            return False
        else:
            array[i] = int(array[i])
    return True


#Function to create a manual list, user interactive.
def CreateAList () -> list:
    newlist=[]
    print("You are going to add numbers 1 by 1,to finish creation- type -1")
    while True:
        answer = input("please provide a number: ")
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

#Function that promps a user to create a list RANDOMLY/MANUALLY/QUIT the script.
def CheckIfCreate():
    print("""
        do you wish to create a random or manual list or quit?
        r/m/q
        """)
    while True:
        answer = input()
        if (answer != "r") and (answer != "m") and (answer != "q"):
            print ("you entered an invalid answer")
            continue
        elif (answer == "r"):
            answer= input("what length should the list be? ")
            if not answer.isnumeric():
                print ("the value you provided is non numeric, starting over")
                continue
            answer2 = input("what should the maximum value be? ")
            if not answer2.isnumeric():
                print ("the value you provided is non numeric, starting over")
                continue
            newlist=[]
            for i in range(1,int(answer)):
                number=random.randint(1,int(answer2))
                newlist.append(number)
            print("successfully created a list: ")
            print(newlist)
            return newlist
        elif (answer == "m"):
            newlist=CreateAList()
            print("successfully created a list: ")
            print(newlist)
            return newlist
        else:
            print ("ok bye")
            sys.exit()

#Function that deletes duplicates from a list, and returns a new un-duplicated value list.
def deleteDuplicates(array:list) -> list:
    array=set(array)
    array=list(array)
    return array

#boolean value used in the error checking, so i dont do sys.exit() but give the user another chance
passNext = False

#checks user arguments, and goes over every option of input possible. 1 valid,2 invalid,2 valid, non given.
if len(sys.argv) > 3:
    print ("you provided too much arguments, please provide two lists")
    sys.exit()
elif len(sys.argv) == 3:
    if (CheckIfAllNum(sys.argv[1])) or (CheckIfAllNum(sys.argv[2])) == False:
        print ("""
        one of the lists you provided is invalid,
        it continans non-numeric values.
        
        you will be prompted to create 2 new lists,
        or given the option to exit the script and correct your arguments.
        """)
        passNext = True
    else:
        print ("thank you for providing 2 valid lists")
        newlist=sys.argv[1]
    if (passNext == True):
        pass
elif len(sys.argv) == 2:
    if (CheckIfAllNum(sys.argv[1])) == False:
        print ("you provided only 1 list, and this list is invalid")
        pass
    else:
        print("you provided only 1 list that is valid")
        newlist=CheckIfCreate()
        newlist2=sys.argv[1]
else:
    print ("""
    you didnt give any valid list or one of the lists was invalid.
    creating 2 new lists.
    """)
    print ("list 1")
    newlist=CheckIfCreate()
    print ("list 2")
    newlist2=CheckIfCreate()

#prints the final lists the script will be working on
print ("list 1 that we will be working on is: ")
print (newlist)
print ("list 2 that we will be working on is: ")
print (newlist2)

#Outputs a new list that is made of common values present both in list1, and list2
AllCombinations = set(newlist+newlist2)
commonList=[]
for combination in AllCombinations:
    if newlist.count(combination)>=1 and newlist2.count(combination)>=1:
        commonList.append(combination)
print ("all the values that are present both in list 1 and 2 are: ")
print (commonList)

#Outputs, the list 1 and 2, after the duplicate values were removed.
print ("we are going to delete duplicates, but not change the list itself, just print it out")
print (deleteDuplicates(newlist))
print (deleteDuplicates(newlist2))