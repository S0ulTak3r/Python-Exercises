#!usr/bin/python3
import datetime
name= input("please enter your name: ")
age= int(input("please enter your age: "))

tillYear= (100-age)

print ("Hello " + name + ", you will turn 100 years old in: "+str(tillYear)+ " years")

randomnumber= int(input ("hello, please input a random number: "))

for i in range(1,randomnumber):
    print("Hello " + name + ", you will turn 100 years old in: " + str(tillYear) + " years" + "\n")