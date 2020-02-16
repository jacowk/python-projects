#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:14:39 2020

@author: jaco
"""

from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))
browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('username')
userElem.send_keys('test')
passwordElem = browser.find_element_by_id('user_pass')
password = input('Enter your password') # Do not store passwords in your script
passwordElem.send_keys(password)
passwordElem.submit()

