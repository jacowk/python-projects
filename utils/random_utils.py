#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:43:57 2020

@author: jaco

http://archive.canonical.com/pool/partner/a/adobe-flashplugin/adobe-flashplugin_20200114.1.orig.tar.gz
https://www.tutorialspoint.com/python/file_writelines.htm
"""
import random

def generate_value_list():
    return range(5000000001, 5000001000)
    
def generate_random_list(cnt):
    random_numbers = []
    for x in range(1,cnt):
        random_value = random.randint(5000000001, 5999999999)
        random_numbers.append(str(random_value))
    return random_numbers

def write_list_to_file(list, filename):
    file = open(filename, 'a')
    file.writelines(list)
    #for value in list:
    #    file.write(str(value) + '\n')
    file.close()
    
def read_file_list(filename):
    input_list = []
    with open(filename) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            input_list.append(str(line))
            line = fp.readline()
            cnt += 1
    return input_list

'''
Use this to read a file with only a column of numbers
'''
def read_file(filename):
    file = open(filename, 'r')
    input_list = file.readlines() # Read all lines
    return input_list

'''
Not tested
'''
def read_file_b(filename):
    with open('file') as f:
        w, h = [int(x) for x in next(f).split()]
        array = [[int(x) for x in line.split()] for line in f]

def make_comma_separated(list_value):
    for value in list_value:
        print(value)
    

#value_list = generate_value_list()
random_list = generate_random_list(100)
print(random_list)
write_list_to_file(random_list, 'value_list.txt')
#input_list = read_file('random_list.txt')
#for value in input_list:
    #print(value)

