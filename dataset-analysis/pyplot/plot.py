#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:23:56 2020

@author: jaco
"""
import matplotlib.pyplot as plt

x = [1,2,3]
xt = ["Jan", "Feb", "Mar"]
y = [2,4,6]
plt.plot(x, y)
plt.xticks(x, xt)
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("Main Title")
plt.show()
