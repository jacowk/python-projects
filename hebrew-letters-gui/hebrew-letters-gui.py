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
import json

class HebrewLettersGui(Frame):
    
    hebrew_input_expression = ""
    
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
        self._letter_names_label = Label(self, width=int(widget_width/2), height=1, text="Hebrew Letter Names")
        
        self._pictographs_text = Text(self, width=widget_width, height=text_area_height)
        self._geomatria_text = Text(self, width=widget_width, height=text_area_height)        
        self._totals_text = Text(self, width=widget_width, height=text_area_height)
        self._divisibles_text = Text(self, width=widget_width, height=text_area_height)
        self._letter_names_text = Text(self, width=int(widget_width/2), height=text_area_height)
        
        self._hebrew_input = StringVar()
        self._keyboard_input = Entry(self, textvariable=self._hebrew_input, width=widget_width)
        self._keyboard_label = Label(self, width=widget_width, height=text_area_height, text="Keyboard Placeholder")
        
        self._empty_label = Label(self, width=int(widget_width/2), height=21, text="Placeholder")
        
        # Place on grid
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
        
        rowa = ['qof','resh','alef','tet','vav','nun_final','mem_final','pe']
        rowb = ['shin','dalet','gimel','kaf','ayin','yod','chet','lamed','kaf_final','pe_final']
        rowc = ['zayin','samech','bet','he','nun','mem','tsade','tav','tsade_final']
        
        hebrew_unicode = json.loads(open('hebrew-unicode.json', 'r').read())
        
        ########## Row One #############
        #Qof button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['qof'] + "\n\nQof", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['qof']))
        self._letter_button.grid(row=0, column=0)
        
        #Resh button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['resh'] + "\n\nResh", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['resh']))
        self._letter_button.grid(row=0, column=1)
        
        #Alef button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['alef'] + "\n\nAlef", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['alef']))
        self._letter_button.grid(row=0, column=2)
        
        #Tet button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['tet'] + "\n\nTest", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['tet']))
        self._letter_button.grid(row=0, column=3)
        
        #Vav button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['vav'] + "\n\nVav", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['vav']))
        self._letter_button.grid(row=0, column=4)
        
        #Final Nun button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['nun_final'] + "\n\nFinal\nNun", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['nun_final']))
        self._letter_button.grid(row=0, column=5)
        
        #Final Mem button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['mem_final'] + "\n\nFinal\nMem", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['mem_final']))
        self._letter_button.grid(row=0, column=6)
        
        #Pe button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['pe'] + "\n\nPe", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['pe']))
        self._letter_button.grid(row=0, column=7)
        
        #Enter button
        self._enter_button = Button(self._keyboard_frame, text='Enter', command=self.press_enter_button)
        self._enter_button.grid(row=2, column=9, columnspan=2)
        
        ########## Row Two #############
        
        #Shin button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['shin'] + "\n\nShin", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['shin']))
        self._letter_button.grid(row=1, column=0)
        
        #Dalet button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['dalet'] + "\n\nDalet", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['dalet']))
        self._letter_button.grid(row=1, column=1)
        
        #Gimel button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['gimel'] + "\n\nGimel", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['gimel']))
        self._letter_button.grid(row=1, column=2)
        
        #Kaf button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['kaf'] + "\n\nKaf", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['kaf']))
        self._letter_button.grid(row=1, column=3)
        
        #Ayin button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['ayin'] + "\n\nAyin", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['ayin']))
        self._letter_button.grid(row=1, column=4)
        
        #Yod button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['yod'] + "\n\nYod", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['yod']))
        self._letter_button.grid(row=1, column=5)
        
        #Chet button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['chet'] + "\n\nChet", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['chet']))
        self._letter_button.grid(row=1, column=6)
        
        #Lamed button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['lamed'] + "\n\nLamed", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['lamed']))
        self._letter_button.grid(row=1, column=7)
        
        #Kaf Final button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['kaf_final'] + "\n\nFinal\nKaf", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['kaf_final']))
        self._letter_button.grid(row=1, column=8)
        
        #Pe Final button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['pe_final'] + "\n\nFinal\nPe", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['pe_final']))
        self._letter_button.grid(row=1, column=9)
        
        ########## Row Three #############
        
        #Zayin button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['zayin'] + "\n\nZayin", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['zayin']))
        self._letter_button.grid(row=2, column=0)
        
        #Samech button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['samech'] + "\n\nSamech", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['samech']))
        self._letter_button.grid(row=2, column=1)
        
        #Bet button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['bet'] + "\n\nBet", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['bet']))
        self._letter_button.grid(row=2, column=2)
        
        #He button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['he'] + "\n\nHe", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['he']))
        self._letter_button.grid(row=2, column=3)
        
        #Nun button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['nun'] + "\n\nNun", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['nun']))
        self._letter_button.grid(row=2, column=4)
        
        #Mem button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['mem'] + "\n\nMem", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['mem']))
        self._letter_button.grid(row=2, column=5)
        
        #Tsade button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['tsade'] + "\n\nTsade", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['tsade']))
        self._letter_button.grid(row=2, column=6)
        
        #Tav button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['tav'] + "\n\nTav", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['tav']))
        self._letter_button.grid(row=2, column=7)
        
        #Tsade Final button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['tsade_final'] + "\n\nFinal\nTsade", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['tsade_final']))
        self._letter_button.grid(row=2, column=8)
    
    def press_letter_button(self, letter):
        global hebrew_input_expression
        self.hebrew_input_expression += letter
        self._hebrew_input.set(self.hebrew_input_expression)
        
    def press_enter_button(self):
        # Load all JSON
        hebrew_numbers = json.loads(open('hebrew-numbers.json', 'r').read())
        hebrew_pict = json.loads(open('hebrew-pictographs.json', 'r').read())
        hebrew_unicode = json.loads(open('hebrew-unicode.json', 'r').read())
        hebrew_acc = json.loads(open('hebrew-accepted-input.json', 'r').read())
        number_meanings = json.loads(open('number-meanings.json', 'r').read())
    
        self.process_letter_names()
        self.process_pictographs()
        self.process_geomatria()
        self.process_letter_totals()
        self.process_divisibles()
        
    # Process letter names
    def process_letter_names(self):
        self._letter_names_text.delete("1.0", END) # Clear text
        
        self._letter_names_text.insert("1.0", self.hebrew_input_expression)
    
    # Process pictographs
    def process_pictographs(self):
        self._pictographs_text.delete("1.0", END) # Clear text
        self._pictographs_text.insert("1.0", "TODO")
    
    # Process geomatria
    def process_geomatria(self):
        self._geomatria_text.delete("1.0", END) # Clear text
        self._geomatria_text.insert("1.0", "TODO")
    
    # Process letter totals
    def process_letter_totals(self):
        self._totals_text.delete("1.0", END) # Clear text
        self._totals_text.insert("1.0", "TODO")
    
    # Process divisibles
    def process_divisibles(self):
        self._divisibles_text.delete("1.0", END) # Clear text
        self._divisibles_text.insert("1.0", "TODO")

