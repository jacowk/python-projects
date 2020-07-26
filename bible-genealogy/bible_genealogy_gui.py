#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat 25 July 2020

@author: Jaco Koekemoer

"""
from tkinter import *
from tkinter import ttk
import bible_genealogy_json as bg
import json

class BibleGenealogyGui(Frame):

    def __init__(self):
        Frame.__init__(self)

        Continue 2 Chron 2:46

        # data = bg.retrieve_json("genealogy-matthew.json")
        data = bg.retrieve_json("chronicles1_genealogy.json")
        # data = bg.retrieve_json("chronicles1_seir_genealogy.json")
        #Remember the kings of Edom - requires a different JSON structure

        self.master.title("Bible Genealogy")
        self.pack()

        # Add Genealogy Selection Dropdown
        self.genealogy_selection = self.load_genealogy_selection()
        self.genealogy_selection_list = list(self.genealogy_selection.keys())
        self.genealogy_selection_combo = ttk.Combobox(self, width=20, values=self.genealogy_selection_list)
        self.genealogy_selection_combo.bind("<<ComboboxSelected>>", self.genealogy_selected)

        self._count = 0

        self.treeview = ttk.Treeview(self)
        self.treeview.config(height=30)
        self.treeview.pack(expand=YES, fill=BOTH)
        self.treeview.heading("#0", text="Genealogy")
        self.treeview.column("#0", minwidth=1024, width=1024, stretch=NO)
        # Automatically expand all nodes on open
        self.treeview.bind('<<TreeviewOpen>>', self.handleOpenEvent)

        # Constructing vertical scrollbar with treeview
        horscrlbar = ttk.Scrollbar(self,
                                   orient="horizontal",
                                   command=self.treeview.xview)
        # Calling pack method w.r.to verical scrollbar
        horscrlbar.pack(side='right', fill='x')

        # Configuring treeview
        self.treeview.configure(yscrollcommand=horscrlbar.set)

        first_name = "{}_{}".format(data['name'], str(self._count))
        self._count = self._count + 1
        self.treeview.insert('', 'end', first_name, text=first_name)
        first_children = data['children']
        for child in first_children:
            self.add_item(first_name, child)

        #self.treeview.insert('', '0', 'item1', text = "First Item")
        #self.treeview.insert('', '1', 'item2', text="Second Item")
        #self.treeview.insert('', 'end', 'item3', text="Third Item")
        #self.treeview.insert('item2', 'end', 'item4', text="Fourth Item")

        # Place on grid
        #self.treeview.grid(row=0,column=0)
        #self.genealogy_selection_combo.grid(row=1, column=0)

    def add_item(self, parent_name, item):
        name = item['name']
        name = "{}_{}".format(name, str(self._count))
        self._count = self._count + 1
        self.treeview.insert(parent_name, 'end', name, text=name)

        try:
            children = item['children']
            for child in children:
                self.add_item(name, child)
        except:
            print("No children for {}".format(name))

    def open_children(self, parent):
        self.treeview.item(parent, open=True)
        for child in self.treeview.get_children(parent):
            self.open_children(child)

    def handleOpenEvent(self, event):
        self.open_children(self.treeview.focus())

    def load_genealogy_selection(self):
        filename = "genealogy_selection.json"
        try:
            f = open(filename, 'r')
            json_raw_data = f.read()
            json_data = json.loads(json_raw_data)
            return json_data
        except Exception as e:
            print(str(e))
            print("File could not be opened")

    def genealogy_selected(self, select_event):
        filename = "genealogy_selection.json"
        geneology_selections = json.loads(open(filename, 'r').read())
        selected = self.genealogy_selection_combo.get()
        self.genealogy_selected_item = geneology_selections[selected]
        print(self.genealogy_selected_item)

def main():
    bible_genealogy_gui = BibleGenealogyGui()
    bible_genealogy_gui.mainloop()

main()