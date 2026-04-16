"""
Python Assignment - Medium Level
Instructions:
- Solve all 10 questions.
- Do not change function names.
- Write clean and readable code.
"""

# --------------------------------------------------
# Q1: Complete the Function
# Write a function to return the factorial of a number.
# Example: factorial(5) -> 120
# --------------------------------------------------

def factorial(n):
    # TODO: Complete the code
    pass


# --------------------------------------------------
# Q2: Debug the Code
# The function should return the sum of all even numbers in a list.
# Fix the bug.
# --------------------------------------------------

def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1:   # Bug here
            total += num
    return total


# --------------------------------------------------
# Q3: Complete the Function
# Return a list of unique elements from the given list.
# Example: [1,2,2,3] -> [1,2,3]
# --------------------------------------------------

def unique_elements(lst):
    # TODO: Complete the code
    pass


# --------------------------------------------------
# Q4: Debug the Code
# The function should reverse a string.
# --------------------------------------------------

def reverse_string(s):
    rev = ""
    for i in range(len(s)):
        rev += s[i]   # Bug here
    return rev


# --------------------------------------------------
# Q5: Implementation
# Write a function to check if a number is prime.
# --------------------------------------------------

def is_prime(n):
    # TODO: Complete the code
    pass


# --------------------------------------------------
# Q6: Debug the Code
# The function should find the maximum number in a list.
# --------------------------------------------------

def find_max(lst):
    max_val = 0   # Bug here
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


# --------------------------------------------------
# Q7: Complete the Function
# Return a dictionary with character frequency.
# Example: "aab" -> {'a':2, 'b':1}
# --------------------------------------------------

def char_frequency(s):
    # TODO: Complete the code
    pass


# --------------------------------------------------
# Q8: Implementation
# Write a function to merge two sorted lists.
# Example: [1,3,5], [2,4] -> [1,2,3,4,5]
# --------------------------------------------------

def merge_sorted(list1, list2):
    # TODO: Complete the code
    pass


# --------------------------------------------------
# Q9: Debug the Code
# The function should count words in a sentence.
# --------------------------------------------------

def count_words(sentence):
    words = sentence.split(" ")
    return len(words) - 1   # Bug here


# --------------------------------------------------
# Q10: Implementation
# Write a function to check if two strings are anagrams.
# Example: "listen", "silent" -> True
# --------------------------------------------------

def are_anagrams(s1, s2):
    # TODO: Complete the code
    pass