def main():
    HebrewLettersGui().mainloop()

main()


"""
U+05D0	א	Hebrew Letter Alef
U+05D1	ב	Hebrew Letter Bet
U+05D2	ג	Hebrew Letter Gimel
U+05D3	ד	Hebrew Letter Dalet
U+05D4	ה	Hebrew Letter He
U+05D5	ו	Hebrew Letter Vav
U+05D6	ז	Hebrew Letter Zayin
U+05D7	ח	Hebrew Letter Het
U+05D8	ט	Hebrew Letter Tet
U+05D9	י	Hebrew Letter Yod
U+05DA	ך	Hebrew Letter Final Kaf
U+05DB	כ	Hebrew Letter Kaf
U+05DC	ל	Hebrew Letter Lamed
U+05DD	ם	Hebrew Letter Final Mem
U+05DE	מ	Hebrew Letter Mem
U+05DF	ן	Hebrew Letter Final Nun
U+05E0	נ	Hebrew Letter Nun
U+05E1	ס	Hebrew Letter Samekh
U+05E2	ע	Hebrew Letter Ayin
U+05E3	ף	Hebrew Letter Final Pe
U+05E4	פ	Hebrew Letter Pe
U+05E5	ץ	Hebrew Letter Final Tsadi
U+05E6	צ	Hebrew Letter Tsadi
U+05E7	ק	Hebrew Letter Qof
U+05E8	ר	Hebrew Letter Resh
U+05E9	ש	Hebrew Letter Shin
U+05EA	ת	Hebrew Letter Tav
"""
