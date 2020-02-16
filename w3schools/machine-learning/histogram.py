#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:57:26 2019

@author: jaco
"""
# https://www.w3schools.com/python/python_ml_data_distribution.asp

import numpy
import matplotlib.pyplot as plt

# Generate 250 random values between 0.0 and 5.0
x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()

