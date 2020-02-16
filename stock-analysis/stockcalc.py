#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:49:33 2020

@author: jaco
"""

# Valuation: Price To Earnings Ratio
def calc_pe_ratio(price_per_share, earnings_per_share):
    return price_per_share / earnings_per_share

# Valuation: Price To Earnings Growth / PEG Ratio
def calc_peg_ratio(pe_ratio, estimate_earnings_per_share):
    return pe_ratio / estimate_earnings_per_share

# Valuation: Price To Sales (P/S)
def calc_ps_ratio(price_per_share, annual_sales_per_share):
    return price_per_share / annual_sales_per_share

# Valuation: Price To Book (P/B)
def calc_pb_ratio(price_per_share, book_value, total_number_of_shares):
    book_value_per_share = calc_book_value_per_share(book_value, total_number_of_shares)
    return price_per_share / book_value_per_share

def calc_book_value_per_share(book_value, total_number_of_shares):
    return book_value / total_number_of_shares

# Valuation: Dividend Yield
def calc_dividend_yield(dividend_per_share, price_per_share):
    return dividend_per_share / price_per_share

# Valuation: Dividend Payout Ratio
def calc_dividend_payout_ratio(dividend, net_income):
    return dividend / net_income

# Profitability: Return on Assets (ROA)
def calc_return_on_assets(net_income, average_total_assets):
    return net_income / average_total_assets

# Profitability: Return on Equity (ROE)
def calc_return_on_equity(net_income, average_stockholder_equity):
    return net_income / average_stockholder_equity

# Profitability: Profit Margin
def calc_profit_margin(net_income, sales):
    return net_income / sales

# Liquidity: Current Ratio
def calc_current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

# Liquidity: Quick Ratio (ACID Test)
def calc_quick_ratio(current_assets, inventory, current_liabilities):
    return (current_assets - inventory) / current_liabilities

# Debt: Debt to Equity
def calc_debt_to_equity_ratio(total_liabilities, total_shareholder_equity):
    return total_liabilities / total_shareholder_equity

# Debt: Interest Coverage Ratio
def calc_interest_coverage_ratio(ebit, interest_expense):
    return ebit / interest_expense

# Efficiency: Asset Turnover Ratio
def calc_asset_turnover_ratio(sales, average_total_assets):
    return sales / average_total_assets

# Efficiency: Inventory Turnover Ratio
def calc_inventory_turnover_ratio(costs_of_goods_sold, average_inventory):
    return costs_of_goods_sold / average_inventory
