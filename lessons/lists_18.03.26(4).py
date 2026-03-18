# LISTS — modifying lists
#
# Lists are mutable — you can change individual items by index.
#
# Example:
#   nums = [10, 20, 30]
#   nums[1] = 99
#   print(nums)  # [10, 99, 30]
#
# You can also remove items:
#   nums.pop()       # removes and returns the last item
#   nums.pop(0)      # removes and returns item at index 0
#   nums.remove(99)  # removes the first occurrence of the value 99
#
# Task:
#   Start with this list:
#     items = ["apple", "banana", "cherry", "date", "elderberry"]
#
#   1. Replace "cherry" with "mango" using its index.
#   2. Remove the last item using pop().
#   3. Remove "banana" by value.
#   4. Print the final list.


items = ["apple", "banana", "cherry", "date", "elderberry"]
print(items)

items[2] = "mango"
print(items)
items.pop()
print(items)
items.remove("banana")
print(items)
