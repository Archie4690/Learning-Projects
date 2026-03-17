# TESTING & DEBUGGING
#
# The simplest form of testing is an assertion — telling Python
# "this should be true, crash if it isn't."
#
# Example:
#   
#   result = add(2, 3)
#   assert result == 5
#
# If the assertion fails, Python raises an AssertionError.
# If it passes, nothing happens — silence is success.
#
# Task: write a function called `multiply` that takes two numbers and returns their product.
# Then write three assert statements to test it:
#   - one that should pass
#   - one that tests an edge case (think: what happens with 0?)
#   - one that you deliberately make fail, just to see the error
def multiply(num1, num2):
    result = num1 * num2
    return result

assert multiply(3, 4) == 12
assert multiply(3, 0) == 0
assert multiply(3, 5) == 10 # Always fails under AssertionError


chosenNum1 = int(input("What number do you want first? "))
chosenNum2 = int(input("What number do you want second? "))

print(multiply(chosenNum1, chosenNum2))


