#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:11:45 2020

@author: jaco
"""
import csv

def add_semi_colons(data):
    new_data = ""
    for x in data:
        if x == ',':
            new_data += "\'"
            new_data += ","
            new_data += "\'"
        else:
            new_data += x
    return new_data

def generate_variable_statements(columns):
    cnt = 0
    for item in columns:
        print("%s = row[%d]" % (item, cnt))
        cnt += 1

def generate_print_statements(columns):
    for item in columns:
        print("print(\'%s: \', %s)" % (item, item))

def scrub_data(data):
    data = data.lower()
    data = data.strip()
    return data

def replace_commas(data):
    return data.replace(',', '.')

def prep_stats(key, dict_statistics):
    if key in dict_statistics.keys():
        dict_statistics[key] = dict_statistics[key] + 1
    else:
        dict_statistics[key] = 1
    return dict_statistics

def harvest_dict_values(key, value, harvest_dict):
    if key not in harvest_dict.keys():
        harvest_dict[key] = value
    return harvest_dict
    
def output_sorted_dict(name, dict_statistics):
    print(name)
    for key in sorted(dict_statistics.keys()):
        print(key, "::", dict_statistics[key])

# Sort offences by value, descending, then return only the top no of offences
def output_sorted_pd_cd(name, dict_statistics, pd_dict, top):
    print(name)
    cnt = 1
    # Sort by values
    sorted_dict_statistics = sorted(dict_statistics.items(), key=lambda kv: kv[1],reverse=True)
    for key, value in sorted_dict_statistics:
        print(key, "::", pd_dict[key], "::",  dict_statistics[key])
        if cnt == top:
            break
        cnt += 1

def get_year(full_date): # mm/dd/yyyy
    date_list = full_date.split("/")
    return date_list[2]

def load_dict_from_file(filename):
    dict_data = {}
    with open(filename, newline = '') as csvfile:
        datareader = csv.reader(csvfile, delimiter = ',')
        for row in datareader:
            pd_cd = row[0]
            pd_desc = row[1]
            dict_data[pd_cd] = pd_desc
    return dict_data
            
        
    
