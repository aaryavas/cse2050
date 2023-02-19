class Animal(object):

    def __init__(self,name):
        self.name = name
    
    def reply(self):
      return self.speak()  

class Mammal(Animal):
    def speak(self):
        return f'{self.name} says ahhhh!'


class Cat(Mammal):
    def speak(self):
        return f'{self.name} says Meow!'


class Dog(Mammal):
    def speak(self):
        return f'{self.name} says Woof!'



class Primate(Mammal):
    def speak(self):
        return f'{self.name} says sound!'


class ComputerScientist(Primate):
    pass

