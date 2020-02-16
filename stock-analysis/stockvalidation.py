#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:49:48 2020

@author: jaco
"""

# Valuation: Price To Earnings Ratio
def validate_pe_ratio(pe_ratio):
    return "Validation Result:\nLower PE ratios are better.\n\
Compare P/E ratio {:f} with the P/E ratio of another company in the same industry.\n"

def compare_pe_ratio(pe_ratio1, pe_ratio2):
    output = "Validation Result:\nLower PE ratios are better.\n"
    if pe_ratio1 > pe_ratio2:
        return output + "PE ratio {:f} is less favourable than PE ratio \
{:f}".format(pe_ratio1, pe_ratio2)
    elif pe_ratio1 < pe_ratio2:
        return output + "PE ratio {:f} is more favourable than PE ratio \
{:f}".format(pe_ratio1, pe_ratio2)
    else:
        return output + "Equal PE ratios {:f} and {:f}, so neither is more \
favourable".format(pe_ratio1, pe_ratio2)

# Valuation: Price To Earnings Growth
def validate_peg_ratio(peg_ratio):
    output = "Validation Result:\nPEG ratios below 1.0 are better.\n"
    if peg_ratio < 1.0:
        return output + "Favourable PEG ratio - {:f}".format(peg_ratio)
    else:
        return output + "Unfavourable PEG ratio - {:f}".format(peg_ratio)

def compare_peg_ratio(peg_ratio1, peg_ratio2):
    output = "Validation Result:\nLower PEG ratios are better.\n"
    if peg_ratio1 > peg_ratio2:
        return output + "PEG ratio {:f} is less favourable than PEG ratio \
{:f}".format(peg_ratio1, peg_ratio2)
    elif peg_ratio1 < peg_ratio2:
        return output + "PEG ratio {:f} is more favourable than PEG ratio \
{:f}".format(peg_ratio1, peg_ratio2)
    else:
        return output + "Equal PEG ratios {:f} and {:f}, so neither is more \
favourable".format(peg_ratio1, peg_ratio2)

# Valuation: Price To Sales (P/S)
def validate_ps_ratio(ps_ratio):
    return "Validation Result:\nLower P/S ratio is better.\n\
Compare P/S ratio {:f} with the P/S ratio of another company in the same \
industry.\n".format(ps_ratio)

def compare_ps_ratio(ps_ratio1, ps_ratio2):
    output = "Validation Result:\nLower P/S ratios are better.\n"
    if ps_ratio1 > ps_ratio2:
        return output + "P/S ratio {:f} is less favourable than P/S ratio \
{:f}".format(ps_ratio1, ps_ratio2)
    elif ps_ratio1 < ps_ratio2:
        return output + "P/S ratio {:f} is more favourable than P/S ratio \
{:f}".format(ps_ratio1, ps_ratio2)
    else:
        return output + "Equal P/S ratios {:f} and {:f}, so neither is more \
favourable".format(ps_ratio1, ps_ratio2)

# Valuation: Price To Book (P/B)
def validate_pb_ratio(pb_ratio):
    return "Validation Result:\nLower P/B ratio is better.\n\
Compare P/B ratio {:f} with the P/B ratio of another company in the same \
industry.\n".format(pb_ratio)

def compare_pb_ratio(pb_ratio1, pb_ratio2):
    output = "Validation Result:\nLower P/B ratios are better.\n"
    if pb_ratio1 > pb_ratio2:
        return output + "P/B ratio {:f} is less favourable than P/S ratio \
{:f}".format(pb_ratio1, pb_ratio2)
    elif pb_ratio1 < pb_ratio2:
        return output + "P/B ratio {:f} is more favourable than P/S ratio \
{:f}".format(pb_ratio1, pb_ratio2)
    else:
        return output + "Equal P/B ratios {:f} and {:f}, so neither is more \
favourable".format(pb_ratio1, pb_ratio2)

# Valuation: Dividend Yield
def validate_dividend_yield(dividend_yield):
    return "Validation Result:\nHigher Dividend Yields are better\n\
Compare Dividend Yield {:f} with the Dividend Yield of another company in the \
same industry.\n".format(dividend_yield)

def compare_dividend_yield(dividend_yield1, dividend_yield2):
    output = "Validation Result:\nThe higher Dividend Yield is better.\n"
    if dividend_yield1 > dividend_yield2:
        return output + "Dividend Yield {:f} is more favourable than Dividend \
Yield {:f}".format(dividend_yield1, dividend_yield2)
    elif dividend_yield1 < dividend_yield2:
        return output + "Dividend Yield {:f} is less favourable than Dividend \
Yield {:f}".format(dividend_yield1, dividend_yield2)
    else:
        return output + "Equal Dividend Yields {:f} and {:f}, so neither is \
more favourable".format(dividend_yield1, dividend_yield2)
    return output

# Valuation: Dividend Payout Ratio
def validate_dividend_payout_ratio(dividend_payout_ratio):
    output = "Validation Result:\nLower Dividend Payout Ratio is better.\n"
    if dividend_payout_ratio < 50:
        return output + "Ratio {} is excellent\n\
The company should be able to maintain dividend payouts".format(dividend_payout_ratio)
    elif dividend_payout_ratio > 50 and dividend_payout_ratio < 60:
        return output + "Ratio {} is good (<50 is excellent)\
The company should be able to maintain dividend payouts\n".format(dividend_payout_ratio)
    elif dividend_payout_ratio > 60 and dividend_payout_ratio < 70:
        return output + "Ratio {} is still OK (<50 is excellent)\
The company should be able to maintain dividend payouts\n".format(dividend_payout_ratio)
    else:
        return output + "Ratio {} is not good. Be cautious. The company might \
not be able to maintain dividend payouts\n".format(dividend_payout_ratio)
    

def compare_dividend_payout_ratio(dividend_payout_ratio1, dividend_payout_ratio2):
    output = "Validation Result:\nLower Dividend Payout Ratios are better.\n"
    if dividend_payout_ratio1 > dividend_payout_ratio2:
        return output + "Dividend Payout Ratio {:f} is less favourable than \
Dividend Payout Ratio {:f}".format(dividend_payout_ratio1, dividend_payout_ratio2)
    elif dividend_payout_ratio1 < dividend_payout_ratio2:
        return output + "Dividend Payout Ratio {:f} is more favourable than \
Dividend Payout Ratio {:f}".format(dividend_payout_ratio1, dividend_payout_ratio2)
    else:
        return output + "Equal Dividend Payout Ratio {:f} and {:f}, so neither \
is more favourable".format(dividend_payout_ratio1, dividend_payout_ratio2)
    return 0

# Profitability: Return on Assets (ROA)
def validate_return_on_assets(return_on_assets):
    return "Validation Result:\nHigher ROA is better.\n\
Compare ROA {:f} with the ROA of another company in the same industry.\n".format(return_on_assets)

def compare_return_on_assets(return_on_assets1, return_on_assets2):
    output = "Validation Result:\nThe higher ROA is better.\n"
    if return_on_assets1 > return_on_assets2:
        return output + "ROA {:f} is more favourable than ROA \
{:f}. The company generates more profits using it's \
assets".format(return_on_assets1, return_on_assets2)
    elif return_on_assets1 < return_on_assets2:
        return output + "ROA {:f} is less favourable than ROA \
{:f}. The company generates less profits using it's \
assets".format(return_on_assets1, return_on_assets2)
    else:
        return output + "Equal ROAs {:f} and {:f}, so neither is \
more favourable".format(return_on_assets1, return_on_assets2)

# Profitability: Return on Equity (ROE)
def validate_return_on_equity(return_on_equity):
    return "Validation Result:\nHigher ROE is better.\n\
Compare ROE {:f} with the ROE of another company in the same industry.\n".format(return_on_equity)

def compare_return_on_equity(return_on_equity1, return_on_equity2):
    output = "Validation Result:\nThe higher ROE is better.\n"
    if return_on_equity1 > return_on_equity2:
        return output + "ROE {:f} is more favourable than ROE \
{:f}. The company generates more profits using for every $1 of equity\
".format(return_on_equity1, return_on_equity2)
    elif return_on_equity1 < return_on_equity2:
        return output + "ROE {:f} is less favourable than ROE \
{:f}. The company generates less profits using for every $1 of equity\
".format(return_on_equity1, return_on_equity2)
    else:
        return output + "Equal ROEs {:f} and {:f}, so neither is \
more favourable".format(return_on_equity1, return_on_equity2)
    
# Profitability: Profit Margin
def validate_profit_margin(profit_margin):
    return "Validation Result:\nHigher Profit Margin is better.\n\
Compare the Profit Margin {:f} with the Profit Margin of another company in the \
same industry.\n".format(profit_margin)

def compare_profit_margin(profit_margin1, profit_margin2):
    output = "Validation Result:\nThe higher Profit Margin is better.\n"
    if profit_margin1 > profit_margin2:
        return output + "Profit Margin {:f} is more favourable than Profit Margin \
{:f}.".format(profit_margin1, profit_margin2)
    elif profit_margin1 < profit_margin2:
        return output + "Profit Margin {:f} is less favourable than Profit Margin \
{:f}.".format(profit_margin1, profit_margin2)
    else:
        return output + "Equal Profit Margin {:f} and {:f}, so neither is \
more favourable".format(profit_margin1, profit_margin2)

# Liquidity: Current Ratio
def validate_current_ratio(current_ratio):
    output = "Validation Result:\n"
    if current_ratio > 1.0:
        return output + "Current ratio is favourable. More short-term assets \
than short-term debts."
    elif current_ratio < 1.0:
        return output + "Current ratio is not favourable. More short-term \
debts than short-term assets. The company could be more vulnerable to unexpected\
bumps in the economy or business climate."
    else:
        return output + "Current ratio is exactly 1.0, so short-term assets \
equals short-term debts"

def compare_current_ratio(current_ratio1, current_ratio2):
    return "Current ratio comparison todo"

# Liquidity: Quick Ratio (ACID Test)
def validate_quick_ratio(quick_ratio):
    output = "Validation Result:\n"
    if quick_ratio > 1.0:
        return output + "Quick ratio is favourable. More short-term assets \
than short-term debts."
    elif quick_ratio < 1.0:
        return output + "Quick ratio is not favourable. More short-term \
debts than short-term assets. The company could be more vulnerable to unexpected\
bumps in the economy or business climate."
    else:
        return output + "Quick ratio is exactly 1.0, so short-term assets \
equals short-term debts"

def compare_quick_ratio(quick_ratio1, quick_ratio2):
    return "Quick ratio comparison todo"

# Debt: Debt to Equity Ratio
def validate_debt_to_equity_ratio(debt_to_equity_ratio):
    return "Validation Result:\nLower Debt to Equity ratio is better.\n\
Compare ratio {:f} with the ratio of another company in the same \
industry.\n".format(debt_to_equity_ratio)

def compare_debt_to_equity_ratio(debt_to_equity_ratio1, debt_to_equity_ratio2):
    output = "Validation Result:\nLower Debt to Equity ratios are better.\n"
    if debt_to_equity_ratio1 > debt_to_equity_ratio2:
        return output + "Debt to Equity ratio {:f} is less favourable than Debt to Equity ratio \
{:f}".format(debt_to_equity_ratio1, debt_to_equity_ratio2)
    elif debt_to_equity_ratio1 < debt_to_equity_ratio2:
        return output + "Debt to Equity ratio {:f} is more favourable than Debt to Equity ratio \
{:f}".format(debt_to_equity_ratio1, debt_to_equity_ratio2)
    else:
        return output + "Equal Debt to Equity ratios {:f} and {:f}, so neither is more \
favourable".format(debt_to_equity_ratio1, debt_to_equity_ratio2)

# Debt: Interest Coverage Ratio
def validate_interest_coverage_ratio(interest_coverage_ratio):
    output = "Validation Result:\nInterest coverage ratio below 1.0 is a sign of trouble.\n"
    if interest_coverage_ratio > 1.0:
        return output + "Interest coverage ratio is favourable."
    elif interest_coverage_ratio < 1.0:
        return output + "Interest coverage ratio is not favourable."
    else:
        return output + "Quick ratio is exactly 1.0"

# Efficiency: Asset Turnover Ratio
def validate_asset_turnover_ratio(asset_turnover_ratio):
    return "Validation Result:\nHigher Asset Turnover Ratio is better.\n\
Compare the Asset Turnover Ratio {:f} with that of another company in the \
same industry.\n".format(asset_turnover_ratio)

def compare_asset_turnover_ratio(asset_turnover_ratio1, asset_turnover_ratio2):
    output = "Validation Result:\nThe higher Asset Turnover Ratio is better.\n"
    if asset_turnover_ratio1 > asset_turnover_ratio2:
        return output + "Asset Turnover Ratio {:f} is more favourable than \
Asset Turnover Ratio {:f}.".format(asset_turnover_ratio1, asset_turnover_ratio2)
    elif asset_turnover_ratio1 < asset_turnover_ratio2:
        return output + "Asset Turnover Ratio {:f} is less favourable than \
Asset Turnover Ratio {:f}.".format(asset_turnover_ratio1, asset_turnover_ratio2)
    else:
        return output + "Equal Asset Turnover Ratio {:f} and {:f}, so neither is \
more favourable".format(asset_turnover_ratio1, asset_turnover_ratio2)

# Efficiency: Inventory Turnover Ratio
def validate_inventory_turnover_ratio(inventory_turnover_ratio):
    return "Validation Result:\nHigher Inventory Turnover Ratio is better.\n\
Compare the Inventory Turnover Ratio {:f} with that of another company in the \
same industry.\n".format(inventory_turnover_ratio)

def compare_inventory_turnover_ratio(inventory_turnover_ratio1, inventory_turnover_ratio2):
    output = "Validation Result:\nThe higher Inventory Turnover Ratio is better.\n"
    if inventory_turnover_ratio1 > inventory_turnover_ratio2:
        return output + "Inventory Turnover Ratio {:f} is more favourable than \
Inventory Turnover Ratio {:f}.".format(inventory_turnover_ratio1, inventory_turnover_ratio2)
    elif inventory_turnover_ratio1 < inventory_turnover_ratio2:
        return output + "Inventory Turnover Ratio {:f} is less favourable than \
Inventory Turnover Ratio {:f}.".format(inventory_turnover_ratio1, inventory_turnover_ratio2)
    else:
        return output + "Equal Inventory Turnover Ratio {:f} and {:f}, so neither is \
more favourable".format(inventory_turnover_ratio1, inventory_turnover_ratio2)

################ Generic Methods ################
# Generic higher is better 1 value
def validate_higher_better(profit_margin, description):
    return "Validation Result:\nHigher {} is better.\n\
Compare the {} {:f} with that of another company in the same industry.\n\
".format(description, description, profit_margin)

# Generic higher is better 2 values
def compare_higher_better(value1, value2, description):
    output = "Validation Result:\nThe higher {} is better.\n".format(description)
    if value1 > value2:
        return output + "{} {:f} is more favourable than \
{:f}.".format(description, value1, value2)
    elif value1 < value2:
        return output + "{} {:f} is less favourable than \
{:f}.".format(description, value1, value2)
    else:
        return output + "Equal {} {:f} and {:f}, so neither is \
more favourable".format(description, value1, value2)

# Generic lower is better 1 value
def validate_lower_better(profit_margin, description):
    return "Validation Result:\nLower {} is better.\n\
Compare the {} {:f} with that of another company in the same industry.\n\
".format(description, description, profit_margin)

# Generic lower is better 2 values
def compare_lower_better(value1, value2, description):
    output = "Validation Result:\nThe lower {} is better.\n".format(description)
    if value1 < value2:
        return output + "{} {:f} is more favourable than \
{:f}.".format(description, value1, value2)
    elif value1 > value2:
        return output + "{} {:f} is less favourable than \
{:f}.".format(description, value1, value2)
    else:
        return output + "Equal {} {:f} and {:f}, so neither is \
more favourable".format(description, value1, value2)