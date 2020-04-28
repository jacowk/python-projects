#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:47:11 2020

@author: jaco
"""

import stockdescription as sd
import stockutils as su

json_data = su.retrieve_json()
su.output_pipe_delimited_string(sd.descr_introduction(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_ratio_categories(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_notes(json_data))
print("\n")

# Valuation
su.output_pipe_delimited_string(sd.descr_pe_ratio(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_peg_ratio(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_ps_ratio(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_pb_ratio(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_dividend_yield(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_dividend_payout_ratio(json_data))
print("\n")

# Profitability
su.output_pipe_delimited_string(sd.descr_return_on_assets(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_return_on_equity(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_profit_margin(json_data))
print("\n")

# Liquidity
su.output_pipe_delimited_string(sd.descr_current_ratio(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_quick_ratio(json_data)) # Revisit this one for better understanding, especially the validation of it
print("\n")

# Debt
su.output_pipe_delimited_string(sd.descr_debt_to_equity_ratio(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_interest_coverage_ratio(json_data))
print("\n")

# Efficiency
su.output_pipe_delimited_string(sd.descr_asset_turnover_ratio(json_data))
print("\n")
su.output_pipe_delimited_string(sd.descr_inventory_turnover_ratio(json_data))

