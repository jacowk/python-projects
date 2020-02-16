#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:30:12 2020

@author: jaco
"""
import stockanalysis as sa

sa.intro()

# Valuation
sa.analyse_pe_ratio()
sa.analyse_peg_ratio()
sa.analyse_ps_ratio()
sa.analyse_pb_ratio()
sa.analyse_dividend_yield()
sa.analyse_dividend_payout_ratio()

# Profitability
sa.analyse_return_on_assets()
sa.analyse_return_on_equity()
sa.analyse_profit_margin()

# Liquidity
sa.analyse_current_ratio()
sa.analyse_quick_ratio() # Revisit this one for better understanding, especially the validation of it

# Debt
sa.analyse_debt_to_equity_ratio()
sa.analyse_interest_coverage_ratio()

# Efficiency
sa.analyse_asset_turnover_ratio()
sa.analyse_inventory_turnover_ratio()

