# i = "aaabbc"

# b = i.split(',')
# print(b)
# d = {}

# for x in b[0]:
#     if x not in d:
#         d[x] = 1
        
#     else : 
#         d[x] += 1
# m = ""   
# for key, values in d.items():
#     m = m+f"{key}{values}"
    
# print(m)

# a = "aaabbc"
# d = {i: a.count(i) for i in a}
# c = "".join(f"{k+str(v)}" for k, v in d.items())
# print(c)

#remove duplicates
# arr = [1, 2, 2, 3, 4, 4, 5]

# r = []
# for x in arr:
#     if x not in r:
#         r.append(x)
        
# print(r)


# Write a Python program to find the cumulative sum of a list.
# a = [1, 2, 3, 4]
# s = 0
# b = []

# for i in a:
#     s = s+i
#     b.append(s)
    
# print(b)

# a = [10, 5, 3, 4, 3, 5, 6]
# b = []

# for x in a:
#     if x not in b:
#         b.append(x)
#     else:
#         print(x)
#         break
    
# output = 3

# Input = [[1, 2], [3, 4], [5, 6]]
# a = []
# for x in Input:
#     a.extend(x)
# print(a)

# a = [1, 2, 3, 4, 5]
# target = 5
# b=[]

# for i, v in enumerate(a):    
#     for y in a[i + 1 :]:
#         if v + y == target:
#             c = (v,y)
#             b.append(c)
# print(b)


# a = [100, 800, 100, 45, 99]
# # a.sort()
# # print(a[-2])

# b = (max(a))
# # d = list(set(a))
# print(a.index(b))
# a.pop()
# for x in a[1: ]:
#     if c < x:
#         b.append(x)
#         if len(b) == 1:
#             print(b)
        
#     else:
#         print(c)
# v = d.index(m)
# d.pop(v)
# print(d)
# print(b)

#     else:
#         pass
# # print(b)
# print(k)

# try:
#     if x > c:
#         b.insert(-1, x)

#     print(b)    
        
# except Exception as e:
#         pass



# for x in a:
#     if x>=c:
#         b.append(x)
#         # c = x
# print(len(b))
# print(b)
# if len(b) == 1:
#     print(b)

# else:
#     while len(b) >= 2:
#         for x in b:
#             if x>=c:
                
#                 b.insert(0,x)
#     print(b)
# print(b[-2])

# arr = ['a', 'b', 'a', 'c', 'b', 'a']
# b = {}

# for x in arr:
#     if x in b:
#         b[x] = b[x] + 1
#     else:
#         b[x] = 1
        
# print(b)

# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}

# d1.update(d2)
# print(d1)



# s1 = "abcd"
# s2 = "cdab"

# for _ in range(len(s1)):
#     s1 = s1[-1] + s1[:-1]
#     if s1 == s2:
#         print("True")
        
        
# a = s1.split()
# c = s2.split()
# print(a)
# b = {}
# d = {}

# for x in a[0]:
#     if x in b:
#         b[x] = b[x] + 1
#     else:
#         b[x] = 1
        
# print(b)
# for x in c[0]:
#     if x in c:
#         d[x] = d[x] + 1
#     else:
#         d[x] = 1

# if b == c:
#     print("rotation")
    
# else:
#     print("no")

# print(m)
# k = True
# for i in range(len(c)):   
#     if c[i] == d[i]:
#         print("Rotation")

# Input = [8, 2, 1, 4, 6]

# x = min(Input)
# Input.pop(x)

# print(min(Input))

# Input = 1234
# a = [Input]

# b = 0
# for x in a:
#     b = b + int(x)
    
# print(b)


# a = [-8, 2, 1, 4, 6, -1]
 
# min = second_min = a[0]
 
# for i in a:
#     if i < min:
#         second_min = min
#         min = i
#     elif i < second_min and i > min:
#         second_max = i
 
# print(second_min)

# Write a Python program to move all zeros to end of list.
# Output: [1, 2, 3, 4, 0, 0, 0]

# Input = [1, 0, 2, 0, 3, 0, 4]
# b = []
# c = []
# for x in Input:
#     if x == 0:
#         b.append(x)

# # for x in Input:
#     else:
#         b.insert(0, x)
        
# print(b)
# print(c)
# d = c + b
# print(d)

# s = "abcdabcdbbdd"
# i = 0
# j = 1
# max1 = 0
# while i < len(s) and j < len(s):
#     if s[i] != s[j]:
#         j = j + 1
#     else:
#         max1 = max(max1, j - i)
#         i = i + 1
#         j = i + 1


# print(max1)
# a = [1, 2, 3, 4, 5]
# target = 5
# b=[]

# for i, v in enumerate(a):    
#     for y in a[i + 1 :]:
#         if v + y == target:
#             c = (v,y)
#             b.append(c)
# print(b)

# Input = ["eat", "tea", "tan", "ate", "nat", "bat"]
# b = []

# for i,v in enumerate(Input):
#     for y in Input[i+1 : ]:
#         if sorted(v) == sorted(y):
#             c = (v,y)
#             b.append(c)

# print(b)

# Output:
# [
# ['eat', 'tea', 'ate'],
# ['tan', 'nat'],
# ['bat']
# ]


# Input = ["eat", "tea", "tan", "ate", "nat", "bat"]
# groups = {}

# for word in Input:
#     key = "".join(sorted(word))  # canonical form
    
#     if key not in groups:
#         groups[key] = []
    
#     groups[key].append(word)

# output = list(groups.values())
# print(output)

# f = {}
# for x in Input:
#     key = "".join(sorted(x))
#     if key not in f:
#         f[key] = [] 
#         print(key)
            
#     f[key].append(x)

# output = list(f.values())
# print(output)


s = "aabbcdeff"

b = list(s)

print(b)
c = []

for x in b:
    if x not in c:
        c.append(x)
    else:
        print(x)
        break
