#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 09:15:07 2020

@author: jaco
"""

"""
In Terminal:
    pip --version
    pip install camelcase
    pip uninstall camelcase
    pip list (List installed packages)

Find modules: https://pypi.org/

"""
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
