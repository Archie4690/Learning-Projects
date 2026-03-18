# DICTIONARIES — basics
#
# A dictionary stores key-value pairs. You look up values by key, not by index.
#
# Example:
#   person = {"name": "Alice", "age": 30, "city": "London"}
#   print(person["name"])   # "Alice"
#   person["age"] = 31      # update a value
#   person["job"] = "engineer"  # add a new key
#
# Keys must be unique. Values can be anything.
#
# Task:
#   1. Create a dictionary called `car` with keys: "make", "model", "year", "colour"
#      and values of your choice.
#   2. Print the value of "model".
#   3. Update "year" to a different value.
#   4. Add a new key "mileage" with any number.
#   5. Print the full dictionary.

car = {"make": "BMW", "model": "116D", "year": 2011, "colour": "black"}

print(car["model"])
car["year"] = 2016
car["mileage"] = 124000
print(car)
