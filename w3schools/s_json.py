#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:20:29 2019

@author: jaco
"""

# https://www.w3schools.com/python/python_json.asp

# http://jsoneditoronline.org/  - To look at an unformatted JSON file

import json

# some json
x = '{ "name":"John", "age":30, "city":"New York" }'

# parse json
y = json.loads(x)

# output
print(y["name"])
print(y["age"])
print(y["city"])

x = { 
     "name":"Jim",
     "age":40,
     "city":"LA"
}

# convert dictionary to JSON
y = json.dumps(x)
print(y)

# Different datatypes
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Format output
print("\nFormat result with indent")
print(json.dumps(x, indent=4))

print("\nFormat result by overridding default seperators")
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print("\nFormat result by ordering the result")
print(json.dumps(x, indent=4, sort_keys=True))