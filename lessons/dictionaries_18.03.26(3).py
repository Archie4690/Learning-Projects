# DICTIONARIES — get() and checking keys
#
# Accessing a key that doesn't exist crashes with a KeyError.
# Use .get() to safely retrieve a value with a fallback:
#
#   d = {"name": "Alice"}
#   print(d["age"])          # KeyError!
#   print(d.get("age"))      # None
#   print(d.get("age", 0))   # 0  — your chosen default
#
# Check if a key exists with `in`:
#   print("name" in d)   # True
#   print("age" in d)    # False
#
# Task:
#   Given this dictionary:
#     scores = {"alice": 88, "bob": 74, "charlie": 91}
#
#   1. Ask the user to enter a name.
#   2. Use .get() to retrieve their score. If they're not in the dictionary,
#      print "Player not found." Otherwise print their score.
#   3. Before retrieving, also check with `in` and print either
#      "Name is registered" or "Name is not registered".

scores = {"alice": 88, "bob": 74, "charlie": 91}

userName = input("What is your name? ")
if scores.get(userName) == False:
    print("Player not found")
else:
    print(scores[userName])
