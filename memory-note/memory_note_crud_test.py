#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:47:50 2020

@author: jaco
"""
import memory_note_crud as mnc

def test_retrieve_all_memory_notes():
    result = mnc.retrieve_all_memory_notes()
    for item in result:
        print(item)

def test_retrieve_memory_note_by_id():
    memory_note_id = 1
    result = mnc.retrieve_memory_note_by_id(memory_note_id)
    print(result)

def test_insert_memory_note():
    note = "This is a test note"
    status = 2
    category = 1
    stage = 1
    odd_even = None
    week_day = None
    month_day = None
    mnc.insert_memory_note(note, status, category, stage, odd_even, week_day, month_day)
    result = mnc.retrieve_all_memory_notes()
    for item in result:
        print(item)

def test_update_memory_note():
    memory_note_id = 6
    result = mnc.retrieve_memory_note_by_id(memory_note_id)
    #(6, 'This is a test note', 2, 1, 1, None, None, None, )
    
    note = result[1] + " Updated"
    status = result[2]
    category = result[3]
    stage = result[4]
    odd_even = result[5]
    week_day = result[6]
    month_day = result[7]
    mnc.update_memory_note(memory_note_id, note, status, category, stage, odd_even, week_day, month_day)
    result = mnc.retrieve_memory_note_by_id(memory_note_id)
    print(result)

def test_delete_memory_note():
    memory_note_id = 6
    mnc.delete_memory_note(memory_note_id)
    result = mnc.retrieve_memory_note_by_id(memory_note_id)
    print(result)

#test_retrieve_all_memory_notes()
#test_retrieve_memory_note_by_id()
#test_insert_memory_note()
#test_update_memory_note()
test_delete_memory_note()
