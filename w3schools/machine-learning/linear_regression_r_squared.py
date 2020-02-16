#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 07:53:16 2019

@author: jaco
"""

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # Age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # Speed

slope, intercept, r, p, std_error = stats.linregress(x, y)

print(r)

# Result: -0.758591524376155
# Close to 1, so we can use linear regression to make future preditions
