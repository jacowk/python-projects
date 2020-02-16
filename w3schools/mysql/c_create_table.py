#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:23:30 2020

@author: jaco
"""

# https://www.w3schools.com/python/python_mysql_create_table.asp

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydatabase" # Auto select the database
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") 

# Check if the table exists
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 