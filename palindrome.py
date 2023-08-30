# wap in python to print palindrome or not
st=str(input("Enter the string :"))
j=-1
flag=0
for i in st:
    if i != st[j]:
        flag = 1
        break
    j=j-1
if flag == 1:
    print("no")
else:
    print("yes")
