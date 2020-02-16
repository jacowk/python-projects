#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:15:46 2020

@author: jaco
"""
#https://pypi.org/project/money/

import pandas as pd
from money import Money

money_format = 'ZAR'
interest_rate = 7.5
capital_amount = 1000000
m_capital_amount = Money(capital_amount, money_format)

# Calculate annual interest
annual_calculated_interest = capital_amount * (interest_rate / 100)
m_annual_calculated_interest = Money(annual_calculated_interest, money_format)

# Calculate monthly interest
monthly_calculated_interest = annual_calculated_interest / 12
m_monthly_calculated_interest = Money(monthly_calculated_interest, money_format)

print("Capital Amount: " + str(m_capital_amount))
print("Interest Rate: " + str(interest_rate) + " %")
print("Annual interest: " + str(m_annual_calculated_interest))
print("Monthly interest: " + str(m_monthly_calculated_interest))

