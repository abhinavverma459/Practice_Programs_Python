rows=9
for i in range(1,rows):
    for j in range(-1+i,-1,-1):
        print(format(2**j,"4d"),end=" ")
    print(" ")
