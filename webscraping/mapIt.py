#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:50:04 2020

@author: jaco

https://automatetheboringstuff.com/2e/chapter12/

mapIt.py - Launches a map in the browser using an address from the
command line or clipboard.

Example: python3 mapIt.py "870 Valencia St, San Francisco, CA 94110"

"""

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    print("Getting address from command line")
    # Get address from command line
    address = ''.join(sys.argv[1:])
else:
    print("Getting address from clipboard")
    # Get address from clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)