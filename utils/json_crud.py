#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:57:04 2020

@author: jaco

Perform CRUD operations of a JSON file

{
     topic: 
         [
           "Test 1": {
             "date_created": 2020-01-01,
             "category": "Category 1"
             "subject": "Test 1",
             "description": "Testing this subject" }
         ],
         [
           "Test 1": {
             "date_created": 2020-01-01,
             "category": "Category 1"
             "subject": "Test 1",
             "description": "Testing this subject" }
         ]
}
"""
import json
import os
from datetime import datetime

def validate_topic_directory(topic):
    print("Validating topic")
    if not os.path.isdir(topic):
        os.mkdir(topic)

def create_json(topic):
    print("Creating")
    
    # Accept user input
    new_dict_data = {}
    category = input("Enter category: ")
    subject = input("Enter subject: ")
    description = input("Enter description: ")
    new_dict_data[subject] = {
            "category": category,
            "subject": subject,
            "description": description
    }
    return new_dict_data
    

def retrieve_json(topic):
    print("Retrieving")
    #Read file
    json_filename = topic + ".json"
    try:
        f = open(json_filename, 'r')
        json_raw_data = f.read()
        json_data = json.loads(json_raw_data)   
        return json_data
    except Exception:
        print("File could not be opened")
    
def update_json(subject_list):
    print("Updating")
    for subject_dict in subject_list:
        for key in list(subject_dict.keys()):
            print(key)
    update_key = input("Enter key to update: ")
    update_value = input("Enter new value: ")
    for subject_dict in subject_list:
        if update_key in subject_dict:
            item_dict = subject_dict[update_key]
            item_dict['description'] = update_value
    return subject_list
    
def delete_json(subject_list):
    print("Deleting")
    for subject_dict in subject_list:
        for key in list(subject_dict.keys()):
            print(key)
    delete_key = input("Enter key to delete: ")
    cnt = 0
    for subject_dict in subject_list:
        if delete_key in subject_dict:
            break
        cnt += 1
    subject_list.pop(cnt)            
    return subject_list

def loop_json(subject_list):
    print("Looping")
    for subject_dict in subject_list:
        for key in list(subject_dict.keys()):
            item_dict = subject_dict[key]
            print("Category: ", item_dict['category'])
            print("Subject: ", item_dict['subject'])
            print("Description: ", item_dict['description'])
            input("Press enter for next...")
        
def save_json(topic, json_data):
    print("Saving")
    json_format = json.dumps(json_data)
    json_filename = topic + ".json"
    f = open(json_filename, 'w')
    f.write(json_format)
    