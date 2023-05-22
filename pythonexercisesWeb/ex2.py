#!usr/bin/python3

number = int(input("please give me a number: "))

if(number%4==0):
    print("this number is an multiple of 4")
elif(number%2==0):
    print("this number is even")
else:
    print ("this number is odd")


number1= int(input("give me number 1: "))
number2= int(input("give me number 2: "))


if number1%number2==0:
    print ("this number: "+str(number1)+ " is a multiple of: " + str(number2))
else:
    print("unlucky")