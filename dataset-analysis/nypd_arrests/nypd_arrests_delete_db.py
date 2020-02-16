#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:03:34 2020

@author: jaco

https://stackoverflow.com/questions/5836623/getting-lock-wait-timeout-exceeded-try-restarting-transaction-even-though-im
"""
import MySQLdb as mysql

from datetime import datetime

db = mysql.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select arrest_key from nypd_arrests"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   cnt = 1
   for row in results:
      arrest_key = row[0]
      print("%d - arrest_key = %d" % (cnt, arrest_key))
      delete_cursor = db.cursor()
      delete_sql = "delete from nypd_arrests where arrest_key = '%d'" % (arrest_key)
      print(delete_sql)
      delete_cursor.execute(delete_sql)
      db.commit()
      cnt += 1
except Exception as e:
    db.rollback()
    print("Error: unable to fetch data: %s" % str(e))

# disconnect from server
db.close()

