n=int(input("Enter number of products :"))
prod={}
for i in range(n):
    p=input("Enter product name :")
    prod[p]=int(input("Enter its price:"))
q=True
while q:
    p=input("Enter product for price or q to exit :")
    if p=='q':
        break
    if p in prod:
        print('price of',p,'is',prod[p])
    else:
        print(p,'is not here')
