def expo(n,p):
    res=1
    for i in range(p):
        res=res*n
    return res;
num=int(input("Enter number:"))
pow=int(input("Enter power:"))
result=expo(num,pow)
print("Exponent result is:",result)
