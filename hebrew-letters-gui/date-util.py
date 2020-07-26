#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun 26 July 2020

@author: Jaco Koekemoer

"""
import datetime

x = datetime.datetime.now()
day = x.strftime("%d")
month = x.strftime("%m")
year = x.strftime("%Y")

print(x)
print(day)
print(month)
print(year)
