# Q11 (Medium) – Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "dog barks"
r1 = Dog()
animal = Animal()
print(r1.speak())
print(animal.speak())
