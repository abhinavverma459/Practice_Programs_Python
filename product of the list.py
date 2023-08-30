Nums = str(input("Enter Numbers separated by SPACE: ")).split(" ")
print(Nums)
Prod = 1
s = ""
for r in range(0,len(Nums)):
    Prod = Prod * int(Nums[r])
    s = s + Nums[r] + " x "
print("Product of list (",s,") = ",Prod)



