
# --------------------------------------------------
# Q6: Debug the Code
# The function should find the maximum number in a list.
# --------------------------------------------------


def find_max(lst):
    max_val = lst[0]  
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

numbers = [1, 2, 3, 4, 5]
print(find_max(numbers))


