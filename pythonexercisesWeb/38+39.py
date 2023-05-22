#!usr/bin/python3
import datetime
name= input("please enter your name: ")
age= int(input("please enter your age: "))

tillYear=  datetime.datetime.now().year + (100-age)

print (f"Hello {name}, you will turn 100 years old in: {str(tillYear)}")

randomnumber= int(input ("hello, please input a random number: \n"))

for i in range(1,randomnumber):
    print(f"Hello {name}, you will turn 100 years old in: {str(tillYear-datetime.datetime.now().year)} years" + "\n")