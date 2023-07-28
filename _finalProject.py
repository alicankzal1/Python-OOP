"""
OOP: Object Oriented Programming
    - class/object
    - attributes/methods
    - encapsulation/ abstraction
    - inheritance
    - overriding/polymorphism
"""
from abc import ABC, abstractclassmethod
# inheritance
class Shape(ABC):
    """
        Shape = super class / abstract class
        
    """
    # abstract method
    @abstractclassmethod
    def area(self): pass
    @abstractclassmethod
    def perimeter(self): pass
    # overriding and polymorphism
    def toString(self):
        pass
#child
class Square(Shape):
    "sub class"
    def __init__(self, edge):
        self.__edge = edge # encapsulation private attribute
    def area(self):
        result = self.__edge ** 2
        return "square area : ", result
    def perimeter(self):
        result = self.__edge * 4
        return "square perimeter : ", result
    # override and polymorphism
    def toString(self):
        print("Square edge: ",self.__edge)
# child
class Circle(Shape):
    "circle class"
    PI = 3.14 # constant variable
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        result = self.PI * self.__radius ** 2 #pi * r ** 2
        return "circle area : ", result
    def perimeter(self):
        result = 2 * self.PI * self.__radius #2 * pi * r
        return "circle perimeter : ", result
    # override and polymorphism
    def toString(self):
        print("Circle radius : ", self.__radius)

circle = Circle(5)
print(circle.area())
print(circle.perimeter())
print(circle.toString())
print("-----" * 20)
square = Square(5)
print(square.area())
print(square.perimeter())
print(square.toString())

