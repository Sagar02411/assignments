
class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



def check_positive(n):
    if n > 0 :
        print("positive integer")
        
    else: 
        raise NegativeNumberError("Negative!")
    
check_positive(9)