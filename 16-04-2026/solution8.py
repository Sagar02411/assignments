def merge_sorted(list1, list2):
    list1.extend(list2)
    return list1
    #return list1+list2

print(merge_sorted([1,2,3,4], [1,2,3]))