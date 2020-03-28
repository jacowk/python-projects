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

Pictographs and Mnemonics
-------------------------
https://www.studylight.org/lexicons/hebrew/ahl_alphabet.html

Python Hebrew Dates:
-------------------------
https://stackoverflow.com/questions/15042200/hebrew-calendar-in-python
https://pypi.org/project/hebcal/
http://www.david-greve.de/luach-code/jewish-python.html
https://github.com/topics/hebrew-calendar
https://pypi.org/project/convertdate/
https://sourceforge.net/projects/pythondateutil/
https://www.hebcal.com/home/195/jewish-calendar-rest-api

Hebrew Names to play with:
-------------------------
https://www.behindthename.com/names/usage/biblical-hebrew
"""

from tkinter import *
import tkinter.ttk as ttk # For the Combobox
import tkinter.scrolledtext as scrolledtext
import json
from convertdate import hebrew

class HebrewLettersGui(Frame):
    
    hebrew_input_expression = ""
    
    def __init__(self):
        Frame.__init__(self)
        
        widget_width = 80
        text_area_height = 15
        pad_x = 5
        pad_y = 5
        font_name = "Helvetica"
        font_size = 10
        
        self.master.title("Hebrew Letters")
        self.pack()
        
        hebrew_date = self.process_hebrew_dates()
        self._hebrew_date_label = Label(self, width=widget_width, height=1, text=hebrew_date)
        
        self._pictographs_label = Label(self, width=widget_width, height=1, text="Hebrew Pictographs and Mnemonics")
        self._geomatria_label = Label(self, width=widget_width, height=1, text="Hebrew Geomatria")
        self._totals_label = Label(self, width=widget_width, height=1, text="Hebrew Dates")
        self._divisibles_label = Label(self, width=widget_width, height=1, text="Letter Number Divisibles")
        self._letter_names_label = Label(self, width=int(widget_width/2), height=1, text="Hebrew Letter Names")
        
        self._pictographs_text = scrolledtext.ScrolledText(self, width=widget_width, height=text_area_height*2+1, padx=pad_x, pady=pad_y, font=(font_name, font_size))
        self._geomatria_text = scrolledtext.ScrolledText(self, width=widget_width, height=text_area_height, padx=pad_x, pady=pad_y, font=(font_name, font_size))
        self._divisibles_text = scrolledtext.ScrolledText(self, width=widget_width, height=text_area_height, padx=pad_x, pady=pad_y, font=(font_name, font_size))
        self._letter_names_text = scrolledtext.ScrolledText(self, width=int(widget_width/2), height=text_area_height, padx=pad_x, pady=pad_y, font=(font_name, font_size))
        
        self._hebrew_input = StringVar()
        self._keyboard_input = Entry(self, justify=RIGHT, textvariable=self._hebrew_input, width=widget_width, font=(font_name, font_size))
        self._keyboard_label = Label(self, width=widget_width, height=text_area_height, text="Keyboard Placeholder")

        # Hebrew Names Combobox
        self.hebrew_names = load_hebrew_names()
        self.hebrew_name_list = list(self.hebrew_names.keys())
        self.hebrew_name_list_sorted = sorted(self.hebrew_name_list)
        self._hebrew_names_combo = ttk.Combobox(self, width=widget_width, values=self.hebrew_name_list_sorted, font=(font_name, font_size))
        self._hebrew_names_combo.bind("<<ComboboxSelected>>", self.hebrew_name_selected)
        #self._hebrew_names_result_text = StringVar()
        #self._hebrew_names_result_text.set("Select a name")
        #self._hebrew_names_result = Entry(self, text=self._hebrew_names_result_text)
        
        # Configs
        self._pictographs_text.config(wrap=WORD)
        self._geomatria_text.config(wrap=WORD)
        self._divisibles_text.config(wrap=WORD)
        self._letter_names_text.config(wrap=WORD)
        
        # Place on grid
        self._hebrew_date_label.grid(row=0, column=0, columnspan=4, padx=pad_x, pady=pad_y)
        self._pictographs_label.grid(row=1, column=0, columnspan=2)
        self._geomatria_label.grid(row=1, column=2, columnspan=2)
        self._pictographs_text.grid(row=2, column=0, columnspan=2, rowspan=3, padx=pad_x, pady=pad_y)
        self._geomatria_text.grid(row=2, column=2, columnspan=2, padx=pad_x, pady=pad_y)
        self._divisibles_label.grid(row=3, column=2, columnspan=2)        
        self._divisibles_text.grid(row=4, column=2, columnspan=2, padx=pad_x, pady=pad_y)
        self._letter_names_label.grid(row=5, column=0)
        self._hebrew_names_combo.grid(row=5, column=1, columnspan=2, padx=pad_x, pady=pad_y)
        #self._hebrew_names_result.grid(row=5, column=3)
        self._keyboard_input.grid(row=6, column=1, columnspan=2, padx=pad_x, pady=pad_y)
        self._letter_names_text.grid(row=6, column=0, rowspan=2, padx=pad_x, pady=pad_y)
        
        #Keyboard Frame
        self._keyboard_frame = Frame(self, width=widget_width, height=text_area_height)
        self._keyboard_frame.grid(row=7, column=1, columnspan=3, padx=pad_x, pady=pad_y)
        
        
        self._save_button = Button(self._keyboard_frame, text="Save Hebrew Word", \
                                     command=lambda: self.save_hebrew_word())
        self._save_button.grid(row=8, column=0)
        
        rowa = ['quph','resh','aleph','tet','waw','nun_final','mem_final','pey']
        rowb = ['shin','dalet','gimel','kaph','ayin','yod','chet','lamed','kaph_final','pey_final']
        rowc = ['zayin','samech','beyt','hey','nun','mem','tsade','taw','tsade_final']
        
        hebrew_unicode = json.loads(open('hebrew-unicode.json', 'r').read())
        
        ########## Row One #############
        #Quph button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['quph'] + "\n\nQuph 100", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['quph']))
        self._letter_button.grid(row=0, column=0)
        
        #Resh button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['resh'] + "\n\nResh 200", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['resh']))
        self._letter_button.grid(row=0, column=1)
        
        #Aleph button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['aleph'] + "\n\nAleph 1", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['aleph']))
        self._letter_button.grid(row=0, column=2)
        
        #Tet button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['tet'] + "\n\nTet 9", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['tet']))
        self._letter_button.grid(row=0, column=3)
        
        #Waw button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['waw'] + "\n\nWaw 6", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['waw']))
        self._letter_button.grid(row=0, column=4)
        
        #Final Nun button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['nun_final'] + "\n\nFinal\nNun 50", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['nun_final']))
        self._letter_button.grid(row=0, column=5)
        
        #Final Mem button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['mem_final'] + "\n\nFinal\nMem 40", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['mem_final']))
        self._letter_button.grid(row=0, column=6)
        
        #Pey button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['pey'] + "\n\nPey 80", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['pey']))
        self._letter_button.grid(row=0, column=7)
        
        #Clear button
        self._letter_button = Button(self._keyboard_frame, text='Clear', \
                                     command=self.press_clear_button)
        self._letter_button.grid(row=0, column=8)
        
        #Enter button
        self._enter_button = Button(self._keyboard_frame, text='Enter', command=self.press_enter_button)
        self._enter_button.grid(row=2, column=9, columnspan=2)
        
        ########## Row Two #############
        
        #Shin button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['shin'] + "\n\nShin 300", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['shin']))
        self._letter_button.grid(row=1, column=0)
        
        #Dalet button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['dalet'] + "\n\nDalet 4", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['dalet']))
        self._letter_button.grid(row=1, column=1)
        
        #Gimel button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['gimel'] + "\n\nGimel 3", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['gimel']))
        self._letter_button.grid(row=1, column=2)
        
        #Kaph button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['kaph'] + "\n\nKaph 20", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['kaph']))
        self._letter_button.grid(row=1, column=3)
        
        #Ayin button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['ayin'] + "\n\nAyin 70", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['ayin']))
        self._letter_button.grid(row=1, column=4)
        
        #Yod button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['yod'] + "\n\nYod 10", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['yod']))
        self._letter_button.grid(row=1, column=5)
        
        #Chet button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['chet'] + "\n\nChet 8", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['chet']))
        self._letter_button.grid(row=1, column=6)
        
        #Lamed button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['lamed'] + "\n\nLamed 30", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['lamed']))
        self._letter_button.grid(row=1, column=7)
        
        #Kaph Final button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['kaph_final'] + "\n\nFinal\nKaph 20", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['kaph_final']))
        self._letter_button.grid(row=1, column=8)
        
        #Pey Final button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['pey_final'] + "\n\nFinal\nPey 80", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['pey_final']))
        self._letter_button.grid(row=1, column=9)
        
        ########## Row Three #############
        
        #Zayin button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['zayin'] + "\n\nZayin 7", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['zayin']))
        self._letter_button.grid(row=2, column=0)
        
        #Samech button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['samech'] + "\n\nSamech 60", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['samech']))
        self._letter_button.grid(row=2, column=1)
        
        #Beyt button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['beyt'] + "\n\nBeyt 2", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['beyt']))
        self._letter_button.grid(row=2, column=2)
        
        #Hey button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['hey'] + "\n\nHey 5", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['hey']))
        self._letter_button.grid(row=2, column=3)
        
        #Nun button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['nun'] + "\n\nNun 50", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['nun']))
        self._letter_button.grid(row=2, column=4)
        
        #Mem button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['mem'] + "\n\nMem 40", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['mem']))
        self._letter_button.grid(row=2, column=5)
        
        #Tsade button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['tsade'] + "\n\nTsade 90", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['tsade']))
        self._letter_button.grid(row=2, column=6)
        
        #Taw button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['taw'] + "\n\nTaw 400", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['taw']))
        self._letter_button.grid(row=2, column=7)
        
        #Tsade Final button
        self._letter_button = Button(self._keyboard_frame, text=hebrew_unicode['tsade_final'] + "\n\nFinal\nTsade 90", \
                                     command=lambda: self.press_letter_button(hebrew_unicode['tsade_final']))
        self._letter_button.grid(row=2, column=8)
        
        # Methods called on startup
        self.process_hebrew_dates()
    
    def hebrew_name_selected(self, select_event):
        hebrew_letter_names = json.loads(open('hebrew-letter-names.json', 'r').read())
        hebrew_letter_list = list(hebrew_letter_names.keys())
        selected = self._hebrew_names_combo.get()
        hebrew_name = self.hebrew_names[selected]
        hebrew_name_scrubbed = ""
        # Eliminate vowels
        for letter in hebrew_name:
            if letter in hebrew_letter_list:
                hebrew_name_scrubbed = letter + hebrew_name_scrubbed # Reading right to left
        #self._hebrew_names_result_text.set(hebrew_name_scrubbed)
        self.hebrew_input_expression = hebrew_name_scrubbed
        self._hebrew_input.set(self.hebrew_input_expression)
    
    def press_letter_button(self, letter):
        global hebrew_input_expression
        self.hebrew_input_expression = letter + self.hebrew_input_expression
        self._hebrew_input.set(self.hebrew_input_expression)
        
    def press_enter_button(self):
        # Load all JSON
        hebrew_numbers = json.loads(open('hebrew-numbers.json', 'r').read())
        hebrew_pictographs = json.loads(open('hebrew-pictographs.json', 'r').read())
        hebrew_mnemonics = json.loads(open('hebrew-mnemonics.json', 'r').read())
        hebrew_unicode = json.loads(open('hebrew-unicode.json', 'r').read())
        hebrew_letter_names = json.loads(open('hebrew-letter-names.json', 'r').read())
        number_meanings = json.loads(open('number-meanings.json', 'r').read())
    
        self.process_letter_names(hebrew_letter_names)
        self.process_pictographs(hebrew_pictographs, hebrew_letter_names, hebrew_mnemonics)
        self.process_geomatria(hebrew_numbers, number_meanings, hebrew_letter_names)
        self.process_divisibles(hebrew_numbers, number_meanings, hebrew_letter_names)
    
    def press_clear_button(self):
        self._hebrew_input.set('')
        self.hebrew_input_expression = ''
        self._keyboard_input.delete(0, 'end')
        self._letter_names_text.delete("1.0", END) # Clear text
        self._pictographs_text.delete("1.0", END) # Clear text
        self._geomatria_text.delete("1.0", END) # Clear text
        self._divisibles_text.delete("1.0", END) # Clear text
    
    # Process letter names
    def process_letter_names(self, hebrew_letter_names):
        self._letter_names_text.delete("1.0", END) # Clear text
        self._letter_names_text.insert("1.0", "Word Entered: " + self.hebrew_input_expression + "\n")
        reverse_letters = self.hebrew_input_expression[::-1]
        for letter in reverse_letters:
            self._letter_names_text.insert(END, letter + ": " + hebrew_letter_names[letter] + "\n")  
    
    # Process pictographs
    def process_pictographs(self, hebrew_pictographs, hebrew_letter_names, hebrew_mnemonics):
        self._pictographs_text.delete("1.0", END) # Clear text
        reverse_letters = self.hebrew_input_expression[::-1]
        for letter in reverse_letters:
            letter_name = hebrew_letter_names[letter]
            pictograph = str(hebrew_pictographs[letter_name]).replace("|", ", ")
            self._pictographs_text.insert(END, letter + ":\nPictograph: " + pictograph + "\n")
            mnemonic = str(hebrew_mnemonics[letter_name]).replace("|", ",\n")
            self._pictographs_text.insert(END, "Mnemonic for " + letter + ":\n" + mnemonic + "\n\n")
    
    # Process geomatria
    def process_geomatria(self, hebrew_numbers, number_meanings, hebrew_letter_names):
        self._geomatria_text.delete("1.0", END) # Clear text
        _sum = 0
        reverse_letters = self.hebrew_input_expression[::-1]
        for letter in reverse_letters:
            letter_name = hebrew_letter_names[letter]
            number = hebrew_numbers[letter_name]
            _sum += int(number)
            try:
                meaning = number_meanings[number].replace("|", ", ")
                self._geomatria_text.insert(END, letter + ": " + number + " - " + meaning + "\n")
            except:
                self._geomatria_text.insert(END, letter + ": " + number + "\n")
        self._geomatria_text.insert(END, "\nSum = " + str(_sum) + "\n")
    
    # Process Hebrew Dates
    def process_hebrew_dates(self):        
        calc_heb_dates = CalculateHebrewDates()
        hebrew_date = calc_heb_dates.calc_hebrew_date(2020, 2, 29)
        heb_year = hebrew_date[0]
        heb_month = hebrew_date[1]
        heb_day = hebrew_date[2]
        heb_month_name = calc_heb_dates.get_hebrew_month_name(heb_month)
        return "Current Hebrew Date: " + \
                                 str(heb_day) + " " + \
                                 heb_month_name.title() + " " + \
                                 str(heb_year) + " "
        
        holidays_2020 = "\nHolidays 2020 (Hard-coded):\n\
        \nShabbat 	Weekly Sabbath from Friday sunset to Saturday night\n\
Purim 	Mon-Tues, March 9-10, 2020\n\
Passover* 	Wed-Thurs, April 8-16, 2020\n\
Shavuot 	Thurs-Sat, May 28-30, 2020\n\
Rosh Hashanah 	Fri-Sun, Sept. 18-20, 2020\n\
Yom Kippur 	Sun-Mon, Sept. 27-28, 2020\n\
Sukkot 	Fri-Fri, Oct. 2-9, 2020\n\
Shemini Atzeret / Simchat Torah   	Sat-Sun, Oct. 10-11, 2020\n\
Hanukkah 	Thurs-Fri, Dec. 10-18, 2020\n"
        
        
    # Process divisibles
    def process_divisibles(self, hebrew_numbers, number_meanings, hebrew_letter_names):
        self._divisibles_text.delete("1.0", END) # Clear text
        _sum = 0
        reverse_letters = self.hebrew_input_expression[::-1]
        for letter in reverse_letters:
            letter_name = hebrew_letter_names[letter]
            number = hebrew_numbers[letter_name]
            _sum += int(number)
        self._divisibles_text.insert(END, "Total " + str(_sum) + " is divisible by:""\n")
        for x in range(2, _sum - 1):
            if (_sum % x) == 0:
                try:
                    meaning = number_meanings[str(x)].replace("|", ", ")
                    self._divisibles_text.insert(END, str(x) + " - " + meaning + "\n")
                except:
                    self._divisibles_text.insert(END, str(x) + "\n")        

        
    def save_hebrew_word(self):
        save_hebrew_word_class = SaveHebrewWord()
    
class SaveHebrewWord(Frame):
    
    def __init__(self):
        Frame.__init__(self)
        pad_x = 5
        pad_y = 5
        self._english_word_label = Label(self, width=50, height=1, text="English Word")
        self._english_word_label.grid(row=0, column=0, padx=pad_x, pady=pad_y)
        
        self._letter_button = Button(self, text="Save", \
                                     command=lambda: self.save())
        self._letter_button.grid(row=1, column=0)
        
    def save(self):
        print("Saving")
        
    

class CalculateHebrewDates():

    hebrew_month_dict = { 1: 'NISAN',
                         2: 'IYYAR',
                         3: 'SIVAN',
                         4: 'TAMMUZ',
                         5: 'AV',
                         6: 'ELUL',
                         7: 'TISHRI',
                         8: 'HESHVAN',
                         9: 'KISLEV',
                         10: 'TEVETH',
                         11: 'SHEVAT',
                         12: 'ADAR',
                         13: 'VEADAR'
    }
    
    def calc_hebrew_date(self, year, month, name):
        return hebrew.from_gregorian(2020, 2, 29)

    def get_hebrew_month_name(self, month):
        return self.hebrew_month_dict[month]

def load_hebrew_names():
    filename = "hebrew-names-data.json"
    try:
        f = open(filename, 'r')
        json_raw_data = f.read()
        json_data = json.loads(json_raw_data)  
        return scrub_hebrew_names(json_data)
    except Exception as e:
        print(str(e))
        print("File could not be opened")

def scrub_hebrew_names(json_data):
    new_hebrew_names = {}
    for key in json_data.keys():
        new_hebrew_names[key] = json_data[key][1]
    return new_hebrew_names

def main():
    hebrew_letters_gui = HebrewLettersGui()
    hebrew_letters_gui.mainloop()

main()


"""
U+05D0	א	Hebrew Letter Aleph
U+05D1	ב	Hebrew Letter Beyt
U+05D2	ג	Hebrew Letter Gimel
U+05D3	ד	Hebrew Letter Dalet
U+05D4	ה	Hebrew Letter He
U+05D5	ו	Hebrew Letter Waw
U+05D6	ז	Hebrew Letter Zayin
U+05D7	ח	Hebrew Letter Het
U+05D8	ט	Hebrew Letter Tet
U+05D9	י	Hebrew Letter Yod
U+05DA	ך	Hebrew Letter Final Kaph
U+05DB	כ	Hebrew Letter Kaph
U+05DC	ל	Hebrew Letter Lamed
U+05DD	ם	Hebrew Letter Final Mem
U+05DE	מ	Hebrew Letter Mem
U+05DF	ן	Hebrew Letter Final Nun
U+05E0	נ	Hebrew Letter Nun
U+05E1	ס	Hebrew Letter Samekh
U+05E2	ע	Hebrew Letter Ayin
U+05E3	ף	Hebrew Letter Final Pey
U+05E4	פ	Hebrew Letter Pey
U+05E5	ץ	Hebrew Letter Final Tsadi
U+05E6	צ	Hebrew Letter Tsadi
U+05E7	ק	Hebrew Letter Qof
U+05E8	ר	Hebrew Letter Resh
U+05E9	ש	Hebrew Letter Shin
U+05EA	ת	Hebrew Letter Taw
"""
