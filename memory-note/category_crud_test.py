#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:38:20 2020

@author: jaco
"""
import category_crud as cc

def test_insert_category():
    description = "Category Test Case 1"
    status = 2
    cc.insert_category(description, status)
    result = cc.retrieve_all_categories()
    for item in result:
        print(item)
        
def test_retrieve_all_categories():
    print("Running test_retrieve_all_categories")
    result = cc.retrieve_all_categories()
    for item in result:
        print(item)

def test_retrieve_category_by_id():
    print("Running test_retrieve_category_by_id")
    result = cc.retrieve_category_by_id(4)
    print(result)

def test_update_category():
    print("Running test_update_category")
    category_id = 4
    description = "Category Test Case 2"
    status = 2
    cc.update_category(category_id, description, status)
    result = cc.retrieve_category_by_id(category_id)
    print(result)
    
def test_delete_category():
    print("Running test_delete_category")
    category_id = 4
    cc.delete_category(category_id)
    result = cc.retrieve_category_by_id(category_id)
    print(result)

#test_insert_category()
#test_retrieve_all_categories()
#test_retrieve_category_by_id()
#test_update_category()
#test_delete_category()

