# LISTS — slicing
#
# You can grab a chunk of a list using a slice: list[start:stop]
# `start` is inclusive, `stop` is exclusive.
#
# Example:
#   nums = [10, 20, 30, 40, 50]
#   print(nums[1:4])   # [20, 30, 40]
#   print(nums[:2])    # [10, 20]      (start defaults to 0)
#   print(nums[3:])    # [40, 50]      (stop defaults to end)
#
# Task:
#   Given this list:
#     scores = [45, 72, 88, 56, 91, 63, 77]
#
#   Without changing the list, print:
#   1. The first three scores
#   2. The last two scores
#   3. Everything except the first and last score
