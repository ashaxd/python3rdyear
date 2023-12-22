def hcf(a,b):
    if a>b:
        small=b
    else:
        small=a
    for i in range(1,small+1):
        if((a%1==0)and(b%1==0)):
            hcf=i
        return hcf            
a=int(input("enter a number:"))
b=int(input("enter a another number:"))
c=hcf(a,b)
print(c)