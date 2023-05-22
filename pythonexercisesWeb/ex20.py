#!usr/bin/python
import sys

#lst=sorted(eval(sys.argv[1]))
def binarysearch(array:list,num:int):
    low=0
    high=len(array)-1
    while low<=high:
        middle = int(((high+low)/2))
        if (array[middle] == num):
            return "im in the array mf'er"
            break
        elif (array[middle] < num):
            low=middle+1
        else:
            high=middle-1
    return "im not in the array"


lst=sorted(sys.argv[1:])

inpt=input("enter a number: ")

if inpt in lst:
    print("gaddayum im in the list")
else:
    print("im not in the list")

print(binarysearch(lst,inpt))


