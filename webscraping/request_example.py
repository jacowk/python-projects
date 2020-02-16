#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:10:47 2020

@author: jaco

https://automatetheboringstuff.com/2e/chapter12/

Unicode encodings:
    https://www.joelonsoftware.com/articles/Unicode.html
    https://nedbatchelder.com/text/unipain.html

Requests module:
https://requests.readthedocs.org/.

"""

import requests

playFile = open("RomeoAndJuliet.txt", "wb")
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
#res = requests.get("https://automatetheboringstuff.com/page_not_exist")
try:
    res.raise_for_status() # Always do this
    print(type(res))
    if res.status_code == requests.codes.ok:
        print("status ok")
    print(len(res.text))
    print(res.text[:250])
    
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
except Exception as exc:
    print("There was a problem: %s" % (exc))
finally:
    playFile.close()
    
