# Q10 (Medium) – OOP (Classes & Objects)

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"{self.name} has {self.marks}"
    
s1 = Student("A", 28)
print(s1.display())
