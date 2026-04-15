# Q2 (Easy) – Exception Handling
def safe_divide(a, b):
    try: 
        return  a/b
    # If division by zero occurs, return "Cannot divide by zero"
    except ZeroDivisionError:
        print("Cannot divide by zero")


safe_divide(2,0)