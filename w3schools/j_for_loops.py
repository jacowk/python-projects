#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 07:12:56 2019

@author: jaco
"""
# https://www.w3schools.com/python/python_for_loops.asp

# Loop through a list
fruits = [ "apple", "banana", "cherry" ]
for x in fruits:
    print(x)

# Loop through a string
for x in "banana":
    print(x)
    
# Break statement
fruits = [ "apple", "banana", "cherry" ]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
# Continue statement
fruits = [ "apple", "banana", "cherry" ]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print("\n")

# The range() function
for x in range(6):
    print(x)
print("\n")
    
for x in range(2, 5):
    print(x)
print("\n")

for x in range(2, 30, 3):
    print(x)
print("\n")    

# Else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished")
print("\n")

# Nested for loop
adj = [ "red", "big", "tasty" ]
fruits = [ "apple", "banana", "cherry" ]
for x in adj:
    for y in fruits:
        print(x, y)
print("\n")

# Pass statement - Used with empty lists to prevent errors
for x in [1, 2, 3]:
    pass
print("\n")