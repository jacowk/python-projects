#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:02:43 2020

@author: jaco

searchpypi.py  - Opens several search results.

https://automatetheboringstuff.com/2e/chapter12/
"""
# searchpypi.py

import requests, sys, webbrowser, bs4

print("Searching") # Display text while downloading results page


# DON'T RUN THIS SCRIPT

# res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
try:
    res.raise_for_status()
    
    # Retrieve top search result links
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    # Open a browser tab for each result
    linkElems = soup.select('.package-snippet')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)
except Exception as exc:
    print("There was a problem: %s" % (exc))
        

