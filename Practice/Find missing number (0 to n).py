# Q4. Find missing number (0 to n)
# arr = [0,1,3]


arr = [0,1,3]

# for i,v in enumerate(arr):
#     for x in arr[i+1 :]:
#         if v + 1 == x:
#             pass
#         else:
#             print(x)

for x in arr:
    for y in arr[1:]:
        if x + 1 == y:
            