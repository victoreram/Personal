
import csv
import os
import time_class as t
from mutagen.easyid3 import EasyID3
import mutagen
from mutagen.mp3 import MP3

files = os.listdir(os.curdir)
master = open('MASTER PLAYLIST - Playlist.csv') 
m_playlist = csv.reader(master)
    
with open('add_to_master.csv', 'w') as csvfile:
    header = m_playlist.__next__()
    fieldnames = header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
    writer.writeheader()

    for f in files:
        if 'mp3' in f[-4:]:
            #mutagen.File(f)
            #audio = EasyID3(f)
            #title, artist, album = audio['title'], audio['artist'], audio['album']
            audio = MP3(f)
            length = t.s_to_time(audio.info.length)
            song = EasyID3(f)
            #title, artist, album = song['title'][0], song['artist'][0], song['album'][0]
            try:
                title = song['title'][0]
                            
            
            except:
                title = ''
                
            try:
                artist = song['artist'][0]
            except:
                artist = ''
                
            try:
                album = song['album'][0]
            except:
                album = ''
                            
            try:
                genre = song['genre'][0]
            except:
                genre = ''
                
            try:
                year = song['year'][0]
            except:
                year = '2017'
            #print(title, artist, album, length)
            writer.writerow({'Title': title, 'Band': artist, 'Album': album, 
                             'Plays': '0', 'Riv': 'x',
                             'Time': length, 'Genre': genre, 'Year': year} )

csvfile.close()
