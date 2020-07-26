#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:59:52 2020

@author: jaco

Calculate initial rate of return
"""

earnings_per_share = 4.57
share_price = 59.90
initial_rate_of_return = round((earnings_per_share / share_price) * 100, 2)
print("initial rate of return = {}%".format(str(initial_rate_of_return)))

