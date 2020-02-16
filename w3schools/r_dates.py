#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:17:19 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_datetime.asp

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)

# Format output
print(x.strftime("%A"))

# Create a datetime object
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime("%B")) 


