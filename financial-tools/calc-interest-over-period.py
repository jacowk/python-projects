#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:15:46 2020

@author: jaco

Inflation Rate: 2020 - 5.17 %

"""
#https://pypi.org/project/money/

import pandas as pd
from money import Money

money_format = 'ZAR'
display_monthly = False

#Starting with an investment
starting_year = 2020
no_of_years = 23
interest_rate = 5
monthly_contribution = 1000
capital_amount = 600000

# Starting from scratch
#no_of_years = 45
#interest_rate = 7.5
#monthly_contribution = 1000
#capital_amount = 0

months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for year_no in range (1, no_of_years + 1):
    one_year_values = []
    for month_no in range(0, 12):
        # Add monthly contribution
        capital_amount = capital_amount + monthly_contribution
        
        # Calculate interest
        calculated_interest = capital_amount * (interest_rate / 100) / 12
        capital_amount += calculated_interest
        
        if display_monthly:
            print("Year No: ", year_no, 
              "- Actual Year: ", starting_year,
              "- Month: ", months[11], 
              "- Interest: ", Money(calculated_interest, money_format), 
              "- Investment Value", Money(capital_amount, money_format))

    if not display_monthly:
        print("Year No: ", year_no, 
              "- Actual Year: ", starting_year,
              "- Month: ", months[11], 
              "- Interest: ", Money(calculated_interest, money_format), 
              "- Investment Value", Money(capital_amount, money_format))
    starting_year += 1

"""
Goal: 
no_of_years = 23
interest_rate = 7.5 (Wished for)
monthly_contribution = 1000
capital_amount = 600000

Year No:  1 - Actual Year:  2020 - Month:  Dec - Interest:  ZAR 4,093.65 - Investment Value ZAR 659,078.41
Year No:  2 - Actual Year:  2021 - Month:  Dec - Interest:  ZAR 4,489.09 - Investment Value ZAR 722,743.23
Year No:  3 - Actual Year:  2022 - Month:  Dec - Interest:  ZAR 4,915.22 - Investment Value ZAR 791,350.51
Year No:  4 - Actual Year:  2023 - Month:  Dec - Interest:  ZAR 5,374.43 - Investment Value ZAR 865,283.95
Year No:  5 - Actual Year:  2024 - Month:  Dec - Interest:  ZAR 5,869.30 - Investment Value ZAR 944,957.04
Year No:  6 - Actual Year:  2025 - Month:  Dec - Interest:  ZAR 6,402.58 - Investment Value ZAR 1,030,815.36
Year No:  7 - Actual Year:  2026 - Month:  Dec - Interest:  ZAR 6,977.26 - Investment Value ZAR 1,123,339.09
Year No:  8 - Actual Year:  2027 - Month:  Dec - Interest:  ZAR 7,596.56 - Investment Value ZAR 1,223,045.67
Year No:  9 - Actual Year:  2028 - Month:  Dec - Interest:  ZAR 8,263.93 - Investment Value ZAR 1,330,492.73
Year No:  10 - Actual Year:  2029 - Month:  Dec - Interest:  ZAR 8,983.11 - Investment Value ZAR 1,446,281.19
Year No:  11 - Actual Year:  2030 - Month:  Dec - Interest:  ZAR 9,758.13 - Investment Value ZAR 1,571,058.60
Year No:  12 - Actual Year:  2031 - Month:  Dec - Interest:  ZAR 10,593.31 - Investment Value ZAR 1,705,522.82
Year No:  13 - Actual Year:  2032 - Month:  Dec - Interest:  ZAR 11,493.33 - Investment Value ZAR 1,850,425.83
Year No:  14 - Actual Year:  2033 - Month:  Dec - Interest:  ZAR 12,463.22 - Investment Value ZAR 2,006,578.05
Year No:  15 - Actual Year:  2034 - Month:  Dec - Interest:  ZAR 13,508.40 - Investment Value ZAR 2,174,852.76
Year No:  16 - Actual Year:  2035 - Month:  Dec - Interest:  ZAR 14,634.73 - Investment Value ZAR 2,356,191.08
Year No:  17 - Actual Year:  2036 - Month:  Dec - Interest:  ZAR 15,848.49 - Investment Value ZAR 2,551,607.17
Year No:  18 - Actual Year:  2037 - Month:  Dec - Interest:  ZAR 17,156.48 - Investment Value ZAR 2,762,193.92
Year No:  19 - Actual Year:  2038 - Month:  Dec - Interest:  ZAR 18,566.02 - Investment Value ZAR 2,989,129.06
Year No:  20 - Actual Year:  2039 - Month:  Dec - Interest:  ZAR 20,084.98 - Investment Value ZAR 3,233,681.76
Year No:  21 - Actual Year:  2040 - Month:  Dec - Interest:  ZAR 21,721.86 - Investment Value ZAR 3,497,219.73
Year No:  22 - Actual Year:  2041 - Month:  Dec - Interest:  ZAR 23,485.82 - Investment Value ZAR 3,781,216.83
Year No:  23 - Actual Year:  2042 - Month:  Dec - Interest:  ZAR 25,386.72 - Investment Value ZAR 4,087,261.37

