class Student:
    school="AkiraChix"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f"Hello my name is {self.name} an i am {self.age} years old and i love {self.school}"

