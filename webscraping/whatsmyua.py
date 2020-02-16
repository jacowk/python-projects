#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:28:14 2020

@author: jaco

Exercise: Scrape this website, to see what your user agent is using a script
https://www.whatsmyua.info/

"""

import requests, bs4

url = "https://www.whatsmyua.info/"

# Get the web data
res = requests.get(url)

# Write to file
filename = "whatsmyua.htm"
file = open(filename, 'w')
file.write(res.text)
file.close

print(res.text)
