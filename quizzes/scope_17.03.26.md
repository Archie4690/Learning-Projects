# SCOPE QUIZ — answer in comments, no running the code until you've answered
#
# Q1 (quick): What will this print?
#
#   x = 5
#   def foo():
#       print(x)
#   foo()
#
# Answer:
# 
# --- Since the variable x is called outside of the function, the function is still able to use it, and therefore when calling foo() it outputs 5
#
# Q2 (quick): What will this print?
#
#   def foo():
#       y = 5
#   foo()
#   print(y)
#
# Answer:
#
# --- This would output NameError since outside of the function the code does not know about the variable.
#
#
# Q3 (explain): In your own words, what is the difference between
# local and global scope? When would having a variable be global cause problems?
#
# Answer:
#
# --- A local variable is created inside a function and only exists there. Global variables exist outside functions and can be read by the entire file. A variable being global is risky, as it may be overwritten later and therefore cannot be used again. Making it local allows for it to be saved inside of smaller snippets of code and therefore be at less risk of being overwritten. 
