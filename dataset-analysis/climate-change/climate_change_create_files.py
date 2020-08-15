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
import utils as u
import os.path as o
import sys as s

print("Started")

filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity.csv"
store_dir = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity"

header = "Date,AverageTemperature,AverageTemperatureUncertainty,City,Country,Latitude,Longitude\n"

errors = []
cnt = 1
next_target_goal = 10000
next_target = next_target_goal

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')

    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names

        #print(row)

        #Convert list to string
        separator = ","
        store_data = "{}\n".format(separator.join(row))

        Date = u.format_date(row[0])
        AverageTemperature = u.scrub_decimal(row[1])
        AverageTemperatureUncertainty = u.scrub_decimal(row[2])
        City = row[3]
        Country = row[4]
        Latitude = row[5]
        Longitude = row[6]

        #Check if a file for the city exists
        store_file = "{}/{}.csv".format(store_dir, City)

        #If the file does not exists, write header to file, else just write the data
        if not o.exists(store_file):
            f = open(store_file, "a")
            f.write(header)
            f.write(store_data)
            f.close()
        else:
            f = open(store_file, "a")
            f.write(store_data)
            f.close()

        if cnt == next_target:
            print("Progress: {}".format(cnt))
            next_target += next_target_goal
            #s.exit()

        cnt += 1

print("Done")