class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative number error")
    else:
        return "valid"
    # Raise NegativeNumberError if n < 0
    # Otherwise return "Valid"
print(check_positive(2))