# Q11 (Medium) – Inheritance


class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    # Override speak method to return "Dog barks"
    def speak(self):
        print("Dog barks")
d1 = Dog()
d1.speak()

