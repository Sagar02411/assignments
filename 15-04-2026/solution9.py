# Q9 (Medium) – Modules
# Fix import issue if files are in different folders

# file: main.py

# from utils import math_utils
from utils.maths_utils.math_utils import add


print(add(2, 3))