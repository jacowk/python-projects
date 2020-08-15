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
import mysql.connector as mysql
from datetime import datetime
import utils as u

print("Started")
db = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity.csv"

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

errors = []
cnt = 1
next_target_goal = 1000
next_target = next_target_goal

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')

    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names

        Date = u.format_date(row[0])
        AverageTemperature = u.scrub_decimal(row[1])
        AverageTemperatureUncertainty = u.scrub_decimal(row[2])
        City = row[3]
        Country = row[4]
        Latitude = row[5]
        Longitude = row[6]

        """
        print("Date: {}".format(Date))
        print("AverageTemperature: {}".format(u.scrub_decimal(AverageTemperature)))
        print("AverageTemperatureUncertainty: {}".format(u.scrub_decimal(AverageTemperatureUncertainty)))
        print("City: {}".format(City))
        print("Country: {}".format(Country))
        print("Latitude: {}".format(Latitude))
        print("Longitude: {}".format(Longitude))
        """

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "insert into climate_change(date, average_temperature, average_temperature_uncertainty, city, country, latitude, longitude) values (" \
            "'{:%Y-%m-%d}'," \
            "{:f}," \
            "{:f}," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}');".format(
            Date,
            AverageTemperature,
            AverageTemperatureUncertainty,
            City,
            Country,
            Latitude,
            Longitude
        );

        #print("{}: {}".format(cnt, sql))

        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except Exception as e:
           # Rollback in case there is any error
           print ("An error occured, rolling back: {}".format(str(e)))
           print("Error: {}".format(sql))
           errors.append(sql)
           db.rollback()

        if cnt == next_target:
            print("Progress: {}".format(cnt))
            next_target += next_target_goal

        cnt += 1

        """
        print('\n')
        key = input("Press any key to continue, or 'q' to quite...")
        print('\n')
        if key == 'q':
            break
        """

# disconnect from server
db.close()

for error in errors:
    print("Error: {}".format(error))

print("Done")