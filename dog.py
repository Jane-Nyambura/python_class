class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hoot(self):
        return f"my dog's name is {self.name} and it is now {self.age}"