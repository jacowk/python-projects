#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:19:54 2019

@author: jaco
"""

import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack()
r.mainloop() 

