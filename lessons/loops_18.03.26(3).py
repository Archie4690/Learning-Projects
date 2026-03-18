# LOOPS — while loops
#
# A `while` loop runs as long as a condition is True.
#
# Example:
#   i = 0
#   while i < 5:
#       print(i)
#       i += 1
#
# Unlike `for`, you control when it stops. Forget to increment and it runs forever.
#
# Task: write a while loop that counts down from 10 to 1 and then prints "Go!".

i = 10
while i > 0:
    print(i)
    i -= 1


print("Go!")
