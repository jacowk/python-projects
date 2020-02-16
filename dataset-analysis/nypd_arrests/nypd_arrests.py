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

filename = "nypd_arrests.csv"

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    cnt = 1
    
    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names
        
        ARREST_KEY = row[0]
        ARREST_DATE = row[1]
        PD_CD = row[2]
        PD_DESC = row[3]
        KY_CD = row[4]
        OFNS_DESC = row[5]
        LAW_CODE = row[6]
        LAW_CAT_CD = row[7]
        ARREST_BORO = row[8]
        ARREST_PRECINCT = row[9]
        JURISDICTION_CODE = row[10]
        AGE_GROUP = row[11]
        PERP_SEX = row[12]
        PERP_RACE = row[13]
        X_COORD_CD = row[14]
        Y_COORD_CD = row[15]
        Latitude = row[16]
        Longitude = row[17]

        #if ARREST_KEY in ('173121084', '173110239', '173111962', '173111101', '173097584', '173092308', '173091230'):
        #    print(row)
        
        print('ARREST_KEY: ', ARREST_KEY)
        print('ARREST_DATE: ', ARREST_DATE)
        print('PD_CD: ', PD_CD)
        print('PD_DESC: ', PD_DESC)
        print('KY_CD: ', KY_CD)
        print('OFNS_DESC: ', OFNS_DESC)
        print('LAW_CODE: ', LAW_CODE)
        print('LAW_CAT_CD: ', LAW_CAT_CD)
        print('ARREST_BORO: ', ARREST_BORO)
        print('ARREST_PRECINCT: ', ARREST_PRECINCT)
        print('JURISDICTION_CODE: ', JURISDICTION_CODE)
        print('AGE_GROUP: ', AGE_GROUP)
        print('PERP_SEX: ', PERP_SEX)
        print('PERP_RACE: ', PERP_RACE)
        print('X_COORD_CD: ', X_COORD_CD)
        print('Y_COORD_CD: ', Y_COORD_CD)
        print('Latitude: ', Latitude)
        print('Longitude: ', Longitude)
        cnt += 1
        
        print('\n')
        key = input("Press any key to continue, or 'q' to quite...")
        print('\n')
        if key == 'q':
            break
