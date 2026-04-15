# Q8 (Medium) – reduce
import functools
from functools import reduce
import operator

def product(lst):
    # Use reduce to multiply all elements
    result = functools.reduce(operator.mul, numbers)
    return result

numbers = [1, 2, 3, 4, 5]
print(product(numbers))


