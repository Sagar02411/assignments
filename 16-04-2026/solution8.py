
# --------------------------------------------------
# Q8: Implementation
# Write a function to merge two sorted lists.
# Example: [1,3,5], [2,4] -> [1,2,3,4,5]
# --------------------------------------------------

def merge_sorted(list1, list2):
    
    
    c = sorted(list1 + list2)
    return c


list1 =  [1,3,5]
list2 = [2,4]

print(merge_sorted(list1,list2))