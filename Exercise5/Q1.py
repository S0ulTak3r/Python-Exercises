#!/usr/bin/python
import sys
import os
import re


def validateNumArg():
    if len(sys.argv) != 3:
        print("Invalid number of arguments. Usage: python script.py <file_path> <search_word>")
        sys.exit(1)


def validateFile(file_path):
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' doesn't exist.")
        sys.exit(1)
    if not os.path.isfile(file_path):
        print(f"'{file_path}' is not a file.")
        sys.exit(1)


def searchInFile(search_word, file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                if re.search(search_word, line):
                    print(line.strip())
    except:
        raise ValueError("Error occured while reading the file")

validateNumArg()
file_path = sys.argv[1]
search_word = sys.argv[2]
validateFile(file_path)
searchInFile(search_word, file_path)

