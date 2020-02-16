#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 08:57:32 2020

@author: jaco

Downloads XKCD comics

"""
import requests, os, bs4, time

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
    
#while not url.endswith('#'):
for x in range(0, 5):
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    try:
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
    
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
    
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')
        
        if url.endswith('#'):
            break
        
    except Exception as exc:
        print('There was a problem: %s' % exc)
    print("Sleeping 2 secs...")
    time.sleep(2)

print('Done')
