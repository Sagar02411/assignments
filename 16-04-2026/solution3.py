
# --------------------------------------------------
# Q3: Complete the Function
# Return a list of unique elements from the given list.
# Example: [1,2,2,3] -> [1,2,3]
# --------------------------------------------------

def unique_elements(lst):
    result = list(set(a))
    print(result)


a = [1, 2, 1, 1, 3, 4, 3, 3, 5]
unique_elements(a)