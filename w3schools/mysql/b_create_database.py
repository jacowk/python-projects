#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:21:02 2020

@author: jaco
"""

# https://www.w3schools.com/python/python_mysql_create_db.asp

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

# Check if the database exist
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
