#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun 26 July 2020

@author: Jaco Koekemoer

"""
import json
no_of_tabs = 0

def generate_tabs(no_of_tabs):
    return "\t" * no_of_tabs

def generate_names(no_of_tabs):
    values = add_quotes("Ahumai, Lahad")
    for value in values:
        print("{}{{ \"name\": \"{}\", \"children\": [] }},".format(generate_tabs(no_of_tabs),value))

def create_dict(name):
    branch = {}
    branch["name"] = name
    branch["children"] = list()
    return branch

def generate_tree():
    names = add_quotes("Jeconiah, Zedekiah")
    dict_list = []
    for name in names:
        branch = create_dict(name)
        dict_list.append(branch)

    tree = dict()
    for dictionary in reversed(dict_list):
        dictionary["children"].append(tree)
        tree = dictionary
    data = json.dumps(tree, indent=2)
    print(data)

def add_quotes(string):
    #string = "Elishah, Tarshish, Kittim, Dodanim"
    values = string.split(", ")
    return values

#add_quotes()
generate_names(no_of_tabs)
#generate_tree()


