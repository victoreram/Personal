# -*- coding: utf-8 -*-
import scrapy


class MetalbotSpider(scrapy.Spider):
    name = 'metalbot'
    allowed_domains = ['www.metal-archives.com/albums/Iron_Maiden/Killers/74']
    start_urls = ['https://www.metal-archives.com/albums/Iron_Maiden/Killers/74/']

    def parse(self, response):
        band = response.css(".band_name a::text").extract()
        #artist_link = response.css(".band_name a").extract()
        album = response.css(".album_name a::text").extract() 
        tracks = response.css(".wrapWords::text").extract()
        tracks = [t.replace("\n", "") for t in tracks]
        tracks = [t.replace("\t", "") for t in tracks]
        times = response.css(".wrapWords+ td::text").extract()
        year = response.css(".float_left dd:nth-child(4)::text").extract()[0].split(', ')[1]
        #scraped_info = [[item[0], artist, album, year, item[1]] for item in zip(tracks, times)]
        #print(scraped_info)
        for item in zip(tracks, times):
            #create a dictionary to store the scraped info
            track = item[0]
            time = item[1]
            
            scraped_info = {
                'band' : band,
                'track' : track,
                'album' : album,
                'year' : year,
                'time' : time,
            }

#            yield or give the scraped info to scrapy
            yield scraped_info
        #yield scraped_info