#!usr/bin/python3

number = input ("please provide me with a number: ")



list=[]
for x in range(1,int(number)+1):
    if (int(number)%x==0):
        list.append(x)

print (list)