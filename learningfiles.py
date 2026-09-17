s=open("README.md","r")
print(s)
print(s.readline())
for i in s.readlines():
    print(i)
s.close()