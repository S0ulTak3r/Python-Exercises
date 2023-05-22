#!/usr/bin/python


import os
import re
import sys
import csv
import hashlib
from multiprocessing import Pool

def validateArg():
    if len(sys.argv) != 2:
        print("invalid amount of arguments")
        sys.exit()


def pathListcalc(directory:str):
    if os.path.exists(directory):
        with Pool() as pool:
            results = pool.map(getPaths, [directory])
        return results[0]
    else:
        print(f"doesnt work, could not find {directory}")


def getPaths(directory):
    PathList=[]
    for root,dirs,files in os.walk(directory):
        for file in files:
            PathList.append(os.path.join(root, file))
    return PathList

def calcmd5(path):
    with open(str(path),"rb") as file:
        data=file.read()
        return hashlib.md5(data).hexdigest()

def runRecoursiveOnDirectory(directory:str):
    counter=0
    with open("test.csv","w") as csvWriter:
        writer=csv.writer(csvWriter)
        writer.writerow(['number','file-path','md5-code'])
        filePaths=pathListcalc(directory)
        with Pool() as pool2:
            md5list= list(pool2.map(calcmd5,filePaths))
        for file_path, md5_hash in zip(filePaths, md5list):
                counter += 1
                writer.writerow([counter, file_path, md5_hash])
        





validateArg()
runRecoursiveOnDirectory(sys.argv[1])
