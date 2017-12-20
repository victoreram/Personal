# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:35:55 2017

@author: ramir
"""
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import requests
from bs4 import BeautifulSoup


# Specify the url
url = "https://www.metal-archives.com/albums/Iron_Maiden/The_Number_of_the_Beast/75"
r = requests.get(url)
html = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html, "lxml")
artist, album = soup.title.string.split(' - ')[:2]
album_info = soup.find_all("tr td")
xpath_='''//*[(@id = "album_tabs_tracklist")]//td'''
tracklist = Selector(text=html).xpath(xpath_).extract()
#xpath_ = '//*[contains(concat( " ", @class, " " ), concat( " ", "wrapWords", " " ))]'
#track_info = Selector(text=html).xpath(xpath_).extract()
#soup.select("#album_tabs")
print(album_info)