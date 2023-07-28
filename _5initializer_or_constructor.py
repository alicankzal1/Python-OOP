class Animal(object):
    def __init__(self, name, age):
        #attribute
        self.name = name
        self.age = age
    def GetName(self):
        return self.name 
    def GetAge(self):
        return self.age
    
animal1 = Animal("cat", 2)
print(f"animal1 name : {animal1.GetName()}")
print(f"animal1 age : {animal1.GetAge()}")
animal2 = Animal("dog", 5)
print(f"animal2 name : {animal2.GetName()}")
print(f"animal2 age : {animal2.GetAge()}")
animal3 = Animal("bird", 12)
print(f"animal3 name : {animal3.GetName()}")
print(f"animal3 age : {animal3.GetAge()}")