#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:59:52 2020

@author: jaco

Calculate CAGR - Compound Annual Growth Rate
"""

end_value = 4.75
beginning_value = 0.24
no_of_years = 11

#end_value = 5000
#beginning_value = 1000
#no_of_years = 5

step1 = end_value / beginning_value
print("step1 = {}".format(step1))
step2 = 1 / no_of_years
print("step2 = {}".format(step2))
step3 = step1 ** step2 #Exponent
print("step3 = {}".format(step3))
cagr = round((step3 - 1) * 100, 2)
print("cagr = {}%".format(str(cagr)))

