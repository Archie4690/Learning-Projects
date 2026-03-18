# DICTIONARIES — looping and methods
#
# Three useful ways to loop over a dictionary:
#   for key in d:               — loops over keys
#   for key in d.keys():        — same, more explicit
#   for value in d.values():    — loops over values
#   for key, value in d.items(): — loops over both
#
# Example:
#   person = {"name": "Alice", "age": 30}
#   for key, value in person.items():
#       print(key, value)
#   # name Alice
#   # age 30
#
# Task:
#   Given this dictionary:
#     stock = {"apples": 12, "bananas": 5, "cherries": 31, "dates": 0, "elderberries": 8}
#
#   1. Print every item in the format: "apples: 12"
#   2. Print only the names of items that are out of stock (value is 0).
#   3. Print the total number of items across all stock (sum of all values).

stock = {"apples": 12, "bananas": 5, "cherries": 31, "dates": 0, "elderberries": 8}

for key, value in stock.items():
    print(f"{key}: {value}")

print("")

for key, value in stock.items():
    if value != 0:
        print(f"{key}: {value}")
    else: 
        print(f"{key}: Out of stock")

print(f"{sum(stock.values())} total items.")