"""

"""
starting_year = 2020
no_of_years = 23
interest_rate = 6 (Depositor Plus)
monthly_contribution = 1000
capital_amount = 600000

Year No:  1 - Actual Year:  2020 - Month:  Dec - Interest:  ZAR 3,230.87 - Investment Value ZAR 649,403.93
Year No:  2 - Actual Year:  2021 - Month:  Dec - Interest:  ZAR 3,491.82 - Investment Value ZAR 701,854.98
Year No:  3 - Actual Year:  2022 - Month:  Dec - Interest:  ZAR 3,768.86 - Investment Value ZAR 757,541.10
Year No:  4 - Actual Year:  2023 - Month:  Dec - Interest:  ZAR 4,062.99 - Investment Value ZAR 816,661.82
Year No:  5 - Actual Year:  2024 - Month:  Dec - Interest:  ZAR 4,375.27 - Investment Value ZAR 879,428.97
Year No:  6 - Actual Year:  2025 - Month:  Dec - Interest:  ZAR 4,706.80 - Investment Value ZAR 946,067.47
Year No:  7 - Actual Year:  2026 - Month:  Dec - Interest:  ZAR 5,058.79 - Investment Value ZAR 1,016,816.08
Year No:  8 - Actual Year:  2027 - Month:  Dec - Interest:  ZAR 5,432.48 - Investment Value ZAR 1,091,928.31
Year No:  9 - Actual Year:  2028 - Month:  Dec - Interest:  ZAR 5,829.22 - Investment Value ZAR 1,171,673.30
Year No:  10 - Actual Year:  2029 - Month:  Dec - Interest:  ZAR 6,250.43 - Investment Value ZAR 1,256,336.78
Year No:  11 - Actual Year:  2030 - Month:  Dec - Interest:  ZAR 6,697.62 - Investment Value ZAR 1,346,222.13
Year No:  12 - Actual Year:  2031 - Month:  Dec - Interest:  ZAR 7,172.40 - Investment Value ZAR 1,441,651.40
Year No:  13 - Actual Year:  2032 - Month:  Dec - Interest:  ZAR 7,676.45 - Investment Value ZAR 1,542,966.55
Year No:  14 - Actual Year:  2033 - Month:  Dec - Interest:  ZAR 8,211.59 - Investment Value ZAR 1,650,530.59
Year No:  15 - Actual Year:  2034 - Month:  Dec - Interest:  ZAR 8,779.75 - Investment Value ZAR 1,764,728.94
Year No:  16 - Actual Year:  2035 - Month:  Dec - Interest:  ZAR 9,382.94 - Investment Value ZAR 1,885,970.80
Year No:  17 - Actual Year:  2036 - Month:  Dec - Interest:  ZAR 10,023.34 - Investment Value ZAR 2,014,690.60
Year No:  18 - Actual Year:  2037 - Month:  Dec - Interest:  ZAR 10,703.23 - Investment Value ZAR 2,151,349.54
Year No:  19 - Actual Year:  2038 - Month:  Dec - Interest:  ZAR 11,425.06 - Investment Value ZAR 2,296,437.32
Year No:  20 - Actual Year:  2039 - Month:  Dec - Interest:  ZAR 12,191.41 - Investment Value ZAR 2,450,473.79
Year No:  21 - Actual Year:  2040 - Month:  Dec - Interest:  ZAR 13,005.03 - Investment Value ZAR 2,614,010.89
Year No:  22 - Actual Year:  2041 - Month:  Dec - Interest:  ZAR 13,868.83 - Investment Value ZAR 2,787,634.60
Year No:  23 - Actual Year:  2042 - Month:  Dec - Interest:  ZAR 14,785.91 - Investment Value ZAR 2,971,967.04

