#!usr/bin/python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in a:
    if x < 5:
        print (x)

newlist=[]
for x in a:
    if x < 5:
        newlist.append(x)
print(newlist)

newlist2= [x for x in a if (x < 5)]

print (newlist2)


input= input("give me a number to check ")

newlist3= [x for x in a if (x < int(input))]

print (newlist3)
        