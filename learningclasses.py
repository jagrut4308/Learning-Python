class student:#class helps create our own customised data type
    def __init__(self,name,major,cgpa):
    #def _init_(self) gives characteristics to our data type
    #it defines what a student is in this case
        self.name=name
        self.major=major
        self.cgpa=cgpa
    def on_honors(self):
        if self.cgpa>=9:
            return True
        else:
            return False