import random
"""
original_prices = [random.randint(-15, 15) for _ in range(10)]
new_prices = [p if p > 0 else 0 for p in original_prices]

print(original_prices)
print(new_prices)
print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))


nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

print(nums)
print(nums[:5])
print(nums[:-2])
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
print(nums[::-2])

"""

nums = [random.randint(1, 50) for _ in range(20)]
a = 3
b = 12
print(nums)
nums[a:b + 1] = []
print(nums)
