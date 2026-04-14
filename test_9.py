class Students:
    #def __init__(self, name, marks):
        #self.name = name
        #self.marks = marks

    def display(self,name,marks):
        return name,marks

#display = Students("devansh",21)
#print(display.name)
#print(display.marks)
print(Students().display("devansh",21))