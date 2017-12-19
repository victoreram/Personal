# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:14:07 2017

@author: ramir
"""

# Import packages
#from urllib.request import urlopen, Request
from lxml import etree
import requests
from bs4 import BeautifulSoup


# Initiate empty dictionary of bands
bands = {}

# Specify the url
url = "https://www.metal-archives.com/bands/Iron_Maiden/25"
r = requests.get(url)
html = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html, "lxml")

# Extract band name and info
band = soup.title.string.replace(" - Encyclopaedia Metallum: The Metal Archives", "")
#print(band.string)
#prinstring.replace(" - Encyclopaedia Metallum: The Metal Archives", "")
band_info = soup.find_all("dd")
band_info = [i.string for i in band_info]
band_info.pop()
if band in bands:
    band = band + band_info[0]
    bands[band] = band_info
else:
    bands[band] = band_info

print(bands)
# Get Guido's text: guido_text
#MA_text = soup.get_text()
#
## Print Guido's text to the shell
##print(MA_text)
#
##print hyperlinks
##a_tags = soup.find_all("a")
#
## Print the URLs to the shell
##for link in a_tags:
##    print(link.get('href'))
#
#album_tags = soup.find_all(class_="tabs2lvl")
#print(album_tags)
