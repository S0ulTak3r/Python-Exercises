number = int(input("Please enter the number of Fibonacci numbers to generate: "))

fib_list = []

for i in range(number):
    if i < 2:
        fib_list.append(i)
    else:
        fib_list.append(fib_list[i-1] + fib_list[i-2])

print(fib_list)
