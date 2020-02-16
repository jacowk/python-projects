#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:44:02 2020

@author: jaco
"""
# https://www.w3schools.com/python/python_mysql_getstarted.asp

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)
