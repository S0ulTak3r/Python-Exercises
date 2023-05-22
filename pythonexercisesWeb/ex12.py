#!usr/bin/python3

a = [5, 10, 15, 20, 25]

newlist=[]
newlist.append(a[0])
newlist.append(a[len(a)-1])

print (newlist)
def getnewlist(array:list):
    newlist=[array[0],array[len(array)-1]]
    return newlist

newlistv2=getnewlist(a)

print (newlistv2)