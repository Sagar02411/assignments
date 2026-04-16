def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return 1 if n <= 1 else n * factorial(n-1)

print(factorial(5))  
print(factorial(-3))