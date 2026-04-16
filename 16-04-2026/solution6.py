def find_max(lst):
    max_val = lst[0]   # Bug here
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val
print(find_max([1,2,3,4]))