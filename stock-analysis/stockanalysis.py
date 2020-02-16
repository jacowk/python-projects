#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:48:54 2020

@author: jaco
"""
import stockcalc as sc
import stockvalidation as sv
import stockdescription as sd
import stockutils as su

def intro():
    json_data = su.retrieve_json()
    su.output_pipe_delimited_string(sd.descr_introduction(json_data))
    su.output_pipe_delimited_string(sd.descr_ratio_categories(json_data))
    su.output_pipe_delimited_string(sd.descr_notes(json_data))

def analyse_pe_ratio():
    json_data = su.retrieve_json()
    price_per_share = input("Enter price per share:")
    earnings_per_share = input("Enter price per share:")
    
    # Calc PE Ratio
    pe_ratio = sc.calc_pe_ratio(float(price_per_share), float(earnings_per_share))
    
    # Output
    print("P/E Ratio: {:f}".format(pe_ratio))
    su.output_pipe_delimited_string(sd.descr_pe_ratio(json_data))
    print(sv.validate_pe_ratio(pe_ratio))
    
def analyse_peg_ratio():
    json_data = su.retrieve_json()
    pe_ratio = input("Enter P/E Ratio:")
    future_earnings_per_share = input("Enter estimated future earnings per share:")
    
    # Calc PE Ratio
    peg_ratio = sc.calc_peg_ratio(float(pe_ratio), float(future_earnings_per_share))
    
    # Output
    print("PEG Ratio: {:f}".format(peg_ratio))
    su.output_pipe_delimited_string(sd.descr_peg_ratio(json_data))
    print(sv.validate_peg_ratio(peg_ratio))
    
def analyse_ps_ratio():
    json_data = su.retrieve_json()
    
    price_per_share = input("Enter Price per Share:")
    annual_sales_per_share = input("Enter Annual Sales per Share:")
    
    # Calc PE Ratio
    ps_ratio = sc.calc_ps_ratio(float(price_per_share), float(annual_sales_per_share))
    
    # Output
    print("P/S Ratio: {:f}".format(ps_ratio))
    su.output_pipe_delimited_string(sd.descr_ps_ratio(json_data))
    print(sv.validate_ps_ratio(ps_ratio))

def analyse_pb_ratio():
    json_data = su.retrieve_json()

    price_per_share = input("Enter Price per Share:")
    book_value = input("Enter company book value:")
    total_number_of_shares = input("Enter total number of shares:")

    # Calc PB Ratio
    pb_ratio = sc.calc_pb_ratio(float(price_per_share), float(book_value), float(total_number_of_shares))
    
    # Output
    print("P/B Ratio: {:f}".format(pb_ratio))
    su.output_pipe_delimited_string(sd.descr_pb_ratio(json_data))
    print(sv.validate_pb_ratio(pb_ratio))

# Valuation: Dividend Yield
def analyse_dividend_yield():
    json_data = su.retrieve_json()

    dividend_per_share = input("Enter Dividend per Share:")
    price_per_share = input("Enter Price per Share:")

    # Calc Dividend Yield
    dividend_yield = sc.calc_dividend_yield(float(dividend_per_share), float(price_per_share))
    
    # Output
    print("Dividend Yield: {:f}".format(dividend_yield))
    su.output_pipe_delimited_string(sd.descr_dividend_yield(json_data))
    print(sv.validate_dividend_yield(dividend_yield))

# Valuation: Dividend Payout Ratio
def analyse_dividend_payout_ratio():
    json_data = su.retrieve_json()

    dividend = input("Enter Dividend:")
    net_income = input("Enter Net Income:")

    # Calc Dividend Payout Ratio
    dividend_payout_ratio = sc.calc_dividend_payout_ratio(float(dividend), float(net_income))
    
    # Output
    print("Dividend Payout Ratio: {:f}".format(dividend_payout_ratio))
    su.output_pipe_delimited_string(sd.descr_dividend_payout_ratio(json_data))
    print(sv.validate_dividend_payout_ratio(dividend_payout_ratio))

# Profitability: Return on Assets (ROA)
def analyse_return_on_assets():
    json_data = su.retrieve_json()

    net_income = input("Enter Net Income:")
    average_total_assets = input("Enter Average Total Assets:")

    # Calc Return on Assets
    return_on_assets = sc.calc_return_on_assets(float(net_income), float(average_total_assets))
    
    # Output
    print("Return on Assets (ROA): {:f}".format(return_on_assets))
    su.output_pipe_delimited_string(sd.descr_return_on_assets(json_data))
    print(sv.validate_return_on_assets(return_on_assets))

# Profitability: Return on Equity (ROE)
def analyse_return_on_equity():
    json_data = su.retrieve_json()

    net_income = input("Enter Net Income:")
    average_stockholder_equity = input("Enter Average Stockholder Equity:")

    # Calc Return on Equity
    return_on_equity = sc.calc_return_on_equity(float(net_income), float(average_stockholder_equity))
    
    # Output
    print("Return on Equity (ROE): {:f}".format(return_on_equity))
    su.output_pipe_delimited_string(sd.descr_return_on_equity(json_data))
    print(sv.validate_return_on_equity(return_on_equity))

# Profitability: Profit Margin
def analyse_profit_margin():
    json_data = su.retrieve_json()

    net_income = input("Enter Net Income:")
    sales = input("Enter Sales:")

    # Calc Profit Margin
    profit_margin = sc.calc_profit_margin(float(net_income), float(sales))
    
    # Output
    print("Profit Margin: {:f}".format(profit_margin))
    su.output_pipe_delimited_string(sd.descr_profit_margin(json_data))
    print(sv.validate_profit_margin(profit_margin))

# Liquidity: Current Ratio
def analyse_current_ratio():
    json_data = su.retrieve_json()

    current_assets = input("Enter Current Assets:")
    current_liabilities = input("Enter Current Liabilities:")
    
    # Calc Current Ratio
    current_ratio = sc.calc_current_ratio(float(current_assets), float(current_liabilities))
    
    # Output
    print("Current Ratio: {:f}".format(current_ratio))
    su.output_pipe_delimited_string(sd.descr_current_ratio(json_data))
    print(sv.validate_current_ratio(current_ratio))

# Liquidity: Quick Ratio (ACID Test)
def analyse_quick_ratio():
    json_data = su.retrieve_json()

    current_assets = input("Enter Current Assets:")
    inventory = input("Enter Inventory:")
    current_liabilities = input("Enter Current Liabilities:")
    
    # Calc Quick Ratio
    quick_ratio = sc.calc_quick_ratio(float(current_assets), float(inventory), float(current_liabilities))
    
    # Output
    print("Quick Ratio (Acid Test Ratio): {:f}".format(quick_ratio))
    su.output_pipe_delimited_string(sd.descr_quick_ratio(json_data))
    print(sv.validate_quick_ratio(quick_ratio))

# Debt: Debt to Equity
def analyse_debt_to_equity_ratio():
    json_data = su.retrieve_json()

    total_liabilities = input("Enter Current Assets:")
    total_shareholder_equity = input("Enter Current Liabilities:")
    
    # Calc Debt to Equity Ratio
    debt_to_equity_ratio = sc.calc_debt_to_equity_ratio(float(total_liabilities), 
                                                        float(total_shareholder_equity))
    
    # Output
    print("Debt to Equity Ratio: {:f}".format(debt_to_equity_ratio))
    su.output_pipe_delimited_string(sd.descr_debt_to_equity_ratio(json_data))
    print(sv.validate_debt_to_equity_ratio(debt_to_equity_ratio))

# Debt: Interest Coverage Ratio
def analyse_interest_coverage_ratio():
    json_data = su.retrieve_json()

    ebit = input("Enter EBIT (Earnings Before Interest and Taxes):")
    interest_expense = input("Enter Interest Expense:")
    
    # Calc Interest Coverage Ratio
    interest_coverage_ratio = sc.calc_interest_coverage_ratio(float(ebit), float(interest_expense))
    
    # Output
    print("Interest Coverage Ratio: {:f}".format(interest_coverage_ratio))
    su.output_pipe_delimited_string(sd.descr_interest_coverage_ratio(json_data))
    print(sv.validate_interest_coverage_ratio(interest_coverage_ratio))

# Efficiency: Asset Turnover Ratio
def analyse_asset_turnover_ratio():
    json_data = su.retrieve_json()

    sales = input("Enter Sales:")
    average_total_assets = input("Enter Average Total Assets:")
    
    # Calc Asset Turnover Ratio
    asset_turnover_ratio = sc.calc_asset_turnover_ratio(float(sales), float(average_total_assets))
    
    # Output
    print("Asset Turnover Ratio: {:f}".format(asset_turnover_ratio))
    su.output_pipe_delimited_string(sd.descr_asset_turnover_ratio(json_data))
    print(sv.validate_asset_turnover_ratio(asset_turnover_ratio))

# Efficiency: Inventory Turnover Ratio
def analyse_inventory_turnover_ratio():
    json_data = su.retrieve_json()
    
    costs_of_goods_sold = input("Enter Costs of Goods Sold:")
    average_inventory = input("Enter Average Inventory:")
    
    # Calc Inventory Turnover Ratio
    inventory_turnover_ratio = sc.calc_inventory_turnover_ratio(float(costs_of_goods_sold), float(average_inventory))
    
    # Output
    print("Inventory Turnover Ratio: {:f}".format(inventory_turnover_ratio))
    su.output_pipe_delimited_string(sd.descr_inventory_turnover_ratio(json_data))
    print(sv.validate_inventory_turnover_ratio(inventory_turnover_ratio))
