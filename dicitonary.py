d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
d3=dict(d1)
d3.update(d2)
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
print(d3)
