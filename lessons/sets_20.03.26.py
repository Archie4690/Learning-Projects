# SETS
#
# A set is an unordered collection of unique values.
# Duplicates are automatically removed.
#
#   tags = {"python", "data", "python", "science"}
#   print(tags)   # {'python', 'data', 'science'} — one 'python'
#   print(len(tags))  # 3
#
# Create an empty set with set(), not {} — that makes a dict.
#
# Add and remove:
#   tags.add("ml")
#   tags.remove("data")   # KeyError if missing
#   tags.discard("data")  # safe — no error if missing
#
# Membership check (fast, same as dict):
#   print("python" in tags)  # True
#
# Task:
#   You have this list of visitors to a website:
#     visitors = ["alice", "bob", "alice", "charlie", "bob", "alice"]
#
#   1. Convert it to a set and print the number of unique visitors.
#   2. Check if "dave" is in the set and print an appropriate message.
#   3. Add "dave" to the set, then check again and print the result.


visitors = set(["alice", "bob", "alice", "charlie", "bob", "alice"])
print(f"{len(visitors)} total visitors. ")

def checkOnDave():
    if "dave" in visitors:
        print("Dave is visiting!")
    else: 
        print("Dave is not visiting.")

checkOnDave()

visitors.add("dave")

checkOnDave()

print(f"{len(visitors)} total visitors. ")
