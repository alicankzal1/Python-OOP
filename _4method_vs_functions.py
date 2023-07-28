# %% methods vs funtions

class Emp(object):
    
    age = 25 #
    salary = 1000 # $
    
    def ageSalaryRatio(self):
        a = self.age / self.salary
        print("method: ", a)
    
e1 = Emp()
e1.ageSalaryRatio()
#╦ ------------------------------------------------------        
# function
def ageSalaryRatio(age, salary):
    a = age / salary
    print("function: ",a)
    
ageSalaryRatio(30, 3000)

#
def findArea(a, b):  # a = pi,  b = r 
    area = a*b**2
    # print(area)
    return area
    
pi = 3.14
r = 5

result1 = findArea(pi, r)
print("result1 : ", result1)
result2 = findArea(pi, 10)

print("result1 + result2 : ", result1 + result2)