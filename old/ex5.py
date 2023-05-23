#!usr/bin/python3
import sys

def usage():
    print("this is the script usage: ")
    print ("usage: " + sys.argv[0] + " fileName" )

def createFile():
    filename = input("give me a new file name to create: ")
    f2 = open(filename, "w")
    while True:
        name = input("to end type -1, input a name: ")
        if len(name) == 0:
            print("you didn't provide a name")
            continue
        elif (name.startswith(" ") or name.endswith(" ")) or (" " in name):
            print("i do not accept spaces in the name.")
            continue
        elif name == "-1":
            print("created text file: " + filename)
            break
        else:
            f2.write(name + " ")
    f2.close()
    return filename


# function that reads all the content of the file at once and splits it into a dictionary, key:value
def checkFile(FileName):
    namelistCount = {}
    try:
        with open(FileName, "r") as file:
            nameslist = file.read().split()
    except FileNotFoundError:
        print("""
        ERROR: I cannot read or find the file you gave me

        Do you want to create a new text file from scratch and add names to it?
        y/n
        """)
        while True:
            answer = input()
            if answer != "y" and answer != "n":
                print("invalid answer")
                continue
            elif answer == "y":
                FileName = createFile()
                with open(FileName, "r") as file:
                    nameslist = file.read().split()
                break
            else:
                print("ok bye")
                sys.exit()

    for name in nameslist:
        if name in namelistCount:
            namelistCount[name] += 1
        else:
            namelistCount[name] = 1
    return namelistCount

if len(sys.argv) == 1:
    print("bruh, provide me a text file")
    usage()
    sys.exit()
elif len(sys.argv) > 2:
    print("bruh you gave me too much arguments, give me 1 text file.")
    usage()
    sys.exit()
else:
    namelistCounter = checkFile(sys.argv[1])
    print("thanks for providing a text file, I don't really care if it's empty")

print(namelistCounter)
