#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:22:27 2020

@author: jaco
"""

import requests, bs4

url = "https://www.behindthename.com/names/usage/biblical-hebrew"

# Get the web data
res = requests.get(url)

# Write to file
filename = "hebrew-names.htm"
file = open(filename, 'w')
file.write(res.text)
file.close

print(res.text)