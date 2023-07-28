class BankAccount:
    def __init__(self, name, money, address):
        self.name = name
        self.money = money
        self.address = address
    # get and set global
    def getMoney(self):
        return self.money
    def setMoney(self, amount):
        self.money = amount
    # private
    def __increase(self, increase):
        self.money = self.money + increase
        return self.money

    

p1 = BankAccount("ali can", 2000, "adana")
p2 = BankAccount("deneme", 312341, "esk")


print(p1.name)

print(p1.increase(500))
print("get method:",p1.getMoney())
#print("get method:",p1.__money)
p1.setMoney(5000)
print("after set method:",p1.getMoney())

#p1.__increase(500)
#print("after raise: ",p1.getMoney())
