"""
Instructions:
- Complete each function
- Follow best practices (PEP8, docstrings, comments)
"""

# Q1 (Easy) – Functions
def square(n):
    # TODO: return square of n
    pass


# Q2 (Easy) – Exception Handling
def safe_divide(a, b):
    # Return result of a/b
    # If division by zero occurs, return "Cannot divide by zero"
    pass


# Q3 (Easy-Medium) – Custom Exception
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    # Raise NegativeNumberError if n < 0
    # Otherwise return "Valid"
    pass


# Q4 (Medium) – os Library
import os

def get_text_files(path):
    # Return list of .txt files in directory
    pass


# Q5 (Medium) – random Library
import random
import string

def generate_password(length):
    # Generate random password using letters and digits
    pass


# Q6 (Medium) – Lambda + map
def square_list(lst):
    # Return new list with squared values using map
    pass


# Q7 (Medium) – filter
def get_even_numbers(lst):
    # Use filter + lambda
    pass


# Q8 (Medium) – reduce
from functools import reduce

def product(lst):
    # Use reduce to multiply all elements
    pass


# Q9 (Medium) – Modules
# Fix import issue if files are in different folders

# file: main.py
# import math_utils
# print(math_utils.add(2, 3))



# Q10 (Medium) – OOP (Classes & Objects)
class Student:
    def __init__(self, name, marks):
        # Initialize attributes
        pass
    
    def display(self):
        # Print "Name: X, Marks: Y"
        pass


# Q11 (Medium) – Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    # Override speak method to return "Dog barks"
    pass


# Q12 (Medium) – Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    # Add method to deposit amount
    # Add method to get balance safely


# Q13 (Medium) – Polymorphism
class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

def animal_sound(animal):
    # Call sound() method
    pass


# Q14 (Medium) – SQL + Python DB Connection
import sqlite3

def create_and_insert():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    
    # Create table students(id, name)
    # Insert 2 records
    
    conn.commit()
    conn.close()


# Q15 (Medium) – Logging + Best Practices
def divide(a, b):
    # Add logging
    # create logging file .log
    # Handle exceptions properly
    return a / b