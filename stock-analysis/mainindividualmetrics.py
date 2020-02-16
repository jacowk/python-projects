#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:28:24 2020

@author: jaco
"""
import stockdescription as sd
import stockvalidation as sv
import stockcalc as sc

### PE Ratio ###
# Compare 
pe_ratio1 = 1.1
pe_ratio2 = 1.1
sv.compare_pe_ratio(pe_ratio1, pe_ratio2)

# Description
sd.descr_pe_ratio()

# Calculate
price_per_share = 1.1
earnings_per_share = 1.1
pe_ratio = sc.calc_pe_ratio(calc_pe_ratio(price_per_share, earnings_per_share))
print("PE Ratio is {:f}".format(pe_ratio))


validate_peg_ratio(peg_ratio)
compare_peg_ratio(peg_ratio1, peg_ratio2)
compare_ps_ratio(ps_ratio1, ps_ratio2)
compare_pb_ratio(pb_ratio1, pb_ratio2)
compare_dividend_yield(dividend_yield1, dividend_yield2)
validate_dividend_payout_ratio(dividend_payout_ratio)
compare_dividend_payout_ratio(dividend_payout_ratio1, dividend_payout_ratio2)
compare_return_on_assets(return_on_assets1, return_on_assets2)
compare_return_on_equity(return_on_equity1, return_on_equity2)
compare_profit_margin(profit_margin1, profit_margin2)
validate_current_ratio(current_ratio)
compare_current_ratio(current_ratio1, current_ratio2)
validate_quick_ratio(quick_ratio)
compare_quick_ratio(quick_ratio1, quick_ratio2)
compare_debt_to_equity_ratio(debt_to_equity_ratio1, debt_to_equity_ratio2)
validate_interest_coverage_ratio(interest_coverage_ratio)
compare_asset_turnover_ratio(asset_turnover_ratio1, asset_turnover_ratio2)
compare_inventory_turnover_ratio(inventory_turnover_ratio1, inventory_turnover_ratio2)

