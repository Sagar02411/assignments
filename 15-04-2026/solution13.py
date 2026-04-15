# Q13 (Medium) – Polymorphism
class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

def animal_sound(animal):
    print(animal.sound())

animal_sound(Cat())
animal_sound(Cow())
    
    