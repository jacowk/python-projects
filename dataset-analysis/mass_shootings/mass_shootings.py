#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

"""
import csv #https://docs.python.org/3/library/csv.html

filename = "mass-shootings.csv"

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

        print('year: ', year)
        
        print('case: ', case)
        print('location: ', location)
        print('date: ', date)
        print('summary: ', summary)
        print('fatalities: ', fatalities)
        print('injured: ', injured)
        print('total_victims: ', total_victims)
        print('location: ', location)
        print('age_of_shooter: ', age_of_shooter)
        print('prior_signs_mental_health_issues: ', prior_signs_mental_health_issues)
        print('mental_health_details: ', mental_health_details)
        print('weapons_obtained_legally: ', weapons_obtained_legally)
        print('where_obtained: ', where_obtained)
        print('weapon_type: ', weapon_type)
        print('weapon_details: ', weapon_details)
        print('race: ', race)
        print('gender: ', gender)
        #print('sources: ', sources)
        #print('mental_health_sources: ', mental_health_sources)
        print('sources_additional_age: ', sources_additional_age)
        #print('latitude: ', latitude)
        #print('longitude: ', longitude)
        print('type: ', _type)
        print('Item no %d' % cnt)
        cnt += 1
        
        print('\n')
        key = input("Press any key to continue, or 'q' to quite...")
        print('\n')
        if key == 'q':
            break


