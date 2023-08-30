def fibonacci(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        return (fibonacci(number - 2) + fibonacci(number - 1))
number=int(input("Enter the range number :"))
for n in range(0,number):
                print(fibonacci(n),end=" ")
