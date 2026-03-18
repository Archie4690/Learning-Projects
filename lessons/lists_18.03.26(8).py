# LISTS — list comprehensions
#
# A list comprehension builds a new list in one line.
#
# Instead of:
#   doubles = []
#   for n in nums:
#       doubles.append(n * 2)
#
# You can write:
#   doubles = [n * 2 for n in nums]
#
# You can also add a condition:
#   evens = [n for n in nums if n % 2 == 0]
#
# Task:
#   Given this list:
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#   Using list comprehensions only (no loops):
#   1. Create a list of each number squared.
#   2. Create a list of only the odd numbers.
#   3. Create a list of the squares of only the odd numbers.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = [n**2 for n in nums]
print(squared)

odd = [n for n in nums if n % 2 == 1] #why do I need the n at the start? 
print(odd)


oddSquared = [n**2 for n in nums if n % 2 == 1]
print(oddSquared)
