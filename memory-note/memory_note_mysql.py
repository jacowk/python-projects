#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:25:59 2020

@author: jaco
"""
import mysql.connector

def get_msql_connection():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="memorynote" # Auto select the database
    )
    return mydb

def get_msql_connection_cursor(mydb):
    return mydb.cursor()
    