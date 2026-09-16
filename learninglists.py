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