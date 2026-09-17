directors=["Kuroswa","Ray","Tarantino","Kashyap","Bergman","Joon-Ho"]
print(directors)
print(directors[2])
print(directors[-1])
#negative index starts indexing from back of the list
print(directors[1:])
#all elements from index 1
print(directors[1:3])
#elements from index 1 to index 3,not including 3
directors[1]="Satyajit Ray"
print(directors)
#LIST FUNCTIONS
ndirect=["Nolan","Scorsese"]
directors.extend(ndirect)
print(directors)
directors.append("Coen")
print(directors)
directors.insert(1,"King")
print(directors)
directors.remove("King")
#.remove() takes one argument
print(directors)
directors.pop()
print(directors)
print(directors.index("Bergman"))
#gives first instance index
directors.clear()
print(directors)
#clears entire list
numl=[11,12,3,4,22,4,16]
numl.sort()
print(numl)
#sorts number in ascending order
numl.reverse()
print(numl)
numl2=numl.copy()
print(numl2)
#2d lists
twod=[[1,0,0],[0,1,0],[0,0,1]]
print(twod)
print(twod[1][1])
