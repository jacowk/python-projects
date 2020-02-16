#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:11:45 2020

@author: jaco
"""

def generate_print_statements(columns):
    for item in columns:
        print("print(\'%s: \', %s)" % (item, item))
        
def generate_variable_statements(columns):
    cnt = 0
    for item in columns:
        print("%s = row[%d]" % (item, cnt))
        cnt += 1

def scrub_data(data):
    data = data.lower()
    data = data.strip()
    return data

def prep_stats(key, dict_statistics):
    if key in dict_statistics.keys():
        dict_statistics[key] = dict_statistics[key] + 1
    else:
        dict_statistics[key] = 1
    return dict_statistics

def output_sorted_dict(name, dict_statistics):
    print(name)
    for key in sorted(dict_statistics.keys()):
        print(key, "::", dict_statistics[key])