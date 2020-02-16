#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:21:09 2019

@author: jaco
"""


from tkinter import *
master = Tk() 
w = Canvas(master, width=40, height=60) 
w.pack() 
canvas_height=20
canvas_width=200
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop() 
