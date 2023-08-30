num=int(input("Enter the number ="))
x=0
if num >1:
    for i in range(2,num):
        if (num % i ) == 0:
            x=1
            break
if num:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")
