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
monthly_interest_amount = 998.57
m_monthly_interest_amount = Money(monthly_interest_amount, money_format)

capital_amount = 201347.18
m_capital_amount = Money(capital_amount, money_format)

# Calculate annual interest
annual_interest_amount = monthly_interest_amount * 12
m_annual_interest_amount = Money(annual_interest_amount, money_format)

# Calculate interest rate
interest_rate = (monthly_interest_amount / capital_amount) * 100

print("Capital Amount: ", m_capital_amount)
print("Monthly Interest Amount: ", m_monthly_interest_amount)
print("Annual Interest Amount: ", m_annual_interest_amount)
print("Interest Rate: ", round(interest_rate, 2))
