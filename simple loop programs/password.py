password="Jagrut"
nguess=0
guess=""
while(guess!=password and nguess!=3):
    guess=input("Enter password:")
    nguess+=1
if(guess==password):
    print("Correct password")
