# LISTS — the `in` operator
#
# `in` checks whether a value exists in a list. Returns True or False.
#
# Example:
#   fruits = ["apple", "banana", "cherry"]
#   print("banana" in fruits)   # True
#   print("mango" in fruits)    # False
#
# You can also use `not in`:
#   print("mango" not in fruits)  # True
#
# Task:
#   Given this list:
#     allowed = ["alice", "bob", "charlie", "diana"]
#
#   1. Ask the user to enter a name.
#   2. If the name is in the list, print "Access granted."
#   3. If not, print "Access denied."

allowed = ["alice", "bob", "charlie", "diana"]

userName = input("What is your name? ")
if userName.lower() in allowed:
    print("Access Granted")
else: 
    print("Feck off tosser")
