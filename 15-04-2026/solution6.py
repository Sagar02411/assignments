def square_list(lst):
    return lst * lst
a = [1, 2, 3, 4]    
res = list(map(square_list, a))
print(res)