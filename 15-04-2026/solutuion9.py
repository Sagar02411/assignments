# Q9 (Medium) – Modules
# Fix import issue if files are in different folders

# file: main.py
# import math_utils
# print(math_utils.add(2, 3))
from utils.maths_utils.math_utils import add
print(math_utils.add(2, 3))