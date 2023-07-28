# SOYUT SINIFLAR
#PEK MANTIĞINI OTURTAMADIM TEKRAR ÇALIŞ

from abc import ABC, abstractclassmethod

class Animal(ABC): #super class
    @abstractclassmethod
    def walk(self): pass

    @abstractclassmethod
    def run(self): pass
#TypeError: Can't instantiate abstract class Animal with abstract methods run, walk 
# böyle bir type error alıyorsak animal classını soyutlamış(abstract) oluruz.
class Bird(Animal): #subclass
    def __init__(self):
        print("bird")

## eğer super classımızda abstract class yapıyorsak subclassta super classtaki methodlar yazmamız lazım

    def walk(self):
        print("walk")
    def run(self):
        print("run")
bird = Bird()
print(bird)
print(bird.walk())
print(bird.run())