#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:03:07 2020

@author: jaco
"""
import memory_note_mysql as mnm
import memory_note_crud as mnc
import memory_note_constant as mncon
from datetime import datetime as dt

#Promote memory note to the next stage
"""
The stage_value represents the values of one of the following columns,
depending on the promoted stage:
Stage, Column, stage_value
2,odd_even,"Odd" or "Even"
3,week_day,"Mon" to "Sun"
4,month_day,1-31
"""
def promote_memory_note(memory_note_id, stage_value):
    #Retrieve the memory note
    memory_note = mnc.retrieve_memory_note_by_id(memory_note_id)
    
    #Determine the next stage
    current_stage = memory_note[4]
    promoted_stage = 0
    if (current_stage < 4):
        promoted_stage = current_stage + 1
    else:
        return mncon.MAX_STAGE
    
    #Validate the stage_value against the promoted stage
    validation_result = validate_stage_value(promoted_stage, stage_value)
    
    #Update the memory note with the promoted stage and stage_value
    if (validation_result == mncon.VALID):
        update_memory_note(memory_note, promoted_stage, stage_value)
        return mncon.PROMOTED
    else:
        return validation_result
    
def validate_stage_value(promoted_stage, stage_value):
    if (promoted_stage == 2):
        if (stage_value not in (mncon.ODD, mncon.EVEN)):
            return "The stage_value can only be Odd or Even"
    elif (promoted_stage == 3):
        if (stage_value not in (mncon.MONDAY, mncon.TUESDAY, mncon.WEDNESDAY,\
                                mncon.THURSDAY, mncon.FRIDAY, mncon.SATURDAY,\
                                mncon.SUNDAY)):
            return "The stage_value must be a day in the week: Mon-Sun"
    elif (promoted_stage == 4):
        if (stage_value not in range(1,31)):
            return "The stage_value must be a day in the month: 1-31"
    return mncon.VALID

def update_memory_note(memory_note, promoted_stage, stage_value):
    memory_note_id = memory_note[0]
    note = memory_note[1]
    status = memory_note[2]
    category = memory_note[3]
    stage = memory_note[4]
    odd_even = memory_note[5]
    week_day = memory_note[6]
    month_day = memory_note[7]
    if (promoted_stage == 2):
        odd_even = stage_value
    if (promoted_stage == 3):
        week_day = stage_value
    if (promoted_stage == 4):
        month_day = stage_value
    mnc.update_memory_note(memory_note_id, note, status, category, promoted_stage, \
                           odd_even, week_day, month_day)    

# Review all memory notes for today
def retrieve_memory_notes_today(category):
    memory_notes_for_review = []
    memory_notes_stage_1 = retrieve_stage_1_memory_notes(category)
    memory_notes_stage_2 = retrieve_stage_2_memory_notes(category)
    memory_notes_stage_3 = retrieve_stage_3_memory_notes(category)
    memory_notes_stage_4 = retrieve_stage_4_memory_notes(category)
    
    if (len(memory_notes_stage_1) > 0):
        memory_notes_for_review.append(memory_notes_stage_1)
    if (len(memory_notes_stage_2) > 0):
        memory_notes_for_review.append(memory_notes_stage_2)
    if (len(memory_notes_stage_3) > 0):
        memory_notes_for_review.append(memory_notes_stage_3)
    if (len(memory_notes_stage_4) > 0):
        memory_notes_for_review.append(memory_notes_stage_4)
    return memory_notes_for_review
    
def retrieve_stage_1_memory_notes(category):
    stage = 1
    memory_notes = mnc.retrieve_memory_note_by_category_stage(category, stage)
    return memory_notes

#Odd Even days
def retrieve_stage_2_memory_notes(category):
    memory_notes_result = []
    stage = 2
    memory_notes = mnc.retrieve_memory_note_by_category_stage(category, stage)
    for memory_note in memory_notes:
        odd_even = memory_note[5]
        today = dt.now()
        today_day_value = today.day
        if (odd_even == mncon.ODD):
            if ((today_day_value % 2) > 0): #Odd number
                memory_notes_result.append(memory_note)
        elif (odd_even == mncon.EVEN):
            if ((today_day_value % 2) == 0): #Even number
                memory_notes_result.append(memory_note)
    return memory_notes_result

#Week days
def retrieve_stage_3_memory_notes(category):
    memory_notes_result = []
    stage = 3
    memory_notes = mnc.retrieve_memory_note_by_category_stage(category, stage)
    for memory_note in memory_notes:
        today = dt.now()
        today_week_day = today.weekday()
        if (today_week_day == 0 and memory_note[6] == mncon.MONDAY):
            memory_notes_result.append(memory_note)
        elif (today_week_day == 1 and memory_note[6] == mncon.TUESDAY):
            memory_notes_result.append(memory_note)
        elif (today_week_day == 2 and memory_note[6] == mncon.WEDNESDAY):
            memory_notes_result.append(memory_note)
        elif (today_week_day == 3 and memory_note[6] == mncon.THURSDAY):
            memory_notes_result.append(memory_note)
        elif (today_week_day == 4 and memory_note[6] == mncon.FRIDAY):
            memory_notes_result.append(memory_note)
        elif (today_week_day == 5 and memory_note[6] == mncon.SATURDAY):
            memory_notes_result.append(memory_note)
        elif (today_week_day == 6 and memory_note[6] == mncon.SUNDAY):
            memory_notes_result.append(memory_note)
    return memory_notes_result

#Month days
def retrieve_stage_4_memory_notes(category):
    memory_notes_result = []
    stage = 4
    memory_notes = mnc.retrieve_memory_note_by_category_stage(category, stage)
    for memory_note in memory_notes:
        today = dt.now()
        today_month_day = today.day
        if (memory_note[7] == str(today_month_day)):
            memory_notes_result.append(memory_note)
    return memory_notes_result
