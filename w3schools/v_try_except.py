#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 09:20:08 2020

@author: jaco
"""

# https://www.w3schools.com/python/python_try_except.asp

# Example 1
try:
    print(x)
except:
    print("An exception occurred")

# Example 2
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
    
# Example 3
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# Example 4
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
# Example 5: Raise an exception
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 
  