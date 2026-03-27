# File I/O — Reading Multiple Lines
#
# f.read()      — reads the whole file as one string
# f.readlines() — reads the file into a list, one item per line
# You can also loop directly:
#   with open("notes.txt") as f:
#       for line in f:
#           print(line)
#
# -------------------------------------------------------
# TASK:
# Extend your notes program so that:
#   1. Each new note is APPENDED to notes.txt (not overwritten)
#   2. After saving, it reads the file back and prints ALL notes,
#      numbered — like this:
#
#      1. Buy milk
#      2. Call dentist
#      3. Fix bike
#
# Hint: readlines() returns a list. What does each element look like?
# -------------------------------------------------------

with open ("notes.txt", "a") as note:
    text = input(f"What would you like to add?")
    note.write(f"{text}\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
