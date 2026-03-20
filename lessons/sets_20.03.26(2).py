# SET OPERATIONS
#
# Union — everything from both sets (no duplicates):
#   a | b
#
# Intersection — only what's in both:
#   a & b
#
# Difference — in one but not the other:
#   a - b
#
# Task:
#   monday = {"alice", "bob", "charlie"}
#   tuesday = {"bob", "charlie", "dave"}
#
#   1. Print everyone who visited on either day.
#   2. Print everyone who visited on both days.
#   3. Print everyone who visited Monday but not Tuesday.

monday = {"alice", "bob", "charlie"}
tuesday = {"bob", "charlie", "dave"}

print(monday | tuesday)
print(monday & tuesday)
print(monday - tuesday)

print(tuesday - monday)
