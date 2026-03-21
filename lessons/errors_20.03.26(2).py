# ERRORS — try/except
#
# When code might fail, wrap it in a try/except block:
#
#   try:
#       result = 10 / 0
#   except ZeroDivisionError:
#       print("Can't divide by zero")
#
# The except block only runs if that specific error occurs.
# If no error — it's skipped entirely.
#
# Task:
#   Ask the user to enter a number.
#   Divide 100 by that number and print the result.
#   Handle two cases:
#     - They enter zero (ZeroDivisionError)
#     - They enter something that isn't a number (ValueError)
#   Print an appropriate message for each.

def div100():
    try:
        userNum = int(input("What number would you like? "))
        print(100/userNum)
    except ValueError:
        print("Please pick a number")
        div100()
    except ZeroDivisionError:
        print("Don't be a smartass")
        div100()

div100()
