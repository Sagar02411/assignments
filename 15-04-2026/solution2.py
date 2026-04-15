def safe_divide(a, b):
    result = a/b
    if b == 0:
        raise ZeroDivisionError("Can not devide by zero")
    return a/b
print(safe_divide(2,0))