
class  Car:
      def __init__(self,name,color,speed,model):
        self.name=name
        self.color=color
        self.speed=speed
        self.model=model
      def move(self):
        return f"This car is a  {self.name} and it is {self.color} in color and it a very high{self.speed} and it is{self.model}"
      def stop(self):
        return f"This car is a  {self.name} and it is {self.color} in color and it a very high{self.speed}  and it is{self.model}"