#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 09:31:00 2020

@author: jaco
"""

from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' % elem.tag_name)
except:
    print('Was not able to find an element with that name.')
    
# Click a link element
linkElem = browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click()

text = input('Press enter to close the browser')
browser.close()
