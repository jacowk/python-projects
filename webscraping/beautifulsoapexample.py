#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:49:45 2020

@author: jaco
"""

import bs4

exampleFile = open("example.html")
exampleData = exampleFile.read()
print(exampleData)
exampleSoup = bs4.BeautifulSoup(exampleData, 'html.parser')
elems = exampleSoup.select("#author")
print(len(elems))
print(type(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)
print("\n")

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())
print("\n")

spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
exists = spanElem.get('some_nonexistent_addr') == None
print(exists)
print(spanElem.attrs)
