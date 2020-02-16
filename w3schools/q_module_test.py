#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:03:19 2019

@author: jaco
"""
import q_module # Imported module
import q_module as test # Imported module
from q_module import person1 as p

q_module.greeting("John Doe")
print("Age: " + str(q_module.person1["age"]))

test.greeting("Jim Doe")

print("Name from p: " + p["name"])

# List all function names in a module
x = dir(test)
print(x)
