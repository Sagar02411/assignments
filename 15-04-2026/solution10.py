# Q10 (Medium) – OOP (Classes & Objects)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        # Print "Name: X, Marks: Y"
        return f"Name is {self.name}, marks is {self.marks}"

r1 = Student("x","y")
print(r1.display())