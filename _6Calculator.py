class Calculator(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b 

        pass
    def add(self):
        result = self.value1 + self.value2
        return result
    def substraction(self):
        result = self.value1 - self.value2
        return result
        
    def multiply(self):
        result = self.value1 * self.value2
        return result
    def division(self):
        result = self.value1 / self.value2
        return result
    

selection = input("Choose selection:\nadd : 1\nsubstract : 2\nmultiply : 3\ndivision : 4\n")
val1 = int(input("first value ? : "))
val2 = int(input("second value ? : "))

c1 = Calculator(val1, val2)
if selection == "1":
    add_result = c1.add()
    print(f"add result : {add_result}")
elif selection == "2":
    substract_result = c1.substraction()
    print(f"substract result : {substract_result}")
elif selection == "3":
    multiply_result = c1.multiply()
    print(f"multiply result : {multiply_result}")
elif selection == "4":
    divide_result = c1.division()
    print(f"division result : {divide_result}")
else:
    print("Error! There is no proper selection.")