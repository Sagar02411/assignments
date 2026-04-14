class Dog:
    def speaks(self):
        return "Dog Barks"

class Cat:
    def speaks(self):
        return "Cat does not barks"


# cat1 = Cat()
# dog1 = Dog()

print(Cat().speaks())
print(Dog().speaks())