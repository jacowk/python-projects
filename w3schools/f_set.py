#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:43:51 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_sets.asp

# Sets are unordered and unindexed

# Set example
thisset = { "apple", "banana", "cherry" }
print(thisset)

# Access items
# Because sets are not indexed, you cannot use an index to access the items
for x in thisset:
    print(x)
print('banana' in thisset) # True

# Add items
thisset.add("orange")
print(thisset)

# Add multiple items
thisset.update(["mango", "grapes"])
print(thisset)

# Get the length
print(len(thisset))

# Remove an item
thisset.remove("banana")
print(thisset)
thisset.discard("mango") # Same as remove
print(thisset)
x = thisset.pop();
print(x)
x = thisset.pop();
print(x)
print(thisset)

# Empty the test
thisset = { "apple", "banana", "cherry" }
thisset.clear()
print(thisset)

# Delete the set
thisset = { "apple", "banana", "cherry" }
del thisset

# Join 2 sets with union
set1 = { "a", "b", "c" }
set2 = { 1, 2, 3 }
set3 = set1.union(set2)
print(set3)

# Join 2 sets with update
set1 = { "a", "b", "c" }
set2 = { 1, 2, 3 }
set1.update(set2)
print(set1)

# Set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

