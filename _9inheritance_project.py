class Website:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def loginInfo(self):
        print(self.name + " " + self.surname)
class Website1(Website):
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)
class Website2(Website):
    def __init__(self, name, surname, email):
        Website.__init__(self,name, surname)
        self.email = email
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)
p1 = Website("ali can", "kızal")
p2 = Website1("ali can" , "kızal", "151320191103")
p3 = Website2("ali can", "kızal", "deneme@g.com")
print(p1.loginInfo())
print("----" * 10)
print(p2.login())
print("----" * 10)
print(p3.login())