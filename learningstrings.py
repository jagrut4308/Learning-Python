print("Things are \"weird\"")
#\"" allows us to print double quotes
phrase="Jagrut"
print(phrase.isupper())
phrase1="JAGRUT"
print(phrase1.isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index('g'))
print(phrase.replace("Jagrut","Devadiga"))
#original string not changed
print(phrase)
#to change original string
phrase=phrase.replace("Ja","Ra")
print(phrase)