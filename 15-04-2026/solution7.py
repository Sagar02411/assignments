def get_even_numbers(lst):
    return lst % 2 == 0

a = [1,2,3,4]
res=list(filter(get_even_numbers,a))
print(res)
