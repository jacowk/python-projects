#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:14:34 2020

@author: jaco

CRUD operations for memory_note
"""
import memory_note_mysql as mnm

def retrieve_all_memory_notes():
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "SELECT * FROM memory_note"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def retrieve_memory_note_by_id(memory_note_id):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "SELECT * FROM memory_note WHERE id = %s"
    val = (memory_note_id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return myresult  

def retrieve_memory_note_by_category_stage(category, stage):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "SELECT * FROM memory_note WHERE category = %s and stage = %s"
    val = (category, stage)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult  

def insert_memory_note(note, status, category, stage, odd_even, week_day, month_day):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "INSERT INTO memory_note (note, status, category, stage, odd_even, week_day, month_day) \
            VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (note, status, category, stage, odd_even, week_day, month_day)
    mycursor.execute(sql, val)
    mydb.commit()
    
def update_memory_note(memory_note_id, note, status, category, stage, odd_even, week_day, month_day):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    sql = "UPDATE memory_note SET \
        note = %s, \
        status = %s, \
        category = %s, \
        stage = %s, \
        odd_even = %s, \
        week_day = %s, \
        month_day = %s \
        where id = %s"
    val = (note, status, category, stage, odd_even, week_day, month_day, memory_note_id)
    mycursor.execute(sql, val)
    mydb.commit()
    
def delete_memory_note(memory_note_id):
    mydb = mnm.get_msql_connection()
    mycursor = mnm.get_msql_connection_cursor(mydb)
    delete_status = "3"
    sql = "UPDATE memory_note SET status = %s where id = %s"
    val = (delete_status, memory_note_id)
    mycursor.execute(sql, val)
    mydb.commit()


