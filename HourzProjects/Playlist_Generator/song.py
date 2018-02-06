
import random
import csv

class Song:
    
    def __init__(self, title = '', artist = '', album = '', year = '', genre = '', length = ''):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre
        self.length = length



def create_dict(playlist):
    songs = {}
    key = 0
    for row in playlist:
        if row[0] != "0":
            songs[key] = [row[4],row[5],row[6],row[7],row[8],row[9],row[3]]
            key += 1
            
            
with open('MASTER PLAYLIST - Playlist.csv') as master:
    m_playlist = csv.reader(master)
    next(m_playlist)
    
    song_dict = create_dict(m_playlist)
