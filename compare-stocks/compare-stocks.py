#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:56:00 2020

@author: jaco

Configuration file contents:
    

    
"""
import pandas as pd


def compare_stocks():
    # Read compare configuration file
    compare_config_data = read_config_file("compare-stocks-config.csv")
    compare_config_map = load_compare_config_map(compare_config_data)
    
    # Read validation configuration file
    validate_config_data = read_config_file("validate-stocks-config.csv")
    validate_config_map = load_validate_config_map(validate_config_data)
    
    # Read stock comparison file containing 2 stocks
    compare_stocks_data = read_config_file("compare-stocks.csv")
    
    # Compare stocks based on config file rules
    ranking_map = {"CompanyA": 0, "CompanyB": 0}
    ranking_map = compare(compare_stocks_data, compare_config_map, ranking_map)
    validate(compare_stocks_data, validate_config_map, ranking_map)
    
    # Write results to file
    output_ranking_result(ranking_map)

def read_config_file(filename):
    return pd.read_csv(filename)    

def write_to_file(data, filename):
    f = open(filename, "a")
    f.write(data)
    f.close()
    
def load_compare_config_map(compare_config_data):
    compare_config_map = {}
    for index, row in compare_config_data.iterrows():
        name = row['Name']
        validation_symbol = row['Validation Symbol']
        compare_config_map[name] = validation_symbol
    return compare_config_map

def load_validate_config_map(validate_config_data):
    validate_config_map = {}
    for index, row in validate_config_data.iterrows():
        name = row['Name']
        validation_symbol = row['Validation Symbol']
        validation_value = row['Validation Value']
        validate_config_map[name] = [validation_symbol, validation_value]
    return validate_config_map

def compare(compare_stocks_data, compare_config_map, ranking_map):
    print(heading("Comparing Ratios"))
    print("Ratio, CompanyA, Symbol, CompanyB, Check")
    for index, row in compare_stocks_data.iterrows():
        ratio = row['Ratio']
        company_a = row['CompanyA']
        company_b = row['CompanyB']
        symbol = ""
        try:
            symbol = compare_config_map[ratio]
        except:
            continue
        value1 = company_a
        symbol = compare_config_map[ratio]
        value2 = company_b
        
        result = False
        if value1 == value2:
            ranking_map['CompanyA']  = ranking_map['CompanyA'] + 1
            ranking_map['CompanyB']  = ranking_map['CompanyB'] + 1
        else:
            if symbol == ">":
                if value1 > value2:
                    result = True
                    ranking_map['CompanyA']  = ranking_map['CompanyA'] + 1
                else:
                    ranking_map['CompanyB']  = ranking_map['CompanyB'] + 1
            elif symbol == "<":
                if value1 < value2:
                    result = True
                    ranking_map['CompanyA']  = ranking_map['CompanyA'] + 1
                else:
                    ranking_map['CompanyB']  = ranking_map['CompanyB'] + 1
            
        if result == True:
            output = "{},{},{},{},(Check)".format(ratio, company_a, symbol, company_b)
        else:
            output = "{},{},{},{},".format(ratio, company_a, symbol, company_b)
        print(output)
    return ranking_map

def validate(compare_stocks_data, validate_config_map, ranking_map):
    print(heading("Validating against single value"))
    print("Company, Ratio, Value, Symbol, Validation Value, Check")
    for index, row in compare_stocks_data.iterrows():
        ratio = row['Ratio']
        company_a = row['CompanyA']
        company_b = row['CompanyB']
        symbol = ""
        try:
            symbol = validate_config_map[ratio]
        except:
            continue
        value1 = company_a
        value2 = company_b
        symbol = validate_config_map[ratio][0]
        validation_value = validate_config_map[ratio][1]
        
        compare_company("CompanyA", ratio, value1, symbol, validation_value, ranking_map)
        compare_company("CompanyB", ratio, value2, symbol, validation_value, ranking_map)
        
    return ranking_map

def compare_company(company, ratio, value, symbol, validation_value, ranking_map):
    result = False
    if symbol == ">":
        if value > validation_value:
            result = True
            ranking_map[company] = ranking_map[company] + 1
    elif symbol == "<":
        if value < validation_value:
            result = True
            ranking_map[company] = ranking_map[company] + 1
    
    # Output
    # Company, Ratio, Value, Symbol, Validation Value, Check
    if result == True:
        output = "{},{},{},{},{},(Check)".format(company, ratio, value, symbol, validation_value)
    else:
        output = "{},{},{},{},{},".format(company, ratio, value, symbol, validation_value)
    print(output)
    return ranking_map
    
def track_ranking(ranking_map):
    print("CompanyA: {}, CompanyB: {}".format(ranking_map['CompanyA'], ranking_map['CompanyB']))

# TODO Load and include actual names of companies in the final result
def output_ranking_result(ranking_map):
    print(heading("Best Performing Company"))
    track_ranking(ranking_map)
    if (ranking_map['CompanyA'] == ranking_map['CompanyB']):
        print("Tied")
    elif (ranking_map['CompanyA'] > ranking_map['CompanyB']):
        print("CompanyA")
    else:
        print("CompanyB")

def heading(value):
    decoration = "=" * 5
    return "\n" + decoration + value + decoration

compare_stocks()


#Phonetics
#Numerics
#Pictographs
#Ancient Hebrew and Aramaic
