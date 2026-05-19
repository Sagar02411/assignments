# Q2. Find all pairs with given sum
# arr = [1,2,3,4,5], target = 6


# arr = [1,2,3,4,5]
# target = 6
# b = []
# for i,v in enumerate(arr):
#     for x in arr[i + 1 : ]:
#         if x + v == target:
#             m = (x,v)
#             b.append(m)

# print(b)

def pairs(arr : list, target : int):
    b = []
    for i,v in enumerate(arr):
        for x in arr[i + 1 : ]:
            if x + v == target:
                m = (x,v)
                b.append(m)
    return b

print(pairs([1,2,3,4,5], 6))