# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:09:44 2017

@author: ramir
"""
import requests, sys, webbrowser, bs4, time
from scrapy.selector import Selector

#bands=['Iron Maiden', 'Inquisition', 'Power Trip']
band = "Power Trip"
song = "Soul Sacrifice"
album = "Nightmare Logic"

#URL_SEARCH = 'https://www.metal-archives.com/search?searchString='
URL_BASE = "https://www.metal-archives.com/search/advanced/searching/songs?"
SEARCH_BY_SONG = "songTitle="
SEARCH_BY_BAND = "&bandName="
SEARCH_BY_ALBUM = "&releaseTitle="
SEARCH_BY_LYRICS = "&lyrics="
SEARCH_BY_GENRE = "&genre="
SEARCH_TYPE = ""

"https://www.metal-archives.com/search/advanced/searching/songs?songTitle=soul+sacrifice&bandName=power+trip&releaseTitle=&lyrics=&genre=#songs"
SEARCH_TERM = '+'.join(sys.argv[1:])

URL_SEARCH = URL_BASE + SEARCH_BY_SONG + SEARCH_TERM + SEARCH_BY_BAND + SEARCH_BY_ALBUM + SEARCH_BY_LYRICS + SEARCH_BY_GENRE + SEARCH_TYPE
time.sleep(3)
res = requests.get(URL_SEARCH)
print("searching for", SEARCH_TERM.replace("+", " "))
print("crawling", URL_SEARCH)
res.raise_for_status()
html = res.text

# Retrieve top search result links.
soup = bs4.BeautifulSoup(html, "lxml")

# Open a browser tab for each result.
linkElems = soup.find_all('searchResultsSong')
#linkElems = soup.select('.r a')
xpath_='''//td'''


### TO DO: FIND THE SEARCH RESULTS
print(Selector(text=html).xpath(xpath_).extract())
#print(search_results)
#print(linkElems)
#print(soup.find_all('a'))
print(soup.select(".td"))
print(soup.find_all("advancedResults"))
print(soup.find_all("searchResultsSong_wrapper"))
print(linkElems)
print(soup.find("nightmare logic"))