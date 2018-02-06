# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 01:03:40 2017

@author: ramir
"""
class Song:
    def __init__(self, title='', artist='', album='', year='', time='', genre=''):
        self.title, self. artist, self.album, self.year, self.time, self.genre = title, artist, album, year, time, genre
    
    def __str__(self):
        return self.artist + " - " + self.title
    
    
class Playlist:
    def __init__(self, songs):
        self.songs = songs
        count = 1
        playlist = {}
        for song in songs:
            playlist[count] = song
        
        
    
song1 = Song("Invisible", "Dio", "Holy Diver", "1986", "5:01")
print(song1)