#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:31:37 2020

@author: jaco

https://automatetheboringstuff.com/2e/chapter12/

"""
import requests, bs4

res = requests.get("https://nostarch.com/automatestuff2/")
try:
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    '''
    noStarchSoup = bs4.BeautifulSoup(res.text, 'lxml.parser') # Faster
    pip install --user lxml
    '''
    print(type(noStarchSoup))
except Exception as exc:
    print("There was a problem: %s" % (exc))
