#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:15:55 2020

@author: jaco
"""

from matplotlib import pyplot as plt
DayOfWeekOfCall = [1,2,3]
DispatchesOnThisWeekday = [77, 32, 42]

LABELS = ["Monday", "Tuesday", "Wednesday"]

plt.bar(DayOfWeekOfCall, DispatchesOnThisWeekday, align='center')
plt.xticks(DayOfWeekOfCall, LABELS)
plt.show()