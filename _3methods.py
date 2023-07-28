class Square(object):
    edge = 5
    area = 0

    def area1(self):
        self.area = self.edge * self.edge
        print("Area : ", self.area)

s1 = Square()
print(s1)
print(s1.edge)
print(s1.area)
print(s1.area1())
s1.edge = 10
print(s1.area1())