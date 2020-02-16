#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 07:14:10 2020

@author: jaco

Exercise: Play with webscraping on the following websites:
-toscrape.com
-https://webscraper.io/test-sites
-scraping.pro/web-scraper-test-drive/

"""
import requests, os, bs4, time, pandas as pd

url = 'http://books.toscrape.com'
res = requests.get(url)
try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    productElements = soup.find_all('article', 'product_pod')
    
    book_names = []
    book_prices = []
    book_availability = []
    #print(type(productElements))
    for productElementTag in productElements:
        # Print all book titles
        links = productElementTag.find_all(name = 'a')
        for link in links:
            if len(link.text) > 0:
                #print(link.text)
                book_names.append(link.text)
                
        # Print all prices
        prices = productElementTag.find_all('p', 'price_color')
        for price in prices:
            #print(price.text[1:])
            book_prices.append(price.text[1:])
        
        # Print instock availability
        instocks = productElementTag.find_all('p', 'instock availability')
        for instock in instocks:
            #print(instock.text.strip())
            book_availability.append(instock.text.strip())
    
    df = pd.DataFrame({'Book Name': book_names,
                      'Book Price': book_prices,
                      'Book Availability': book_availability},
        index = range(0, len(book_names)))
    df.style.set_properties({'text-align': 'left'})
    print(df)
    #help(bs4.element.Tag)
except Exception as exc:
    print("Something went wrong: %s" % exc)
    


