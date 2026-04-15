# Q9 (Medium) – Modules
# Fix import issue if files are in different folders

# file: main.py

import utils
# from utils import math_utils
from math_utils import add


print(math_utils.add(2, 3))