num1 , num2, num3 = tuple(input("input 3 numbers with spaces: ").split())

if num1>num2 and num1>num3:
    print(num1," is bigger")
elif num2>num1 and num2>num3:
    print(num2," is bigger")
elif num3>num1 and num3>num2:
    print(num3," is bigger")
else:
    print("all numbers are equal")