#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

"""
import csv #https://docs.python.org/3/library/csv.html
import stats_utils as su

filename = "mass_shootings.csv"
race_statistics = {}
gender_statistics = {}
mental_health_statistics = {}
year_statistics = {}

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    cnt = 1
    
    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names
        
        case = row[0]
        location = row[1]
        date = row[2]
        summary = row[3]
        fatalities = row[4]
        injured = row[5]
        total_victims = row[6]
        location = row[7]
        age_of_shooter = row[8]
        prior_signs_mental_health_issues = row[9]
        mental_health_details = row[10]
        weapons_obtained_legally = row[11]
        where_obtained = row[12]
        weapon_type = row[13]
        weapon_details = row[14]
        race = row[15]
        gender = row[16]
        sources = row[17]
        mental_health_sources = row[18]
        sources_additional_age = row[19]
        latitude = row[20]
        longitude = row[21]
        _type = row[22]
        year = row[23]

        # Prep race statistics
        race = su.scrub_data(race)
        race_statistics = su.prep_stats(race, race_statistics)
        
        # Prep gender statistics
        gender = su.scrub_data(gender)
        gender_statistics = su.prep_stats(gender, gender_statistics)
        
        # Prep mental health statistics
        prior_signs_mental_health_issues = su.scrub_data(prior_signs_mental_health_issues)
        mental_health_statistics = su.prep_stats(prior_signs_mental_health_issues, mental_health_statistics)
        
        # Prep year statistics
        year = su.scrub_data(year)
        year_statistics = su.prep_stats(year, year_statistics)

su.output_sorted_dict("Race statistics:", race_statistics)
su.output_sorted_dict("\nGender statistics:", gender_statistics)
su.output_sorted_dict("\nMental health statistics:", mental_health_statistics)
su.output_sorted_dict("\nYear statistics:", year_statistics)
