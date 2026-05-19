# Q7 (Medium) – filter
def get_even_numbers(lst):
    # Use filter + lambda
    evens = list(filter(lambda x: x%2 == 0, numbers))
    return evens

numbers = [1, 2, 3, 4, 5]

print(list(get_even_numbers(numbers)))

