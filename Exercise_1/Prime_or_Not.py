number = int(input("Enter a number : "))
isPrime = True
for i in range(2, number):
    if (number%i) ==0:
        isPrime = False
        break
if isPrime :
    print("The number " + str(number) + " is Prime")
else:
    print("The number " + str(number) + " is not Prime")



