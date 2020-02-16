#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 07:24:01 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_ml_linear_regression.asp

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # Age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # Speed

slope, intercept, r, p, std_error = stats.linregress(x, y)

def myfunc(x):
    calc = slope * x + intercept
    print("x:",x," calc:",calc)
    return calc

# mymodel represents new values for the y-axis, used to draw in the regression line
# This line is used to predict future values
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()