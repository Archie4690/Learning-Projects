# LISTS — indexing and append
#
# A list holds ordered values. You access items by index (starting at 0).
# Negative indexes count from the end: -1 is the last item.
#
# Example:
#   colours = ["red", "green", "blue"]
#   print(colours[1])   # "green"
#   print(colours[-1])  # "blue"
#   colours.append("yellow")
#
# Task:
#   1. Create a list called `temperatures` with these five values: 12, 18, 7, 24, 15
#   2. Print the first and last item using indexing.
#   3. Append the value 20 to the list.
#   4. Print the full list.

temps = [12, 18, 7, 24, 15]
newTemp = int(input(f"the first temperature is {temps[0]} and the last temperature is {temps[-1]}. What would you like the final temperature to be? "))
temps.append(newTemp)
print(temps)
