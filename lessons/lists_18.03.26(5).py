# LISTS — looping over lists
#
# You can loop directly over a list with a for loop.
#
# Example:
#   fruits = ["apple", "banana", "cherry"]
#   for fruit in fruits:
#       print(fruit)
#
# If you need the index too, use enumerate():
#   for i, fruit in enumerate(fruits):
#       print(i, fruit)  # 0 apple, 1 banana, 2 cherry
#
# Task:
#   Given this list:
#     scores = [34, 67, 89, 45, 91, 55, 78]
#
#   1. Loop over the list and print each score that is above 60.
#   2. Loop over the list using enumerate() and print the index and score
#      for any score below 50, e.g: "Index 0: 34"

scores = [34, 67, 89, 45, 91, 55, 78]

for i in scores:
    if i>60:
        print(i)

for i, score in enumerate(scores):
    if score<50:
        print(f"Index: {i} --- {score}")
