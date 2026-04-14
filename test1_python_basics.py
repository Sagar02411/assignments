"""
PYTHON ASSIGNMENT

Instructions:
- Each question is written as a comment or TODO.
- Fix errors, complete missing parts, or implement logic as instructed.
- Do NOT remove the questions.
- You may test each section independently.

Topics Covered:
Functions, Exception Handling, Standard Libraries, Lambda/map/filter/reduce,
Modules & Packages, OOP, SQL Basics, DB Connection, Best Practices, Logging.
"""

# =========================
# Q1: FUNCTIONS (Basic)
# =========================

# TODO:
# Create a function `add_numbers(a, b)` that returns the sum of two numbers.
# Then call the function and print the result.

def add_numbers(a, b):
    pass

print("Q1 Output:", add_numbers(5, 3))


# =========================
# Q2: EXCEPTION HANDLING
# =========================

# TODO:
# Fix the code so that it handles division by zero properly using try-except.

def divide(a, b):
    return a / b

print("Q2 Output:", divide(10, 0))


# =========================
# Q3: CUSTOM EXCEPTION
# =========================

# TODO:
# Create a custom exception called InvalidAgeError.
# Raise it if age < 18.

def check_age(age):
    if age < 18:
        # raise custom exception
        pass
    return "Eligible"

print("Q3 Output:", check_age(15))


# =========================
# Q4: STANDARD LIBRARIES
# =========================

# TODO:
# Use the random module to generate a random number between 1 and 100.

import random

def generate_random():
    # return random number
    pass

print("Q4 Output:", generate_random())


# =========================
# Q5: LAMBDA, MAP, FILTER
# =========================

# TODO:
# Use lambda + map to square all numbers in the list.

numbers = [1, 2, 3, 4, 5]

squared = None  # Replace with map + lambda

print("Q5 Output:", list(squared))


# =========================
# Q6: FILTER
# =========================

# TODO:
# Use filter to get only even numbers.

evens = None

print("Q6 Output:", list(evens))


# =========================
# Q7: REDUCE
# =========================

# TODO:
# Use reduce to calculate the product of the list.

from functools import reduce

product = None

print("Q7 Output:", product)


# =========================
# Q8: MODULE IMPORT ISSUE
# =========================

# TODO:
# Fix the issue: This code assumes a module named `math_utils`
# with a function `multiply(a, b)`.
# Write a comment explaining how to structure the package properly.

# from math_utils import multiply
# print(multiply(2, 3))


# =========================
# Q9: OOP - CLASS & OBJECT
# =========================

# TODO:
# Create a class `Student` with attributes name and marks.
# Add a method `display()` to print details.

class Student:
    pass

s1 = Student()
# Assign values and call display()


# =========================
# Q10: INHERITANCE
# =========================

# TODO:
# Create a class `Person` with method `show()`.
# Create a child class `Teacher` that inherits from Person.

class Person:
    def show(self):
        print("I am a person")

class Teacher:
    pass


# =========================
# Q11: POLYMORPHISM
# =========================

# TODO:
# Create two classes Dog and Cat with method `sound()`.
# Both should print different sounds.

class Dog:
    pass

class Cat:
    pass


# =========================
# Q12: ENCAPSULATION
# =========================

# TODO:
# Create a class BankAccount with private variable __balance.
# Add deposit and get_balance methods.

class BankAccount:
    def __init__(self):
        pass


# =========================
# Q13: ABSTRACTION
# =========================

# TODO:
# Use ABC module to create an abstract class Shape
# with abstract method area()

from abc import ABC, abstractmethod

class Shape(ABC):
    pass


# =========================
# Q14: SQL BASICS (THEORY)
# =========================

# TODO:
# Write SQL query (in comment) to:
# 1. Create a table Students(id, name, marks)
# 2. Insert one record
# 3. Select all records


# =========================
# Q15: PYTHON DB CONNECTION
# =========================

# TODO:
# Complete the SQLite connection code.

import sqlite3

def create_connection():
    conn = None
    try:
        # connect to database 'test.db'
        pass
    except Exception as e:
        print(e)
    return conn


# =========================
# Q16: CTE EXPRESSION
# =========================

# TODO:
# Write a SQL CTE query (in comment) to find students with marks > average.


# =========================
# Q17: BUG FIXING
# =========================

# TODO:
# Fix the bug in the function below.

def calculate_average(nums):
    total = 0
    for i in range(len(nums)):
        total += i
    return total / len(nums)

print("Q17 Output:", calculate_average([10, 20, 30]))


# =========================
# Q18: CODE REUSABILITY
# =========================

# TODO:
# Refactor the below code to avoid repetition using a function.

print(2 * 2)
print(3 * 3)
print(4 * 4)


# =========================
# Q19: LOGGING
# =========================

# TODO:
# Replace print statements with logging.

import logging

logging.basicConfig(level=logging.INFO)

def process():
    print("Processing started")
    print("Processing ended")

process()


# =========================
# Q20: BEST PRACTICES
# =========================

# TODO:
# Add proper docstring and comments to this function.

def multiply(a,b):
    return a*b
