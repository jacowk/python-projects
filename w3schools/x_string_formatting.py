#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:09:51 2020

@author: jaco
"""

# Example 1
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Example 2
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Format reference https://www.w3schools.com/python/ref_string_format.asp

# Multiple values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Refer to the same value more than once
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
