# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:23:36 2016

@author: ramir
"""


import time_class as t
#from classes.dir import Dir
#import csv
#'''usecols=(3,4,5,6,7),''
    
def dupe_artist(artist, artist_list):
    '''check if artist already in playlist'''
    if artist in artist_list:
        #print("{} already in playlist".format(artist))
        return True
    else:
        return False
        
def valid_add(song, unique_artists, genre_info=[]):
    song_artist = song[1]
    duplicate_artist = (dupe_artist(song_artist, unique_artists))
    
    if duplicate_artist == True:
        return False
        
    else:
        return True

def add_genre(song, genre_info):
    genre_list = ["black","death","thrash","power","folk","nwobhm","heavy","doom"]
    song_genre = song[5].lower()
    song_time = t.Time(song[4])
    
    
    for genre in genre_list:
        if genre in song_genre:
            #print(genre)
            #print(song_genre)
            genre_info[genre] += song_time
            
    
    return genre_info

def genre_cap(song, genre, dictionary):
    return True
    
def year_cap(song, year, dictionary):
    return True
    
def build_setlist(dictionary):
    options = '''
    s: Make a playlist based on an amount of songs
    t: Make a playlist based on time
    Press ENTER to create a default setlist of 3 hours (without feature)
    '''
    choice = input(options)
    genres = {"black": t.Time(), "death" : t.Time(), "thrash" : t.Time(), 
    "power" : t.Time(), "folk" : t.Time(), "nwobhm": t.Time(), 
    "heavy": t.Time(), "doom": t.Time()}
    artists = []
    years = {"1970's": t.Time(), "1980's": t.Time(), "1990's": t.Time(), 
    "2000's": t.Time(), "2010's": t.Time(), "2016": t.Time() } 
    setlist = []
    if choice == 's':
        s = int(input("How many total songs? "))
        
        for i in range(s):
            k = random.sample(list(dictionary),1)[0]
            song = dictionary[k]
            total_time = t.Time()
            #song_str = "".join(song)

        
            #song_info = dictionary[k]
            #song_info.insert(0,song)
            if valid_add(song,artists) == True and song[4] != "":
                setlist.append(song)
                artists.append(song[1])
                total_time += t.Time(song[4])
                genres = add_genre(song,genres)
            else:
                print("{} not added".format(song[0]))
                
    elif choice == 't':
        t_str = t.Time(input("Enter the minimum time in mm:ss format: "))
        total_time = t.Time()
        
        while total_time < t_str:
            k = random.sample(list(dictionary),1)[0]
            song = dictionary[k]
            
            if valid_add(song,artists) == True and song[4] != "":
                setlist.append(song)
                artists.append(song[1])
                total_time += t.Time(song[4])  
                genres = add_genre(song,genres)
            else:
                print("{} not added".format(song[0]))
            
        
    else:
        default_time = t.Time("180:00")
        total_time = t.Time()
        
        while total_time < default_time:
            
            k = random.sample(list(dictionary),1)[0]
            song = dictionary[k]
            
            if valid_add(song,artists) == True and song[4] != "":
                setlist.append(song)
                artists.append(song[1])
                total_time += t.Time(song[4])
                genres = add_genre(song,genres)

    #print(artists)

    #print(genres["death"])
    for genre in genres:
        print(genre, "-", genres[genre])
    #    print ("{:12} {:5}".format(genre, genres[genre]))
            
    #print(setlist)
    #print(artists)
    return setlist

def print_setlist(setlist):
    total_time = t.Time()
    song_count = 1
    #print("NO.|{:30}|{:20}|{:25}|{:4}|{:5}|{:25}".format(
    #'SONG', 'ARTIST', 'ALBUM', 'YEAR', 'TIME', 'GENRE'))
    
    setlist_str = "NO. |{:30}|{:20}|{:25}|{:4}|{:5}|{:25}".format(
    'SONG', 'ARTIST', 'ALBUM', 'YEAR', 'TIME', 'GENRE')
    #print(header_str)
    for song in setlist:
        song_str = "{:4}{:30}|{:20}|{:25}|{:4}|{:5}|{:25}".format(str(song_count)+'.',
        song[0], song[1], song[2], song[3], song[4], song[5])
        #print("{}. {:30}|{:20}|{:25}|{:4}|{:5}|{:25}".format(song_count,
        #song[0], song[1], song[2], song[3], song[4], song[5]))
        setlist_str += '\n'
        setlist_str += song_str
        #print(song_str)
        if song[4] != "":
            total_time += t.Time(song[4])
        song_count+=1
    
    total_time_str = "TOTAL TIME: {}".format(total_time)
    setlist_str += '\n' + total_time_str
    print(setlist_str)
    return setlist_str
    
def write_playlist(playlist):
    playlist_file = open("playlist.txt",'w')
    for line in playlist:
        playlist_file.write(line)
    
    

def create_dict(playlist):
    songs = {}
    key = 0
    for row in playlist:
        if row[3] != "0":
            songs[key] = [row[4],row[5],row[6],row[7],row[8],row[9],row[3]]
            key += 1
            #print(key)
            
            #if row[3] != '':
            #    row[3] -= 1
    return songs 
    
import random
import csv
with open('MASTER PLAYLIST - Playlist.csv') as master:
    m_playlist = csv.reader(master)
    next(m_playlist)
    song_dict = create_dict(m_playlist)
    setlist = build_setlist(song_dict)
    playlist = print_setlist(setlist)
    write_playlist(playlist)
    #incsv.next()
    #unique_artists = []
    
        #song = row[4]

        #if row[5] not in unique_artists:
        #    unique_artists.append(row[5])
         #print(row[4])
         #for cat in row:
         #    print(cat)
    #print(len(master))


#print(len(song_dict))

master.close()
#unique_artists.sort()
#print(unique_artists)
#for artist in unique_artists:
#    print(artist)

'''
import numpy as np
count=0
unique_artists = []
master = open("master1.csv")
result = np.loadtxt(master,delimiter=',',skiprows=1,unpack=True)
for line in master:
    print(line)
    #print(line[2])
#print(count)
    */'''