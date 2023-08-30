n=10
end_range=int(input("Enter the end range :"))
sum=0
for i in range(1,end_range):
    z=((i*n)+3)
    print(z,end="  ")
    sum=sum+z
print("\nSum of the series is :",sum)
