#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:57:37 2020

@author: jaco
"""
import json


def main():
    #hebrew_letter_to_find = "ו"
    hebrew_letter_to_find = "ה"
    load_hebrew_names()    
    hebrew_letter_names = json.loads(open('hebrew-letter-names.json', 'r').read())
    
    # loop through 300 names
    hebrew_names = load_hebrew_names()
    for name in hebrew_names.keys():
        hebrew_name = hebrew_names[name]
        present = hebrew_letter_present(hebrew_name, hebrew_letter_to_find, hebrew_letter_names)
        if present == True:
            print(name)

def load_hebrew_names():
    filename = "hebrew-names-data.json"
    try:
        f = open(filename, 'r')
        json_raw_data = f.read()
        json_data = json.loads(json_raw_data)  
        return scrub_hebrew_names(json_data)
    except Exception as e:
        print(str(e))
        print("File could not be opened")

def scrub_hebrew_names(json_data):
    new_hebrew_names = {}
    for key in json_data.keys():
        new_hebrew_names[key] = json_data[key][1]
    return new_hebrew_names

# Process geomatria
def hebrew_letter_present(hebrew_name, hebrew_letter_to_find, hebrew_letter_names):
    letter_sum = 0
    for letter in hebrew_name:
        if letter not in hebrew_letter_names.keys():
            continue
        if letter == hebrew_letter_to_find:
            return True
    return False

main()