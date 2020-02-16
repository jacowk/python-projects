#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:45:22 2020

@author: jaco
"""

from matplotlib import pyplot as plt
import numpy as np

##generating some data
years = [1936, 1945]+[i for i in range(1947,1997)]
data1 = np.random.rand(len(years))
data2 = np.random.rand(len(years))

diabete = {key: val for key,val in zip(years, data1)}
not_diabete = {key: val for key,val in zip(years, data2)}



##the actual graph:
fig, ax = plt.subplots(figsize = (10,4))

idx = np.asarray([i for i in range(len(years))])

width = 0.2

ax.bar(idx, [val for key,val in sorted(diabete.items())], width=width)
ax.bar(idx+width, [val for key,val in sorted(not_diabete.items())], width=width)

ax.set_xticks(idx)
ax.set_xticklabels(years, rotation=65)
ax.legend(['Diabete', 'Non-Diabete'])
ax.set_xlabel('years')
ax.set_ylabel('# of patients')

fig.tight_layout()

plt.show()