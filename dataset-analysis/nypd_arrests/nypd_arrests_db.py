#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

----------------------------
Installing mysql for python:
----------------------------
https://pypi.org/project/mysqlclient/
https://mysqlclient.readthedocs.io/

----------------------------
If you get the error
----------------------------
ImportError: ... version `GLIBCXX_3.4.21' not found

https://askubuntu.com/questions/575505/glibcxx-3-4-20-not-found-how-to-fix-this-error
conda install libgcc

----------------------------
https://pythonspot.com/mysql-with-python/
https://www.tutorialspoint.com/python/python_database_access.htm
----------------------------
String formatting:
https://pyformat.info/#simple
----------------------------

Public Datasets:
    https://www.tableau.com/learn/articles/free-public-data-sets
    https://www.springboard.com/blog/free-public-data-sets-data-science-project/
    https://www.forbes.com/sites/bernardmarr/2016/02/12/big-data-35-brilliant-and-free-data-sources-for-2016/#127c8d21b54d
    https://www.data.gov/
    https://www.forbes.com/sites/metabrown/2017/04/30/these-are-the-10-most-popular-datasets-on-the-us-government-data-portal/#631cd64b748b
    
    https://www.kdnuggets.com/datasets/government-local-public.html
    https://nasa.github.io/data-nasa-gov-frontpage/
    https://docs.opendata.aws/1000genomes/readme.html
    https://ucr.fbi.gov/crime-in-the-u.s/2016/crime-in-the-u.s.-2016/topic-pages/tables/table-1
    https://www.cia.gov/library/publications/the-world-factbook/
    https://www.data.gov/climate/
    ftp://ftp.ncdc.noaa.gov/pub/data/normals/1981-2010/ (FTP site)
    
    https://code.gov/
    Try data.gov


"""
import csv #https://docs.python.org/3/library/csv.html
import stats_utils as su
import sys
import MySQLdb as mysql
from datetime import datetime

db = mysql.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

year = 2017
filename = "nypd_arrests.csv"

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    cnt = 1
    
    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names
        
        arrest_key = int(row[0])
        arrest_date = datetime.strptime(row[1], '%m/%d/%Y')
        arrest_year = int(su.get_year(row[1]))
        pd_cd = int(row[2])
        pd_desc = row[3]
        try:
            ky_cd = int(row[4])
        except:
            ky_cd = 0
        ofns_desc = row[5].replace('\'', '')
        law_code = row[6]
        law_cat_cd = row[7]
        arrest_boro = row[8]
        arrest_precinct = int(row[9])
        jurisdiction_code = int(row[10])
        age_group = row[11]
        perp_sex = row[12]
        perp_race = row[13]
        x_coord_cd = float(row[14])
        y_coord_cd = float(row[15])
        latitude = float(row[16])
        longitude = float(row[17])

        if not arrest_year == year:
            continue

        #print("Inserting ", arrest_key)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        
        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO nypd_arrests_{:s}(\
            arrest_key, \
            arrest_date, \
            arrest_year, \
            pd_cd, \
            pd_desc, \
            ky_cd, \
            ofns_desc, \
            law_code, \
            law_cat_cd, \
            arrest_boro, \
            arrest_precinct, \
            jurisdiction_code, \
            age_group, \
            perp_sex, \
            perp_race, \
            x_coord_cd, \
            y_coord_cd, \
            latitude, \
            longitude \
        ) VALUES ({:d}, \
           '{:%Y-%m-%d}', \
            {:d}, \
            {:d}, \
            '{:s}', \
            {:d}, \
            '{:s}', \
            '{:s}', \
            '{:s}', \
            '{:s}', \
            {:d}, \
            {:d}, \
            '{:s}', \
            '{:s}', \
            '{:s}', \
            {:f}, \
            {:f}, \
            {:f}, \
            {:f} \
            )".format(
            str(year),
            arrest_key, 
            arrest_date.date(), 
            arrest_year,
            pd_cd,
            pd_desc,
            ky_cd,
            ofns_desc,
            law_code,
            law_cat_cd,
            arrest_boro,
            arrest_precinct,
            jurisdiction_code,
            age_group,
            perp_sex,
            perp_race,
            x_coord_cd,
            y_coord_cd,
            latitude,
            longitude
        )
        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except Exception as e:
           # Rollback in case there is any error
           print ("An error occured, rolling back for {:d}: {}".format(arrest_key, str(e)))
           db.rollback()
        
        cnt += 1
        
        #if cnt == 5:
        #    break

# disconnect from server
db.close()
