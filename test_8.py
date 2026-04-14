from functools import reduce
numbers = [1,2,3,4,5]
product = list(reduce(lambda x,y: x * y,numbers))
print(product)