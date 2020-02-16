#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 07:44:20 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_lambda.asp

"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

lambda arguments : expression
"""

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambda Functions
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))