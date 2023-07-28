#parent class
class Animal:
    def __init__(self):
        print("animal is created")
    def toString(self):
        print("animal")
    def walk(self):
        print("animal walks")
#child class 1
class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init of parent(animal) class
        print("monkey is created")
    def toString(self):
        print("monkey")
    def climb(self):
        print("monkey can climb")
#child class 2
class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    def fly(self):
        print("Bird can fly")

#monkey = Monkey()

monkey = Monkey()
monkey.toString()
monkey.walk()
monkey.climb()
print("----")
bird = Bird()
bird.walk()
# b1.climb()
bird.fly()  
