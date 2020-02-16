#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:42:43 2019

@author: jaco
"""

import numpy
from scipy import stats

ages = [20, 25, 34, 45, 26, 21, 43, 50, 34]

x = numpy.mean(ages)
print("Mean:",x)

x = numpy.median(ages)
print("Median:",x)

x = stats.mode(ages)
print("Mode:",x)

x = numpy.std(ages)
print("Std Dev:",x)

x = numpy.var(ages)
print("Variance:",x)

x = numpy.percentile(ages, 75)
print("Percentile:",x)