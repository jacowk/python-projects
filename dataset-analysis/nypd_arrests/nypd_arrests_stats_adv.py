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
from datetime import datetime

filename = "nypd_arrests.csv"
race_statistics = {}
gender_statistics = {}
pd_dict = {}
pd_desc_statistics = {}
pd_cd_statistics = {}
age_group_statistics = {}
year_statistics = {}
pd_dict = su.load_dict_from_file("pd_dict.csv")

# Parameters
par_from_date = datetime.strptime("01/01/2019", "%d/%m/%Y")
par_to_date = datetime.strptime("31/12/2019", "%d/%m/%Y")
par_age_group = "65+" # 18-24, 25-44, 45-64, 65+, <18
par_gender = "M" # M or F
par_race = "WHITE"
par_pd_cd = "100"
par_year = "2015" #2015, 2016, 2017

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
        """X_COORD_CD = row[14]
        Y_COORD_CD = row[15]
        Latitude = row[16]
        Longitude = row[17]"""
        
        """
        # Convert arrest date to object
        arrest_date_object = datetime.strptime(ARREST_DATE, "%m/%d/%Y")
        if par_from_date <= arrest_date_object <= par_to_date:
            # Date between
            print (ARREST_DATE, " between")
        else:
            #print (ARREST_DATE, " not between")
            continue
        """
        
        # Parameters
        arrest_year = su.get_year(ARREST_DATE)
        if not arrest_year == par_year:
            continue
        
        if not AGE_GROUP == par_age_group:
            continue
        
        if not PERP_SEX == par_gender:
            continue
        
        if not PERP_RACE == par_race:
            continue
        
        #if not PD_CD == par_pd_cd:
        #    continue

        # Prep year statistics
        year = su.get_year(ARREST_DATE)
        year_statistics = su.prep_stats(year, year_statistics)
        
        # Prep race statistics
        PERP_RACE = su.scrub_data(PERP_RACE)
        race_statistics = su.prep_stats(PERP_RACE, race_statistics)
        
        # Prep gender statistics
        PERP_SEX = su.scrub_data(PERP_SEX)
        gender_statistics = su.prep_stats(PERP_SEX, gender_statistics)
        
        # Harvest pd_cd and pd_desc values
        pd_dict = su.harvest_dict_values(PD_CD, PD_DESC, pd_dict)
        
        # Prep pd_desc statistics
        PD_DESC = su.scrub_data(PD_DESC)
        pd_desc_statistics = su.prep_stats(PD_DESC, pd_desc_statistics)
        
        # Prep pd_cd statistics
        PD_CD = su.scrub_data(PD_CD)
        pd_cd_statistics = su.prep_stats(PD_CD, pd_cd_statistics)
        
        # Prep age group statistics
        AGE_GROUP = su.scrub_data(AGE_GROUP)
        age_group_statistics = su.prep_stats(AGE_GROUP, age_group_statistics)

su.output_sorted_dict("Year statistics:", year_statistics)
su.output_sorted_dict("\nRace statistics:", race_statistics)
su.output_sorted_dict("\nGender statistics:", gender_statistics)
#su.output_sorted_dict("\nPD Desc statistics:", pd_desc_statistics)
su.output_sorted_pd_cd("\nPD CD statistics:", pd_cd_statistics, pd_dict, 10)
su.output_sorted_dict("\nAge Group statistics:", age_group_statistics)
#su.output_sorted_dict("\nPD CD and PD Desc:", pd_dict)


"""
Total: 942096 nypd_arrests.csv


Race statistics:
american indian/alaskan native :: 2236
asian / pacific islander :: 45683
black :: 450559
black hispanic :: 80117
unknown :: 9231
white :: 114847
white hispanic :: 239422


Gender statistics:
f :: 161841
m :: 780254


Age Group statistics:
18-24 :: 238778
25-44 :: 455664
45-64 :: 179911
65+ :: 9012
<18 :: 58730


PD Desc statistics:
 :: 2713
a.b.c.,false proof of age :: 46
abortion 1 :: 4
absconding from work release 2 :: 2
accosting,fraudulent :: 445
adm.code,unclassified misdemea :: 46
adm.code,unclassified violatio :: 1593
adm.code,unclassified violation :: 8436
aggravated criminal contempt :: 456
aggravated harassment 1 :: 209
aggravated harassment 2 :: 11964
agriculture & markets law,uncl :: 1
"""