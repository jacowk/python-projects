#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:19:02 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_while_loops.asp

print("Loop 1")
i = 1
while i < 6:
    print(i)
    i += 1

print("\nLoop 2")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("\nLoop 2")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
