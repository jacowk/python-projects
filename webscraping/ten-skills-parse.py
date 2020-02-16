#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:01:01 2020

@author: jaco
"""

import bs4


# Read from file
filename = "ten-skills.htm"
outputfilename = "ten-skills-links.txt"

# Open the file
file = open(filename, 'r')
output_file = open(outputfilename, 'a')

# Find all links
soup = bs4.BeautifulSoup(file, 'html.parser')
linkElements = soup.find_all('a', href=True)
print(type(linkElements))
count = 0
for linkElement in linkElements:
    link_url = linkElement['href']
    link_text = linkElement.text
    if link_url.startswith("http") and "twitter" not in link_url and "github" not in link_url and "facebook" not in link_url:
        count += 1
        output = str(count), link_text.strip(), ":", link_url.strip()
        print(output)
        output_file.write(output)

# Find the text and the url


# Output the text, url

# Close the file
file.close()
output_file.close()