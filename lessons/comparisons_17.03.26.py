# COMPARISONS
#
# Comparison operators return True or False:
#
#   ==   equal to
#   !=   not equal to
#   >    greater than
#   <    less than
#   >=   greater than or equal to
#   <=   less than or equal to
#
# Example:
#   print(5 > 3)   # True
#   print(5 == 6)  # False
#
# Task: write a function called `is_even` that takes a number
# and returns True if it's even, False if it's odd.
# Hint: you've seen the operator you need for this today.

def is_even(num):
    return num % 2 == 0

chosenNum = int(input("Is this number even: "))
print(is_even(chosenNum))
