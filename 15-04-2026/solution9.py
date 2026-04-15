# Q9 (Medium) – Modules
# Fix import issue if files are in different folders

# file: main.py
# import math_utils
# print(math_utils.add(2, 3))
from utils.custom_maths_utils.test_custom_maths_utils import _add_custom
print(_add_custom(2, 3))