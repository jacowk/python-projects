#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:57:22 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_dictionaries.asp
# Dictionaries are unordered, changeable and indexed

# Create and print a dictionary
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
print(thisdict)

# Accessing items
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

# Change values
thisdict["year"] = 1984
print(thisdict)

# Loop through a dictionary
# Print all key names
for x in thisdict:
    print(x)

# Print all values
for x in thisdict:
    print(thisdict[x])

# Print all values
for x in thisdict.values():
    print(x)
    
# Print all items
for x, y in thisdict.items():
    print(x, y)

# Check if item exists
if "model" in thisdict:
    print("Model is present")
    
# Dictionary length
print(len(thisdict))

# Adding items
thisdict["color"] = "red"
print(thisdict)

# Remove items
thisdict.pop("model")
print(thisdict)

# Remove last inserted item
thisdict.popitem()
print(thisdict)

# Remove item using del
del thisdict["year"]
print(thisdict)

# Delete the dictionary entirely
del thisdict

# Empty the dictionary
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
thisdict.clear()
print(thisdict)

# Copy a dictionary
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": "1964"
}
mydict = thisdict.copy()
print(thisdict)
print(mydict)

# Another way to copy the dictionary
del mydict
mydict = dict(thisdict)
print(mydict)

# Nested dictionaries example 1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

# Nested dictionaries example 2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# The dict Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# See tons of dictionary methods
