#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:55:48 2019

@author: jaco
"""
#https://www.w3schools.com/python/python_datatypes.asp

# Get the type
# int
x = 5
print(type(x))

# str
x = "Hello world"
print(type(x))

# float
x = 10.5
print(type(x))

# complex
x = 1J
print(type(x))

# list
x = [ "Apples", "Oranges", "Pears" ]
print(type(x))

# tuple
x = ( "Apples", "Oranges", "Pears" )
print(type(x))

# range
x = range(6)
print(type(x))

# dict (Like a Map in Java)
x = {"name" : "John", "age" : 36}
print(type(x))

# set
x = {"apple", "banana", "cherry"}
print(type(x))

# set
x = frozenset({"apple", "banana", "cherry"})
print(type(x))

# bool
x = True
print(type(x))

# bytes
x = b"Hello"
print(type(x))

# bytearray
x = bytearray(5)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(type(x))

# Setting datatypes
x = str("Hello World")
print(type(x))

x = int(20)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = range(6)
print(type(x))

x = dict(name="John", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(type(x))

x = bool(5)
print(type(x))

x = bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))
