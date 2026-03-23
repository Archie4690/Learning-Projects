# File I/O — Reading and Writing Files
#
# Python opens files with the open() function.
# You pass it a filename and a mode:
#   "r"  — read (default)
#   "w"  — write (overwrites the file)
#   "a"  — append (adds to the end)
#
# Always use a `with` block — it closes the file automatically.
#
# Example — writing:
#   with open("notes.txt", "w") as f:
#       f.write("hello\n")
#
# Example — reading:
#   with open("notes.txt", "r") as f:
#       content = f.read()
#   print(content)
#
# -------------------------------------------------------
# TASK:
# Write a program that:
#   1. Asks the user to enter a note (a single line of text)
#   2. Saves it to a file called "notes.txt"
#   3. Reads the file back and prints its contents
#
# Run it twice — what happens to the previous note on the second run?
# -------------------------------------------------------

with open("notes.txt", "w") as f:
    f.write(input("What would you like to write? "))

with open("notes.txt", "r") as f:
    content = f.read()
print(content)
