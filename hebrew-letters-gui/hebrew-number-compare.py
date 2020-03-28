#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:02:20 2020

@author: jaco
"""
import json


def main():
    load_hebrew_names()    
    hebrew_numbers = json.loads(open('hebrew-numbers.json', 'r').read())
    hebrew_letter_names = json.loads(open('hebrew-letter-names.json', 'r').read())
    
    totals_dict = {} #Total, list of names
    
    # loop through 300 names
    hebrew_names = load_hebrew_names()
    for name in hebrew_names.keys():
        hebrew_name = hebrew_names[name]
        letter_sum = process_geomatria(hebrew_name, hebrew_numbers, hebrew_letter_names)
        if letter_sum in totals_dict.keys():
            name_list = totals_dict.get(letter_sum)
            name_list.append(name)
        else:
            totals_dict[letter_sum] = [name]
    for key in sorted(totals_dict.keys()):
        print(key, totals_dict[key])
    print("Total entries: " + str(len(totals_dict)))

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
def process_geomatria(hebrew_name, hebrew_numbers, hebrew_letter_names):
    letter_sum = 0
    for letter in hebrew_name:
        if letter not in hebrew_letter_names.keys():
            continue
        letter_name = hebrew_letter_names[letter]
        number = hebrew_numbers[letter_name]
        letter_sum += int(number)
    return letter_sum

main()