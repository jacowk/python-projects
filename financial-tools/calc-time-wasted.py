#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:15:15 2020

@author: jaco
"""

minutes_wasted_per_day = 30
no_of_years = 20
include_weekends = True

def calc_minutes_wasted(no_week_days):
    hours_wasted_per_day = minutes_wasted_per_day / 60
    
    minutes_wasted_per_week = minutes_wasted_per_day * no_week_days
    hours_wasted_per_week = minutes_wasted_per_week / 60
    
    minutes_wasted_per_month = minutes_wasted_per_week * 4
    hours_wasted_per_month = minutes_wasted_per_month / 60
    
    minutes_wasted_per_year = minutes_wasted_per_month * 12
    hours_wasted_per_year = minutes_wasted_per_year / 60
    
    minutes_wasted_for_no_years = minutes_wasted_per_year * no_of_years
    hours_wasted_for_no_years = minutes_wasted_for_no_years / 60
    
    #print("minutes_wasted_per_day: ", minutes_wasted_per_day)
    print("hours_wasted_per_day: ", round(hours_wasted_per_day, 2))
    
    #print("\nminutes_wasted_per_week: ", minutes_wasted_per_week)
    print("hours_wasted_per_week: ", round(hours_wasted_per_week, 2))
    
    #print("\nminutes_wasted_per_month: ", minutes_wasted_per_month)
    print("hours_wasted_per_month: ", round(hours_wasted_per_month, 2))
    
    #print("\nminutes_wasted_per_year: ", minutes_wasted_per_year)
    print("hours_wasted_per_year: ", round(hours_wasted_per_year, 2))
    
    #print("\nminutes_wasted_for: ", no_of_years, "years: ",  minutes_wasted_for_no_years)
    print("hours_wasted_for: ", no_of_years, "years: ", round(hours_wasted_for_no_years, 2))
    

if include_weekends:
    calc_minutes_wasted(7)
else:
    calc_minutes_wasted(5)