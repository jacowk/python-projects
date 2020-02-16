#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 06:29:20 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_conditions.asp

a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")    
else:
    print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If Else
print("A") if a > b else print("B")

# One line with 3 conditions
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")

if a > b or a > c:
    print("At least one of the conditions is true")

# Nested ifs
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print(" and also above 20!")
    else:
        print(" and not above 20.")
        
# The pass statement
# Use this for if statements with no contents
if a > b:
    pass