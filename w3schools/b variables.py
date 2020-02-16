#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:48:56 2019

@author: jaco
"""

x = 5
y = "John"
print(x)
print(y)
x = "James"
print(x)
z = "Jack"
a = 'Jim'
print(z)
print(a)
x, y, z = "Orange", "Banana", "Apple"
print(x)
print(y)
print(z)

name = "Jeff"
print("Hello " + name)
x = 10
y = 10
print(x + y)

name = "Jeffrey"

def sayHello():
    global name 
    name = "Jimmy"
    print("Hello " + name)

sayHello()
print("Hello " + name)

