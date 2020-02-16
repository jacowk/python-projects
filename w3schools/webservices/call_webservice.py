#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:37:12 2019

@author: jaco
"""

"""
Login credentials
https://developer.here.com
Username: gmail
Password: 100_g00d9oy%

App ID: TwfmL0YSW5hTioe4b57p
API Key: LwyrCyWP_uZZQR1Qcf3Sw1OXVH0fj87TcwwRZODtVn4
"""

# Public transport data (Not REST APIs)
# https://www.transitwiki.org/TransitWiki/index.php/Publicly-accessible_public_transportation_data

# Public transit data (REST APIs)
# https://developer.here.com/documentation/transit/dev_guide/topics/quick-start-routing.html

# Webservice example
# https://www.pythonforbeginners.com/python-on-the-web/how-to-access-various-web-services-in-python

#Import the modules
import requests
import json

# Get the feed (Call the webservice)
print("Calling webservice")
request = requests.get("https://route.ls.hereapi.com/routing/7.2/calculateroute.json?apiKey=LwyrCyWP_uZZQR1Qcf3Sw1OXVH0fj87TcwwRZODtVn4&waypoint0=geo!52.5,13.4&waypoint1=geo!52.5,13.45&mode=fastest;car;traffic:disabled")

# Convert it to a Python dictionary
print("Converting request to JSON")
dictionary = json.loads(request.text)
json = json.dumps(dictionary, indent = 4)

# write output to file
print("Writing JSON to file")
filename = "calculateroute.json"
file = open(filename, "w")
file.write(json)

print("Done")
