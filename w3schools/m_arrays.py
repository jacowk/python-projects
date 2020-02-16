#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 07:50:57 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_arrays.asp

# Define an array
cars = [ "Ford", "Volvo", "BMW" ]
print(cars)

# Access the elements of an array
x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)

# The length of an array
x = len(cars)
print(x)

# Loop array elements
for x in cars:
    print(x)

# Adding array elements
cars.append("Honda")
print(cars)

# Removing array elements
cars.pop(1)
print(cars)

cars.remove("Honda")
print(cars)

# See other array methods

