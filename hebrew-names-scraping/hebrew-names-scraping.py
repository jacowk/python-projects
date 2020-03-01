#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:46:31 2020

@author: jaco

https://www.behindthename.com/names/usage/biblical-hebrew

https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import bs4, pandas as pd, html, json

#&#1488;&#1458;&#1491;&#1463;&#1500;&#1456;&#1497;&#1464;&#1488;
#letter = "&#1488;&#1458;&#1491;&#1463;&#1500;&#1456;&#1497;&#1464;&#1488;"
#print(html.unescape(letter))


def main():
    # Read from file
    filename = "hebrew-names.htm"
    outputfilename = "hebrew-name.txt"
    
    # Open the file
    file = open(filename, 'r')
    output_file = open(outputfilename, 'a')
    
    # Find all links
    soup = bs4.BeautifulSoup(file, 'html.parser')
    browse_name_divs = soup.find_all('div', {'class': 'browsename'})
    count = 0
    
    final_data_map = {}
    
    for browse_name_div in browse_name_divs:
        name = ""
        gender = ""
        hebrew_name = ""
        hebrew_form = ""
        children = browse_name_div.findChildren("span")
        hebrew_form_a = browse_name_div.find("a", {"class":"nl"})
        #print(hebrew_form_a)
        for child in children: #bs4.element.Tag
            #print(child)
            #print("\n\n")
            
            try:
                tag_class = child['class'][0]
            except:
                continue
            
            # Process name
            if tag_class == "listname":
                anchor = child.find('a') #bs4.element.Tag
                name = anchor.getText()
        
            # Process gender
            if tag_class == "listgender":
                span = child.find('span') #bs4.element.Tag
                gender = span['title'] #Getting an attribute
                
            # Process hebrew letters
            if tag_class == 'listtrans':
                html_code = child.getText()
                hebrew_name = html.unescape(html_code)
        
        # Process hebrew form
        try:
            hebrew_form = hebrew_form_a.getText()
        except:
            #If Hebrew form in the HTML does not exist, default to the name
            hebrew_form = name
        
        #print(name)
        #print(gender)
        #print(hebrew_name)
        print(hebrew_form)
        
        hebrew_form = scrub_hebrew_form(hebrew_form)
        
        final_data_map[hebrew_form] = [gender, hebrew_name]
        
        count += 1
        #if count == 20:
        #    break
    
    # Final output
    print(final_data_map)
    print("Found " + str(count))
    
    # Output the text, url
    save_json(final_data_map)
    
    # Close the file
    file.close()
    output_file.close()
    
def scrub_hebrew_form(hebrew_form):
    if "(" in hebrew_form:
        index_no = hebrew_form.index("(")
        hebrew_form = hebrew_form[:index_no] # Exclude the text after the ()
        return hebrew_form.strip() # Strio white space
    else:
        return hebrew_form

def save_json(json_data):
    print("Saving")
    json_format = json.dumps(json_data)
    json_filename = "hebrew-names-data.json"
    f = open(json_filename, 'w')
    f.write(json_format)

main()

