#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:41:18 2019

@author: jaco
"""

import re

pattern = '\d{3}-\d{3}-\d{4}'
value = "My number is 082-949-1405"

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
result = phoneNumRegex.
print(result)

result = re.search(pattern, value)
print(result)
