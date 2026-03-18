# LISTS — slicing challenge
#
# Slices can also take a step: list[start:stop:step]
#
# Example:
#   nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   print(nums[::2])    # [0, 2, 4, 6, 8]  — every other item
#   print(nums[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  — reversed
#
# Task:
#   Given this list:
#     data = [3, 7, 12, 5, 19, 2, 8, 14, 6, 11]
#
#   Using only slicing (no loops, no extra variables):
#   1. Print the list in reverse.
#   2. Print every other item, starting from the first.
#   3. Print the middle four items.
#   4. Print the last five items in reverse order.

data = [3, 7, 12, 5, 19, 2, 8, 14, 6, 11]

print(data[::-1])
print(data[::2])
print(data[4:8])
print(data[:-6:-1])
