#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:43:13 2020

@author: jaco

These methods returns true or false. If the 1st ratio is better, True is
returned, else False is returned.

The following method does not compare 2 stocks, but validates single values:
-validate_dividend_payout_ratio
-validate_current_ratio
-validate_quick_ratio
-validate_interest_coverage_ratio

"""

What if the values are equal. Rather 
Return 1 if primary condition met
Return -1 if primary condition not met
Return 0 if equal

# Valuation: Price To Earnings Ratio
def compare_pe_ratio(pe_ratio1, pe_ratio2):
    if pe_ratio1 < pe_ratio2:
        return True
    else:
        return False

# Valuation: Price To Earnings Growth
def validate_peg_ratio(peg_ratio):
    if peg_ratio < 1.0:
        return True
    else:
        return False

def compare_peg_ratio(peg_ratio1, peg_ratio2):
    if peg_ratio1 < peg_ratio2:
        return True
    else:
        return False

# Valuation: Price To Sales (P/S)
def compare_ps_ratio(ps_ratio1, ps_ratio2):
    if ps_ratio1 < ps_ratio2:
        return True
    else:
        return False

# Valuation: Price To Book (P/B)
def compare_pb_ratio(pb_ratio1, pb_ratio2):
    if pb_ratio1 < pb_ratio2:
        return True
    else:
        return False

# Valuation: Dividend Yield
def compare_dividend_yield(dividend_yield1, dividend_yield2):
    if dividend_yield1 > dividend_yield2:
        return True
    else:
        return False

# Valuation: Dividend Payout Ratio
def validate_dividend_payout_ratio(dividend_payout_ratio):
    if dividend_payout_ratio < 50:
        return True
    elif dividend_payout_ratio > 50 and dividend_payout_ratio < 60:
        return True
    elif dividend_payout_ratio > 60 and dividend_payout_ratio < 70:
        return True
    else:
        return False
    
def compare_dividend_payout_ratio(dividend_payout_ratio1, dividend_payout_ratio2):
    if dividend_payout_ratio1 < dividend_payout_ratio2:
        return True
    else:
        return False

# Profitability: Return on Assets (ROA)
def compare_return_on_assets(return_on_assets1, return_on_assets2):
    if return_on_assets1 > return_on_assets2:
        return True
    else:
        return False

# Profitability: Return on Equity (ROE)
def compare_return_on_equity(return_on_equity1, return_on_equity2):
    if return_on_equity1 > return_on_equity2:
        return True
    else:
        return False
    
# Profitability: Profit Margin
def compare_profit_margin(profit_margin1, profit_margin2):
    if profit_margin1 > profit_margin2:
        return True
    else:
        return False

# Liquidity: Current Ratio
def validate_current_ratio(current_ratio):
    if current_ratio > 1.0:
        return True
    else:
        return False

# Liquidity: Quick Ratio (ACID Test)
def validate_quick_ratio(quick_ratio):
    if quick_ratio > 1.0:
        return True
    else:
        return False

# Debt: Debt to Equity Ratio
def compare_debt_to_equity_ratio(debt_to_equity_ratio1, debt_to_equity_ratio2):
    if debt_to_equity_ratio1 < debt_to_equity_ratio2:
        return True
    else:
        return False

# Debt: Interest Coverage Ratio
def validate_interest_coverage_ratio(interest_coverage_ratio):
    if interest_coverage_ratio > 1.0:
        return True
    else:
        return False

# Efficiency: Asset Turnover Ratio
def compare_asset_turnover_ratio(asset_turnover_ratio1, asset_turnover_ratio2):
    if asset_turnover_ratio1 > asset_turnover_ratio2:
        return True
    else:
        return False

# Efficiency: Inventory Turnover Ratio
def compare_inventory_turnover_ratio(inventory_turnover_ratio1, inventory_turnover_ratio2):
    if inventory_turnover_ratio1 > inventory_turnover_ratio2:
        return True
    else:
        return False
