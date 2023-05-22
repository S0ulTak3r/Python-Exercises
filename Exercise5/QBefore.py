#!/usr/bin/python3
import json
import os.path
import sys

def validateArg():
    if len(sys.argv) != 3:
        print("invalid amount of arguments presented")
        sys.exit()

def find_char(word:str):
    dic={}

    try:
        for x in word:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        return dic
    except:
        print("couldn't iterate over the word")
        sys.exit()

def toFile(name:json):
    if len(sys.argv) == 3:
        filename = str(sys.argv[2])
        if os.path.exists(filename) and os.path.splitext(filename)[1] == ".json":
            print(f"the file '{filename}' exists")
            with open(filename, "w") as file:
                file.write(json.dumps(name))
        else:
            print(f"the file '{filename}' does not exist or doesn't have a .json extension")
            sys.exit()
    else:
        print("invalid amount of arguments presented")
        sys.exit()

validateArg()
result = find_char(sys.argv[1])
print(result)
dic1 = json.dumps(result)
print(dic1)
toFile(dic1)
