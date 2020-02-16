#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:47:14 2020

@author: jaco
"""

import matplotlib.pyplot as plt
import MySQLdb as mysql

# Total arrests per age group

table_name = "nypd_arrests_2015"

db = mysql.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

# prepare a cursor object using cursor() method
cursor = db.cursor()

select count(na.id) as cnt, na.age_group 
from nypd_arrests_2015 na
group by na.age_group
order by cnt desc;