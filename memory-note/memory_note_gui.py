#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 08:58:55 2020

@author: jaco

Database: MemoryNote
Table:
    memory-note:
        id long primary key
        note textblob - The piece of info you want to remember
        category (Scripture, Vocabulary) long - Possible values (Foreign key to category table)
        stage long - Possible values (1-4)
        odd_even varchar(4) - Possible values (Odd or Even)
        week_day varchar(10) - Possible values (Sun to Sat)
        month_day long - Possible values (1-31)
    
    category:
        id
        description
        
Use Cases
    review-note (CRUD)
    category (CRUD)
    start review for a category
    promote to next stage (1 - Review daily, 2 - Review odd or even days, 
                           3 - Review once a week, 4 - Review once a month)
    view all for a category, order by stage
    view stats per stage
"""
from tkinter import *
import tkinter.ttk as ttk # For the Combobox
import tkinter.scrolledtext as scrolledtext

class MemoryNoteGui(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        
        widget_width = 80
        pad_x = 5
        pad_y = 5
        font_name = "Helvetica"
        font_size = 10
        
        self.master.title("Memory Notes")
        self.pack()
        
        self._mem_note_id_label = Label(self, width=widget_width, height=1, text="id")
        self._mem_note_note_label = Label(self, width=widget_width, height=1, text="Note")
        
        
        
