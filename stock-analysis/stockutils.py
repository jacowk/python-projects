#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:18:30 2020

@author: jaco
"""
import json

def retrieve_json():
    #Read file
    json_filename = "stockinfo.json"
    try:
        f = open(json_filename, 'r')
        json_raw_data = f.read()
        return json.loads(json_raw_data)   
    except Exception as e:
        print("File could not be opened: {:s}".format(str(e)))

def output_pipe_delimited_string(value):
    value_list = value.split("|")
    for value_item in value_list:
        print(value_item)
