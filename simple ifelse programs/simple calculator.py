num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
op=input("Enter operator:")
if op=='+':
  print(num1+num2)
elif op=='-':
  print(num1-num2)
elif op=='*':
  print(num1*num2)
elif op=='/':
  if num2!=0:
    print(num1/num2)
  else:
    print("Zero Division Error")
else:
  print("Wrong input")
