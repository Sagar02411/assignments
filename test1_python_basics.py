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
    return a + b

print("Q1 Output:", add_numbers(5, 3))


# =========================
# Q2: EXCEPTION HANDLING
# =========================

# TODO:
# Fix the code so that it handles division by zero properly using try-except.

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        return f"Cannot divide by zero. {e}"

print("Q2 Output:", divide(10, 0))


# =========================
# Q3: CUSTOM EXCEPTION
# =========================

# TODO:
# Create a custom exception called InvalidAgeError.
# Raise it if age < 18.

class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Not an adult")
    else:
        return "Eligible"

print("Q3 Output:", check_age(18))


# =========================
# Q4: STANDARD LIBRARIES
# =========================

# TODO:
# Use the random module to generate a random number between 1 and 100.

import random

def generate_random():
    
    return random.randint(1,100)

print("Q4 Output:", generate_random())


# =========================
# Q5: LAMBDA, MAP, FILTER
# =========================

# TODO:
# Use lambda + map to square all numbers in the list.

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))

print("Q5 Output:", list(squared))


# =========================
# Q6: FILTER
# =========================

# TODO:
# Use filter to get only even numbers.

evens = list(filter(lambda x: x%2 == 0, numbers))

print("Q6 Output:", list(evens))


# =========================
# Q7: REDUCE
# =========================

# TODO:
# Use reduce to calculate the product of the list.
import functools
from functools import reduce
import operator 


product = functools.reduce(operator.mul, numbers)

print("Q7 Output:", product)


# =========================
# Q8: MODULE IMPORT ISSUE
# =========================

# TODO:
# Fix the issue: This code assumes a module named `math_utils`
# with a function `multiply(a, b)`.
# Write a comment explaining how to structure the package properly.

# import math_utils 
# from math_utils import multiply
# first import the module andn then import the function. The directory should be : math_utils/multiply()
# print(multiply(2, 3))


# =========================
# Q9: OOP - CLASS & OBJECT
# =========================

# TODO:
# Create a class `Student` with attributes name and marks.
# Add a method `display()` to print details.

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"{self.name} has {self.marks}"
    
s1 = Student("A", 28)
print(s1.display())



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

class Teacher(Person):
    pass


# =========================
# Q11: POLYMORPHISM
# =========================

# TODO:
# Create two classes Dog and Cat with method `sound()`.
# Both should print different sounds.

class Dog:
    def sound(self):
        print("barks")

d1 = Dog()
d1.sound()
class Cat:
    def sound(self):
        print("MEOW")
c1 = Cat()
c1.sound()


# =========================
# Q12: ENCAPSULATION
# =========================

# TODO:
# Create a class BankAccount with private variable __balance.
# Add deposit and get_balance methods.

class BankAccount:
    def __init__(self, deposit, balance):
        self.deposit = deposit
        self.__balance = balance # Private
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self):
        amount = float(input("Enter amount: "))
        self.__balance += amount
        print("\nAmount Deposited:", amount)
        


# =========================
# Q13: ABSTRACTION
# =========================

# TODO:
# Use ABC module to create an abstract class Shape
# with abstract method area()

from abc import ABC, abstractmethod


@abstractmethod
class Shape(ABC):
    def area(self):
        pass 


# =========================
# Q14: SQL BASICS (THEORY)
# =========================

# TODO:
# Write SQL query (in comment) to:
# 1. Create a table Students(id, name, marks)
# 2. Insert one record
# 3. Select all records

# create table Students(id INT,name VARCHAR(20),marks INT);
# insert INTO Students (id, name, marks) VALUES (1, a, 12);
# select * from Students

# =========================
# Q15: PYTHON DB CONNECTION
# =========================

# TODO:
# Complete the SQLite connection code.

import sqlite3

def create_connection():
    conn = None
    try:
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        # Execute a query to get the SQLite version
        query = 'SELECT sqlite_version();'
        cursor.execute(query)

        # Fetch and print the result
        result = cursor.fetchall()
        print('SQLite Version is {}'.format(result[0][0]))

        # Close the cursor after use
        cursor.close()
    except Exception as e:
        print(e)
    return conn


# =========================
# Q16: CTE EXPRESSION
# =========================

# TODO:
# Write a SQL CTE query (in comment) to find students with marks > average.

#select name from Students where marks > avg(marks)
# =========================
# Q17: BUG FIXING
# =========================

# TODO:
# Fix the bug in the function below.

def calculate_average(nums):
    total = 0
    for i in nums:
        total += i
    return total / len(nums)

print("Q17 Output:", calculate_average([10, 20, 30]))

# =========================
# Q18: CODE REUSABILITY
# =========================

# TODO:
# Refactor the below code to avoid repetition using a function.

def multi(a):
    x = [2,3,4]
    square = list(map(lambda x: x**2, x))
    




# =========================
# Q19: LOGGING
# =========================

# TODO:
# Replace print statements with logging.

import logging

logging.basicConfig(level=logging.INFO)

def process():
    logging.info("Processing started")
    logging.info("Processing ended")

process()


# =========================
# Q20: BEST PRACTICES
# =========================

# TODO:
# Add proper docstring and comments to this function.

def multiply(a,b):
    """ multiplies the input numbers and returns the product"""
    return a*b
