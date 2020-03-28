#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:30:34 2020

@author: jaco
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydatabase" # Auto select the database
)

"""
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
# Fetch one
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print("\n")
print(myresult)

# Where clause to prevent sql injection
print("\n")
print("Where clause to prevent sql injection")
sql = "SELECT * FROM customers WHERE address = %s"
adr = "Yellow Garden 2"

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

"""