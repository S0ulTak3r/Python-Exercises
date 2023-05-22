
#!/usr/bin/python
import sys


try:
    filename1=sys.argv[1]
    filename2=sys.argv[2]
    with open(filename1,"r") as file:
        list1=file.read().split()
    with open(filename2,"r") as file:
        list2=file.read().split()

    common=[value for value in list1 if value in list2]

    print(common)

except:
    print ("no such file found unlucky")