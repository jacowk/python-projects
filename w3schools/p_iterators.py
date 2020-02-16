#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:57:09 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_iterators.asp

# Return an iterator from a tuple
mytuple = ("apple", "banana", "cherry")
myiter = iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# Return an iterator from a string
mystr = "banana"
myiter = iter(mystr)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Create an iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

# StopIteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
