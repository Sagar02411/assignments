# Q6 (Medium) – Lambda + map
def square_list(lst):
    squared = list(map(lambda x: x**2, numbers))
    return squared

numbers = [1, 2, 3, 4, 5]
print(list(square_list(numbers)))
    
