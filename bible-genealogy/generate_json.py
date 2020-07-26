#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun 26 July 2020

@author: Jaco Koekemoer

"""
no_of_tabs = 30

def generate_tabs(no_of_tabs):
    return "\t" * no_of_tabs

def generate_names(no_of_tabs):
    values = [ "Korah", "Tappuah", "Rekem", "Shema" ]
    for value in values:
        print("{}{{ \"name\": \"{}\", \"children\": [] }},".format(generate_tabs(no_of_tabs),value))

generate_names(no_of_tabs)

