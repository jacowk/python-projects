#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:50:04 2020

@author: jaco
"""
import json

json_data = ""

def descr_introduction(json_data):
    return json_data["descr_introduction"]

def descr_ratio_categories(json_data):
    return json_data["descr_ratio_categories"]

def descr_notes(json_data):
    return json_data["descr_notes"]

# Valuation: Price To Earnings Ratio
def descr_pe_ratio(json_data):
    return json_data["descr_pe_ratio"]

# Valuation: Price To Earnings Growth / PEG Ratio
def descr_peg_ratio(json_data):
    return json_data["descr_peg_ratio"]

# Valuation: Price To Sales (P/S)
def descr_ps_ratio(json_data):
    return json_data["descr_ps_ratio"]

# Valuation: Price To Book (P/B)
def descr_pb_ratio(json_data):
    return json_data["descr_pb_ratio"]

# Valuation: Dividend Yield
def descr_dividend_yield(json_data):
    return json_data["descr_dividend_yield"]

# Valuation: Dividend Payout Ratio
def descr_dividend_payout_ratio(json_data):
    return json_data["descr_dividend_payout_ratio"]

# Profitability: Return on Assets
def descr_return_on_assets(json_data):
    return json_data["descr_return_on_assets"]

# Profitability: Return on Equity
def descr_return_on_equity(json_data):
    return json_data["descr_return_on_equity"]

# Profitability: Profit Margin
def descr_profit_margin(json_data):
    return json_data["descr_profit_margin"]

# Liquidity: Current Ratio
def descr_current_ratio(json_data):
    return json_data["descr_current_ratio"]

# Liquidity: Quick Ratio (ACID Test)
def descr_quick_ratio(json_data):
    return json_data["descr_quick_ratio"]

# Debt: Debt to Equity
def descr_debt_to_equity_ratio(json_data):
    return json_data["descr_debt_to_equity_ratio"]

# Debt: Interest Coverage Ratio
def descr_interest_coverage_ratio(json_data):
    return json_data["descr_interest_coverage_ratio"]

# Efficiency: Asset Turnover Ratio
def descr_asset_turnover_ratio(json_data):
    return json_data["descr_asset_turnover_ratio"]

# Efficiency: Inventory Turnover Ratio
def descr_inventory_turnover_ratio(json_data):
    return json_data["descr_inventory_turnover_ratio"]
