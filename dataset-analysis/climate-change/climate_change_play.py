#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

To install mysql-connector go to Terminal in pycharm at the bottom, then type:
sudo python -m pip install mysql-connector

8599213 GlobalLandTemperaturesByCity.csv
"""
import csv #https://docs.python.org/3/library/csv.html
from datetime import datetime
import utils as u

print("Started")

filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity.csv"
store_dir = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity"

temperatures = dict()
city_name = "Aberdeen"

errors = []
cnt = 1
next_target_goal = 100000
next_target = next_target_goal

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')

    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names

        #print(row)

        Date = u.format_date(row[0])
        AverageTemperature = u.scrub_decimal(row[1])
        AverageTemperatureUncertainty = u.scrub_decimal(row[2])
        City = row[3]
        Country = row[4]
        Latitude = row[5]
        Longitude = row[6]

        if City == city_name:
            print("{}: {} - {}".format(City, Date, AverageTemperature))
            temperatures[Date] = AverageTemperature

        """
        print("Date: {}".format(Date))
        print("AverageTemperature: {}".format(u.scrub_decimal(AverageTemperature)))
        print("AverageTemperatureUncertainty: {}".format(u.scrub_decimal(AverageTemperatureUncertainty)))
        print("City: {}".format(City))
        print("Country: {}".format(Country))
        print("Latitude: {}".format(Latitude))
        print("Longitude: {}".format(Longitude))
        """

        if cnt == next_target:
            print("Progress: {}".format(cnt))
            next_target += next_target_goal

        cnt += 1

print("Done")