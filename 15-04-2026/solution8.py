from functools import reduce

def product(x,y):
    return lst[x] * lst[y]

a = [1,2,3,4,5]
res=list(reduce(lambda x, y: x * y, a))
print(res)



