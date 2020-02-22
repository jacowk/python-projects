#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:54:18 2020

@author: jaco
"""

from tkinter import *

class LabelDemo(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        
        self.master.title("Label Demo")
        self.grid()
        self._label1 = Label(self, width=20, height=10, background="blue")
        self._label2 = Label(self, width=20, height=10, background="red")
        self._label3 = Label(self, width=40, height=10, background="green")
        
        self._label1.grid(row=0, column=0)
        self._label2.grid(row=0, column=1)
        self._label3.grid(row=1, column=0, columnspan=2)
        
        
        self._label10 = Label(self, width=5, height=10, background="black", justify="left")
        self._label11 = Label(self, width=5, height=10, background="yellow")
        self._label12 = Label(self, width=5, height=10, background="black")
        self._label13 = Label(self, width=5, height=10, background="yellow")
        
        self._label10.grid(row=2, column=0)
        self._label11.grid(row=2, column=1)
        self._label12.grid(row=2, column=2)
        self._label13.grid(row=2, column=3)
        
def main():
    LabelDemo().mainloop()

main()
