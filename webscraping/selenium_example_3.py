#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:23:26 2020

@author: jaco
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
print(type(browser))
browser.get('https://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)

'''
Clicking browser buttons:
-------------------------
    
browser.back() Clicks the Back button.

browser.forward() Clicks the Forward button.

browser.refresh() Clicks the Refresh/Reload button.

browser.quit() Clicks the Close Window button.

'''
