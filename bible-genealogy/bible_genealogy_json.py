#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat 25 July 2020

@author: Jaco Koekemoer

"""
import json

def retrieve_json(json_filename):
    print("Retrieving")
    #Read file
    try:
        f = open(json_filename, 'r')
        json_raw_data = f.read()
        json_data = json.loads(json_raw_data)
        return json_data
    except Exception:
        print("File could not be opened")


