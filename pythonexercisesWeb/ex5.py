#!usr/bin/python3
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

commonlist=[]
for x in a:
    if x in b and not x in commonlist:
        commonlist.append(x)

print (commonlist)

input1= input("enter maximum value for random number: ")
input2= input("enter the maximum length: ")
randomlist1 = [random.randint(1,int(input1)) for x in range(1,int(input2))]

print("random list 1:")
print (randomlist1)


randomlist2 = [random.randint(1,int(input1)) for x in range(1,int(input2))]
print ("random list 2: ")
print (randomlist2)

commonlist2=[]
for x in randomlist1:
    if x in randomlist2 and not x in commonlist2:
        commonlist2.append(x)

print (commonlist2)