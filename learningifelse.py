ismale=True
istall=False
if ismale and istall: #and can also be used
    print("Higher avg height")
elif ismale and not istall:
    print("Should be taller")
else:
    print("Lower avg height")
def largest(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print("The largest number is",num1)
    elif num2>=num1 and num2>=num3:
        print("The largest number is",num2)
    else:
        print("The largest number is",num3)
a=int(input("Enter num:"))
b=int(input("Enter num:"))
c=int(input("Enter num:"))
largest(a,b,c)