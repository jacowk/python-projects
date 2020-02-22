#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:27:53 2020

@author: jaco
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:54:18 2020

@author: jaco
"""

from tkinter import *

class HebrewLettersGui(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        
        widget_width = 80
        text_area_height = 15
        
        self.master.title("Hebrew Letters")
        self.pack()
        self._pictographs_label = Label(self, width=widget_width, height=1, text="Hebrew Pictographs")
        self._geomatria_label = Label(self, width=widget_width, height=1, text="Hebrew Geomatria")
        self._totals_label = Label(self, width=widget_width, height=1, text="Letter Number Totals")
        self._divisibles_label = Label(self, width=widget_width, height=1, text="Letter Number Divisibles")
        
        self._pictographs_text = Text(self, width=widget_width, height=text_area_height)
        self._geomatria_text = Text(self, width=widget_width, height=text_area_height)
        self._totals_text = Text(self, width=widget_width, height=text_area_height)
        self._divisibles_text = Text(self, width=widget_width, height=text_area_height)
        
        self._letter_names_label = Label(self, width=int(widget_width/2), height=1, text="Hebrew Letter Names")
        self._letter_names_text = Text(self, width=int(widget_width/2), height=text_area_height)
        
        self._hebrew_input = StringVar()
        self._keyboard_input = Entry(self, textvariable=self._hebrew_input, width=widget_width)
        self._keyboard_label = Label(self, width=widget_width, height=text_area_height, text="Keyboard Placeholder")
        
        self._empty_label = Label(self, width=int(widget_width/2), height=21, text="Placeholder")
        
        self._pictographs_label.grid(row=0, column=0, columnspan=2)
        self._geomatria_label.grid(row=0, column=2, columnspan=2)
        
        self._pictographs_text.grid(row=1, column=0, columnspan=2)
        self._geomatria_text.grid(row=1, column=2, columnspan=2)
        
        self._totals_label.grid(row=2, column=0, columnspan=2)
        self._divisibles_label.grid(row=2, column=2, columnspan=2)
        
        self._totals_text.grid(row=3, column=0, columnspan=2)
        self._divisibles_text.grid(row=3, column=2, columnspan=2)
        
        self._letter_names_label.grid(row=4, column=0)
        self._letter_names_text.grid(row=5, column=0)
        
        self._keyboard_input.grid(row=4, column=1, columnspan=2)
        #self._keyboard_label.grid(row=5, column=1, columnspan=2)
        
        self._empty_label.grid(row=4, column=3, rowspan=2)
        
        #Keyboard Frame
        self._keyboard_frame = Frame(self, width=widget_width, height=text_area_height)
        self._keyboard_frame.grid(row=5, column=1, columnspan=2)
        
        self._alef_button = Button(self._keyboard_frame, text="Alef")
        self._bet_button = Button(self._keyboard_frame, text="Bet")
        
        self._alef_button.grid()
        self._bet_button.grid()
        
        
def main():
    HebrewLettersGui().mainloop()

main()
