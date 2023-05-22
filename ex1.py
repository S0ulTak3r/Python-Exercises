#!/usr/bin/python3

x = "Daniel"

print (x.upper())

def reverseString(name:str) -> str:
    return name[::-1]

print (reverseString(x))

print (len(x))

middleIndex = int(len(x)/2)

if ( (len(x)%2) == 0 ):
    print (x[:middleIndex-1] + "*" + x[middleIndex:])
else:
    print (x[:middleIndex] + "*" + x[middleIndex+1:])
