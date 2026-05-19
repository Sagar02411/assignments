# Q1. Rotate a list by k positions
# arr = [1,2,3,4,5], k = 2


arr = [1,2,3,4,5]
k = 2
# print(k)
# result = arr[-k:] + arr[:-k]
# print(result)


def rotate(arr : list, k):
    result = arr[-k:] + arr[:-k]
    return result

print(rotate([1,2,3,4,5], 2))