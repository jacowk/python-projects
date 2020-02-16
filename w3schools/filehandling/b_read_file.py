#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:24:52 2020

@author: jaco
"""

f = open("demofile.txt", "r")
#print(f.read(5))
#print(f.read(5)) # Read the first 5 characters
#print(f.readline())

# Loop through the file line by line
"""
for x in f:
    print(x)
"""

# Close the file
print(f.readline())
f.close()
