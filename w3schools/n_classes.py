#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 07:59:38 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_classes.asp

# Create a class
class MyClass:
    x = 5

# Create an object
p1 = MyClass()
print(p1.x)

""" 
__init__() function is always called when a class is being initiated

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 36)
print(p1.name)
print(p1.age)