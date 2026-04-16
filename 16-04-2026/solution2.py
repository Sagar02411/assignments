def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:   # Bug here
            total += num
    return total
print(sum_even([1,2,3,4]))