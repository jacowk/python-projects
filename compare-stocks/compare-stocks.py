#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:56:00 2020

@author: jaco

Configuration file contents:
    

    
"""

def compare_stocks():
    print("Hello world")
    # Read compare configuration file
    compare_config_filename = "compare-stocks-config.csv"
    compare_config_data = read_config_file(compare_config_filename)
    print("\nCompare Config Data")
    print(compare_config_data)
    
    # Read validation configuration file
    validate_config_filename = "validate-stocks-config.csv"
    validate_config_data = read_config_file(validate_config_filename)
    print("\nValidate Config Data")
    print(validate_config_data)
    
    # Read stock comparison file containing 2 stocks
    compare_stocks_filename = "compare-stocks.csv"
    compare_stocks_data = read_config_file(compare_stocks_filename)
    print("\nStock Data")
    print(compare_stocks_data)
    
    # Compare stocks based on config file rules
    
    # Write results to file

def read_config_file(filename):
    f = open(filename, "r")
    data = f.read()
    return data
    

def write_to_file(data, filename):
    f = open(filename, "a")
    f.write(data)
    f.close()

compare_stocks()
