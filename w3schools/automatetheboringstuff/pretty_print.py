#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:31:29 2019

@author: jaco
"""

import pprint
person = { 'name': 'John Doe', 'age': 30, 'gender': 'male' }
print(person)
pprint.pprint(person) # Sorts the keys when output
print(pprint.pformat(person)) # Does exactly the same
