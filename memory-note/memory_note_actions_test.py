#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:56:02 2020

@author: jaco
"""
import memory_note_crud as mnc
import memory_note_actions as mna
import memory_note_constant as mncon

def test_promote_memory_note():
    memory_note_id = 4
    stage_value = 10
    memory_note = mnc.retrieve_memory_note_by_id(memory_note_id)
    print(memory_note)
    result = mna.promote_memory_note(memory_note_id, stage_value)
    print(result)
    memory_note = mnc.retrieve_memory_note_by_id(memory_note_id)
    print(memory_note)

def test_validate_stage_value():
    promoted_stage = 4
    stage_value = 10
    result = mna.validate_stage_value(promoted_stage, stage_value)
    print(result)

def test_update_memory_note():
    print("Running test_update_memory_note")
    memory_note_id = 1
    memory_note = mnc.retrieve_memory_note_by_id(memory_note_id)
    print(memory_note)
    promoted_stage = 4
    stage_value = 10
    mna.update_memory_note(memory_note, promoted_stage, stage_value)
    memory_note = mnc.retrieve_memory_note_by_id(memory_note_id)
    print(memory_note)
    

def test_retrieve_stage_1_memory_notes():
    category = 1
    results = mna.retrieve_stage_1_memory_notes(category)
    for item in results:
        print(item)

def test_retrieve_stage_2_memory_notes():
    category = 1
    results = mna.retrieve_stage_2_memory_notes(category)
    for item in results:
        print(item)

def test_retrieve_stage_3_memory_notes():
    category = 1
    results = mna.retrieve_stage_3_memory_notes(category)
    for item in results:
        print(item)

def test_retrieve_stage_4_memory_notes():
    category = 1
    results = mna.retrieve_stage_4_memory_notes(category)
    for item in results:
        print(item)


def test_retrieve_memory_notes_today():
    category = 1
    results = mna.retrieve_memory_notes_today(category)
    for item in results:
        print(item)

#test_promote_memory_note()
#test_validate_stage_value()
#test_update_memory_note()
        
test_retrieve_memory_notes_today()
#test_retrieve_stage_1_memory_notes()
#test_retrieve_stage_2_memory_notes()
#test_retrieve_stage_3_memory_notes()
#test_retrieve_stage_4_memory_notes()
        