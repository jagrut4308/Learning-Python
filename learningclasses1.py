from learningclasses import student
from question import question
#imports student class from learning classes file
student1=student("Jagrut","CSE",9.3)
mcq=["The color of a banana is:\na.Yellow\nb.Blue\nc.Red\n\n",
"The color of apple is:\na.Red/Green\nb.Blue\nc.White\n\n",
"The color of watermelon is:\na.White\nb.Green/Black\nc.Orange\n\n"]
mcqans=[question(mcq[0],"a"),#Create a question object and give it mcq[0] as its prompt and "a" as its answer.
question(mcq[1],"a"),
question(mcq[2],"b")]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)#mcq[0] stored in question.prompt
        if answer==question.answer:
            score+=1
    print("Your score is:",score)
run_test(mcqans)
class studdata(student):#studdata inherits data from student
    #now you can use functions from student
    print(student1.on_honors())
