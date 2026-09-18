s=open("README.md","r")
print(s)
print(s.readline())
for i in s.readlines():
    print(i)
s.close()
o=open("practice.txt","a")
o.write("\nPractice makes a man perfect")
o.close()
a=int(input("Enter a number:"))
if a==1:
    o=open("practice1.text","w")#creates new file practice1
    o.write("Overwrite")
    o.close()