# SCOPE — reassignment gotcha
#
# You can read a global variable inside a function.
# But try to reassign it and Python creates a new local variable instead.
#
# Task: define a variable `count = 10` globally.
# Write a function that tries to set `count = 99` and then prints it.
# Call the function, then print `count` outside it.
# What do you expect? Run it and see if you're right.
