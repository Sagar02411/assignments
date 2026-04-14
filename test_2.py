def divide(a, b):
    if b == 0 :
        raise MyCustomError("Can not devide by zero")
    return a / b

print("Q2 Output:", divide(10, 0))