"""

"""
starting_year = 2020
no_of_years = 23
interest_rate = 5 (Investment Advantage)
monthly_contribution = 1000
capital_amount = 600000

Year No:  1 - Actual Year:  2020 - Month:  Dec - Interest:  ZAR 2,668.16 - Investment Value ZAR 643,027.16
Year No:  2 - Actual Year:  2021 - Month:  Dec - Interest:  ZAR 2,855.83 - Investment Value ZAR 688,255.66
Year No:  3 - Actual Year:  2022 - Month:  Dec - Interest:  ZAR 3,053.10 - Investment Value ZAR 735,798.15
Year No:  4 - Actual Year:  2023 - Month:  Dec - Interest:  ZAR 3,260.47 - Investment Value ZAR 785,772.99
Year No:  5 - Actual Year:  2024 - Month:  Dec - Interest:  ZAR 3,478.44 - Investment Value ZAR 838,304.65
Year No:  6 - Actual Year:  2025 - Month:  Dec - Interest:  ZAR 3,707.57 - Investment Value ZAR 893,523.92
Year No:  7 - Actual Year:  2026 - Month:  Dec - Interest:  ZAR 3,948.42 - Investment Value ZAR 951,568.32
Year No:  8 - Actual Year:  2027 - Month:  Dec - Interest:  ZAR 4,201.59 - Investment Value ZAR 1,012,582.38
Year No:  9 - Actual Year:  2028 - Month:  Dec - Interest:  ZAR 4,467.71 - Investment Value ZAR 1,076,718.03
Year No:  10 - Actual Year:  2029 - Month:  Dec - Interest:  ZAR 4,747.45 - Investment Value ZAR 1,144,134.99
Year No:  11 - Actual Year:  2030 - Month:  Dec - Interest:  ZAR 5,041.50 - Investment Value ZAR 1,215,001.12
Year No:  12 - Actual Year:  2031 - Month:  Dec - Interest:  ZAR 5,350.59 - Investment Value ZAR 1,289,492.90
Year No:  13 - Actual Year:  2032 - Month:  Dec - Interest:  ZAR 5,675.50 - Investment Value ZAR 1,367,795.82
Year No:  14 - Actual Year:  2033 - Month:  Dec - Interest:  ZAR 6,017.03 - Investment Value ZAR 1,450,104.87
Year No:  15 - Actual Year:  2034 - Month:  Dec - Interest:  ZAR 6,376.04 - Investment Value ZAR 1,536,625.01
Year No:  16 - Actual Year:  2035 - Month:  Dec - Interest:  ZAR 6,753.41 - Investment Value ZAR 1,627,571.68
Year No:  17 - Actual Year:  2036 - Month:  Dec - Interest:  ZAR 7,150.09 - Investment Value ZAR 1,723,171.35
Year No:  18 - Actual Year:  2037 - Month:  Dec - Interest:  ZAR 7,567.06 - Investment Value ZAR 1,823,662.08
Year No:  19 - Actual Year:  2038 - Month:  Dec - Interest:  ZAR 8,005.37 - Investment Value ZAR 1,929,294.11
Year No:  20 - Actual Year:  2039 - Month:  Dec - Interest:  ZAR 8,466.10 - Investment Value ZAR 2,040,330.48
Year No:  21 - Actual Year:  2040 - Month:  Dec - Interest:  ZAR 8,950.41 - Investment Value ZAR 2,157,047.68
Year No:  22 - Actual Year:  2041 - Month:  Dec - Interest:  ZAR 9,459.49 - Investment Value ZAR 2,279,736.35
Year No:  23 - Actual Year:  2042 - Month:  Dec - Interest:  ZAR 9,994.61 - Investment Value ZAR 2,408,702.00

"""