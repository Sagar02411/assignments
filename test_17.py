def calculate_average(nums):
    total = 0
    for i in nums:
        total += i
    return total / len(nums)

print("Q17 Output:", calculate_average([10, 20, 30]))