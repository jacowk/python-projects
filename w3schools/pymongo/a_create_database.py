#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:21:21 2020

@author: jaco
"""

# https://www.w3schools.com/python/python_mongodb_create_db.asp
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

print(myclient.list_database_names())
