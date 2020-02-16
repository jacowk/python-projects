#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:52:56 2019

@author: jaco
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Access tuple
print(thistuple[1])

# Negative indexing
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Range of Negative Indexes
print(thistuple[-4:-1])

# Changing Tuple Values
# Tuples are immutable. So to change a value, convert to list, change and convert back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Loop through a tuple
for x in thistuple:
    print(x)
    
# Check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' exists in the tuple")

# Tuple length
print(len(thistuple))

# Add items
# Not possible since tuples are immutable
#thistuple[3] = "orange"

# Create tuple with one item
thistuple = ("apple",) #You need to add the comma
print(thistuple)

# Remove items
# Tuples are unchangeable, so items cannot be removed
# It is possible to delete tuples
thistuple = ("apple", "banana", "cherry")
del(thistuple)
#print(thistuple) # Not possible since tuple is deleted

# Join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Tuple methods
# count()
# index()
 
