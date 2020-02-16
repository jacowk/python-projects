#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:33:38 2020

@author: jaco
"""
import os
filename = "deletefile.txt"
f = open(filename, "w")

# Delete the file
#os.remove(filename)

# Check if the file exists
if os.path.exists(filename):
  os.remove(filename)
else:
  print("The file does not exist")
  
# Remove a directory
#os.rmdir("myfolder")
  