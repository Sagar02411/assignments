def check_age(age):
    if age < 18:
        raise MyCustomError("Age must be greater than 18",400)
    return "Eligible"

print("Q3 Output:", check_age(15))