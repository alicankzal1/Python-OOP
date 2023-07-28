class Animal:

    def toString(self):
        print("animal")
class Monkey(Animal):

    def toString(self):
        print("monkey")
a1 = Animal()
print(a1.toString())
m1 = Monkey()
print(m1.toString()) #monkey calls overriding method