from functools import reduce
from operator import mul

def product(lst):
    return mul(lst)

lst = [1,2,3,4,5]
res= reduce(mul , lst)
print(res)


