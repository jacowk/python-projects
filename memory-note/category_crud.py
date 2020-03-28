#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:24:12 2020

@author: jaco

CRUD operations for category
"""
import mysql.connector
import memory_note_mysql as mnm

def retrieve_all_categories():
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "SELECT * FROM category"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def retrieve_category_by_id(category_id):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "SELECT * FROM category WHERE id = %s"
    val = (category_id,) # For 1 parameter, there must be a comma after the parameter
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult  

def insert_category(description, status):
    print("Inserting category %s" % description)
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "INSERT INTO category(description, status) VALUES(%s, %s)"
    val = (description,status) # For 1 parameter, there must be a comma after the parameter
    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        print("Exception inserting category: %s", str(e))
    
def update_category(category_id, description, status):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "UPDATE category SET \
            description = %s, \
            status = %s \
            where id = %s"
    val = (description, status, category_id)
    mycursor.execute(sql, val)
    mydb.commit()
    
def delete_category(category_id):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    delete_status = "3" #Inactive status
    sql = "UPDATE category SET status = %s where id = %s"
    val = (delete_status, category_id)
    mycursor.execute(sql, val)
    mydb.commit()
