n = int(input("Enter the number to which you have to find Factorial : "))
fact = 1
for i in range (1, n+1):
    fact *= i
print("Factorial of a number " + str(n) + " is " + str(fact))