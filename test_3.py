class InvalidAgeException(Exception):
    def __init__(self,message):
       self.message = message
       super().__init__(self.message)
def check_age(age):
     if age < 18:
        raise InvalidAgeException("Age must be greater than 18")
     else:
        return "Eligible"

print("Q3 Output: ", check_age(13))