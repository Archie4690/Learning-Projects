# SOLO PROJECT — Temperature Tracker
#
# Build a program that tracks daily temperatures.
#
# Requirements:
#   1. Start with an empty list called `temperatures`.
#   2. Use a loop to ask the user for 5 temperature readings (one at a time),
#      appending each to the list.
#   3. After all inputs are collected, print:
#      - The full list
#      - The highest temperature
#      - The lowest temperature
#      - The average temperature (rounded to 1 decimal place)
#
# Hints:
#   - You already know loops, lists, input(), and basic arithmetic.
#   - max(), min(), and len() are built-in functions you can use — try to
#     figure out what they do from their names.
#   - round(value, 1) rounds to 1 decimal place.
#
# Don't look anything up. Have a go and let me know when you're done.

temperature = []
averageTemp = 0
for i in range(5):
    newTemp = int(input("What temperature would you like to record? "))
    temperature.append(newTemp)

print(temperature)
print(f"The highest temperature is {max(temperature)} and the lowest is {min(temperature)}")
averageTemp = round(sum(temperature) / len(temperature), 1)
print(f"The average temperature is {averageTemp}")
