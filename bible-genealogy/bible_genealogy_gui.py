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

        #Continue 1 Chron 2:50
        #https://www.askpython.com/python-modules/tkinter/tkinter-treeview-widget

        # data = bg.retrieve_json("genealogy-matthew.json")
        data = bg.retrieve_json("1chronicles_genealogy.json")
        # data = bg.retrieve_json("chronicles1_seir_genealogy.json")
        # data = bg.retrieve_json("test.json")
        # data = bg.retrieve_json("matthew1_genealogy.json")
        # data = bg.retrieve_json("luke3_genealogy.json")
        # data = bg.retrieve_json("genesis10_genealogy.json")
        #Remember the kings of Edom - requires a different JSON structure

        self.master.title("Bible Genealogy")
        self.pack()

        # Add Genealogy Selection Dropdown
        self.genealogy_selection = self.load_genealogy_selection()
        self.genealogy_selection_list = list(self.genealogy_selection.keys())
        self.genealogy_selection_combo = ttk.Combobox(self, width=20, values=self.genealogy_selection_list)
        self.genealogy_selection_combo.bind("<<ComboboxSelected>>", self.genealogy_selected)

        self._count = 1

        self.treeview = ttk.Treeview(self, selectmode = 'browse')
        self.treeview.config(height=30)
        self.treeview.pack(expand=YES, fill=BOTH)
        self.treeview.heading("#0", text="Genealogy")
        # By setting minwidth > width, and stretch=True, horizontal scrollbar works
        self.treeview.column("#0", minwidth=2560, width=1024, stretch=True)
        # Automatically expand all nodes on open
        self.treeview.bind('<<TreeviewOpen>>', self.handleOpenEvent)

        # Constructing horizontal scrollbar with treeview
        self.horizontal_scrollbar = ttk.Scrollbar(self,
                                                  orient="horizontal",
                                                  command=self.treeview.xview)
        # Configuring treeview
        self.treeview.configure(xscrollcommand=self.horizontal_scrollbar.set)

        #----------------------------------------------------------
        # Constructing vertical scrollbar with treeview
        self.vertical_scrollbar = ttk.Scrollbar(self,
                                                orient="vertical",
                                                command=self.treeview.yview)

        # Configuring treeview
        self.treeview.configure(yscrollcommand=self.vertical_scrollbar.set)

        #----------------------------------------------------------

        first_name = "{}_{}".format(data['name'], str(self._count))
        self._count = self._count + 1
        self.treeview.insert('', 'end', first_name, text=first_name)
        first_children = data['children']
        for child in first_children:
            self.add_item(first_name, child)

        # Place on grid
        self.treeview.grid(row=0, column=0)
        self.vertical_scrollbar.grid(row=0, column=2, rowspan=2, sticky=NS)
        self.horizontal_scrollbar.grid(row=1, column=0, columnspan=2, sticky=EW)
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