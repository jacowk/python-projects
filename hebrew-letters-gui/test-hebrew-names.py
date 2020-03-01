#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:54:04 2020

@author: jaco
"""
import html

unicode = u"\u05d9\u05b7\u05e2\u05b2\u05e7\u05b9\u05d1"

for letter in unicode:
    print(letter)

#unicode_list = [u"\u05d9", u"\u05b7", u"\u05e2", u"\u05b2", u"\u05e7", u"\u05b9", u"\u05d1"]
#for item in unicode_list:
#    print(html.unescape(item))