#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:35:01 2020

@author: jaco

This module is used to compare two stocks for all qualitative metrics

Free tool to find stock info:
https://eresearch.fidelity.com/eresearch/landing.jhtml
Try Yahoo Finance aswell

"""
import os
import stockvalidationsimple as svs

filename = "stockcomparisonresult.csv"

company_names = {
    "company_a": "John & Sons",
    "company_b": "Sam's Store"
}

company_a = {
    "pe_ratio": 5.7,
    "peg_ratio": 4.7,
    "ps_ratio": 4.7,
    "pb_ratio": 2.8,
    "dividend_yield": 4.9,
    "dividend_payout_ratio": 5.9,
    "return_on_assets": 2.5,
    "return_on_equity": 45.7,
    "profit_margin": 3.6,
    #"current_ratio": 6.9,
    #"quick_ratio": 2.7,
    "debt_to_equity_ratio": 4.8,
    #"interest_coverage_ratio": 5.8,
    "asset_turnover_ratio": 2.7,
    "inventory_turnover_ratio": 3.7
}

company_b = {
    "pe_ratio": 6.7,
    "peg_ratio": 3.7,
    "ps_ratio": 8.7,
    "pb_ratio": 2.8,
    "dividend_yield": 9.9,
    "dividend_payout_ratio": 6.9,
    "return_on_assets": 5.5,
    "return_on_equity": 4.7,
    "profit_margin": 6.6,
    "current_ratio": 2.9,
    "quick_ratio": 7.7,
    "debt_to_equity_ratio": 6.8,
    "interest_coverage_ratio": 3.8,
    "asset_turnover_ratio": 7.7,
    "inventory_turnover_ratio": 2.7
}

method_names = {
    "pe_ratio": "compare_pe_ratio",
    "peg_ratio": "compare_peg_ratio", # Also validate
    "ps_ratio": "compare_ps_ratio",
    "pb_ratio": "compare_pb_ratio",
    "dividend_yield": "compare_dividend_yield",
    "dividend_payout_ratio": "compare_dividend_payout_ratio",
    "return_on_assets": "compare_return_on_assets",
    "return_on_equity": "compare_return_on_equity",
    "profit_margin": "compare_profit_margin",
    #"current_ratio": "validate_current_ratio", #
    #"quick_ratio": "validate_quick_ratio", #
    "debt_to_equity_ratio": "compare_debt_to_equity_ratio",
    #"interest_coverage_ratio": "validate_interest_coverage_ratio", #
    "asset_turnover_ratio": "compare_asset_turnover_ratio",
    "inventory_turnover_ratio": "compare_inventory_turnover_ratio" 
}

company_rating = {
    "company_a": 0,
    "company_b": 0
}

def file_validation(filename):
    if os.path.exists(filename):
        os.remove(filename)

def write_to_file(data, filename):
    f = open(filename, "a")
    f.write(data)
    f.close()

def compare(company_a, company_b, filename):
    file_validation(filename)
    write_to_file("Metric," + \
            company_names["company_a"] + \
            "," + \
            company_names["company_b"] + \
            ",Best Performer" +\
                      "\n", filename)
    for key in company_a.keys():
        # Get values
        value_a = company_a[key]
        value_b = company_b[key]
        
        # Call valuation method
        method_to_call = getattr(svs, method_names[key])
        result = method_to_call(value_a, value_b)
        
        # Increase rating
        if result:
            company_rating["company_a"] = company_rating["company_a"] + 1
        else:
            company_rating["company_b"] = company_rating["company_b"] + 1
        
        # Determine best performer
        best_performer = company_names["company_a"] # Default
        if not result:
            best_performer = company_names["company_b"]
        
        # Write to file
        write_to_file(key + "," +\
                      str(value_a) + "," +\
                      str(value_b) + "," +\
                      best_performer +\
                      "\n", filename)
    
    # Determine best overall rating
    best_overall = company_names["company_a"]
    if company_rating["company_a"] > company_rating["company_b"]:
        best_overall = company_names["company_a"]
    elif company_rating["company_a"] < company_rating["company_b"]:
        best_overall = company_names["company_b"]
    else:
        best_overall = "Tie"
        
    write_to_file("\nBest Overall Rating," + best_overall, filename)
    
    print("Done")

# Main program starts
compare(company_a, company_b, filename)
