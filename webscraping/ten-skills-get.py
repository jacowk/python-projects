#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:01:01 2020

@author: jaco
"""

import requests, bs4

url = "https://dev.to/javinpaul/10-skills-java-programmer-can-learn-to-accelerate-their-career-3nlh"

# Get the web data
res = requests.get(url)

# Write to file
filename = "ten-skills.htm"
file = open(filename, 'w')
file.write(res.text)
file.close

print(res.text)
