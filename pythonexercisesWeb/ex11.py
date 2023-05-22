number = int(input("Please provide me with a number: "))

# No point starting from 1, as every number divides by 1.
# The loop checks if the inputted number divides by any number lower than itself.
# if the for loop completes without encountering a break statement, it will print out
# Number is prime
for x in range(2, number):
    if number % x == 0 and x != 5:
        print("This number is not prime")
        print(x)
        break
else:
    print("This number is prime")
