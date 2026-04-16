# --------------------------------------------------
# Q2: Debug the Code
# The function should return the sum of all even numbers in a list.
# Fix the bug.
# --------------------------------------------------

def sum_even(numbers : list):
    total = 0
    for num in numbers:
        if num % 2 == 0: 
            total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(sum_even(numbers))