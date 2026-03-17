# LOOPS — combining with functions
#
# Task: write a function called `sum_to` that takes a number n
# and returns the sum of all numbers from 1 to n.
#
# For example: sum_to(5) should return 15 (1+2+3+4+5)
# Don't use any built-in sum functions — use a loop.

def sum_to(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total

print(sum_to(int(input("What number do you want? "))))
