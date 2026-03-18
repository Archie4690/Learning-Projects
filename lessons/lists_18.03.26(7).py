# LISTS — sorting
#
# Two ways to sort a list:
#   sorted(list)   — returns a new sorted list, original unchanged
#   list.sort()    — sorts the list in place, returns None
#
# Example:
#   nums = [3, 1, 4, 1, 5, 9]
#   print(sorted(nums))  # [1, 1, 3, 4, 5, 9]
#   print(nums)          # [3, 1, 4, 1, 5, 9]  — unchanged
#
#   nums.sort()
#   print(nums)          # [1, 1, 3, 4, 5, 9]  — now changed
#
# Both accept reverse=True to sort descending:
#   sorted(nums, reverse=True)
#
# Task:
#   Given this list:
#     scores = [54, 23, 87, 12, 66, 91, 38]
#
#   1. Print the scores sorted ascending, without modifying the original.
#   2. Print the original list to confirm it's unchanged.
#   3. Sort the list in place and print it.
#   4. Print the scores sorted descending.

scores = [54, 23, 87, 12, 66, 91, 38]

print(sorted(scores))
print(scores)

scores.sort()
print(scores)

print(sorted(scores, reverse=True))
