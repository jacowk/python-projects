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
        
        widget_width = 20
        pad_x = 5
        pad_y = 5
        font_name = "Helvetica"
        font_size = 10
        
        self.master.title("Memory Notes")
        self.pack()
        
        #############################################################
        self._mem_note_search_label = Label(self, width=widget_width, height=1, text="Search Memory Notes")
        self._mem_note_id_label = Label(self, width=widget_width, height=1, text="ID")
        self._mem_note_category_label = Label(self, width=widget_width, height=1, text="Category")
        self._mem_note_status_label = Label(self, width=widget_width, height=1, text="Status")
        
        # ID Input
        self._id_input = StringVar()
        self._id_entry = Entry(self, textvariable=self._id_input, width=widget_width, font=(font_name, font_size))
        
        # Category Dropdown
        self._category_list = ["Scriptures","Vocabulary"]
        self._category_combo = ttk.Combobox(self, width=widget_width, 
                                            values=self._category_list, font=(font_name, font_size))
        self._category_combo.bind("<<ComboboxSelected>>", self.category_selected)
        
        # Status Dropdown
        self._status_list = ["Pending","Active","Deleted"]
        self._status_combo = ttk.Combobox(self, width=widget_width, 
                                            values=self._status_list, font=(font_name, font_size))
        self._status_combo.bind("<<ComboboxSelected>>", self.status_selected)
        
        #############################################################
        
        # Search button
        self._search_button = Button(self, text="Search", 
                                     command=lambda: self.press_search_button())
        self._search_button.grid(row=2, column=2)
        
        #############################################################
        # Grid
        self._mem_note_search_label.grid(row=0, column=0, columnspan=6, padx=pad_x, pady=pad_y)
        self._mem_note_id_label.grid(row=1, column=0, padx=pad_x, pady=pad_y)
        self._id_entry.grid(row=1, column=1, padx=pad_x, pady=pad_y)
        
        self._mem_note_category_label.grid(row=1, column=2, padx=pad_x, pady=pad_y)
        self._category_combo.grid(row=1, column=3, padx=pad_x, pady=pad_y)
        
        self._mem_note_status_label.grid(row=1, column=4, padx=pad_x, pady=pad_y)
        self._status_combo.grid(row=1, column=5, padx=pad_x, pady=pad_y)
        
    def category_selected(self, select_event):
        self._selected_category = self._category_combo.get()
        
    def status_selected(self, select_event):
        self._selected_status = self._status_combo.get()
        
    def press_search_button(self):
        print("ID: %s" % self._id_input)
        print("Category: %s" % self._selected_category)
        print("Status: %s" % self._selected_status)
        
def main():
    print("Hello world")
    memory_note_gui = MemoryNoteGui()
    memory_note_gui.mainloop()

main()

