
# --------------------------------------------------
# Q1: Complete the Function
# Write a function to return the factorial of a number.
# Example: factorial(5) -> 120
# --------------------------------------------------

def factorial(n):
    if n < 0:
        print("error")
    else:
        f = 1
        for i in range(1, n+1):
            f *= i
        print(f)


factorial(4)