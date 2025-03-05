class Animal:
    def sound(self):
        return "Animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meww"

animals=[Dog(),Cat(),Animal()]
for animal in animals:
    print(animal.sound())

