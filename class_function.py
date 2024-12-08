#creating class
class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 
    def display(self):
        print(f"Name is {self.name}, age is {self.age} and gender is {self.gender}")

#object creation

p1= person(name="Ram", age=25, gender= "male")
p2= person(name="sita", age=14, gender= "female")

p1.display()
p2.display()
