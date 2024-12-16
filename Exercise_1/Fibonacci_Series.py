n = int(input("Enter a Number : "))
fibonacci = []
first = 0
second = 1
fibonacci.append(first)
fibonacci.append(second)
for i in range(2, n+1) :
    temp = first + second
    fibonacci.append(temp)
    first = second
    second = temp
print("The Fibonacci Series upto " + str(n) + " terms : ")
for i in fibonacci :
    print(i)
