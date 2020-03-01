#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:00:47 2020

@author: jaco

https://pypi.org/project/convertdate/
"""


from convertdate import hebrew

class CalculateHebrewDates():
    
    hebrew_month_dict = { 1: 'NISAN',
                         2: 'IYYAR',
                         3: 'SIVAN',
                         4: 'TAMMUZ',
                         5: 'AV',
                         6: 'ELUL',
                         7: 'TISHRI',
                         8: 'HESHVAN',
                         9: 'KISLEV',
                         10: 'TEVETH',
                         11: 'SHEVAT',
                         12: 'ADAR',
                         13: 'VEADAR'
    }
    
    def calc_hebrew_date(self, year, month, name):
        return hebrew.from_gregorian(2020, 2, 29)

    def get_hebrew_month_name(self, month):
        return self.hebrew_month_dict[month]

