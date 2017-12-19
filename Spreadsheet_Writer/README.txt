How to use the spreadsheet writer:

### PRELIMINARY STUFF ###

Before running any scripts, make sure you have python 3.5 downloaded. This script won't work on any python versions under 3. 
Go here:
https://www.python.org/downloads/

Once you have python, you need to install the mutagen library. Enter the following on the command line:

pip install mutagen

If you want to edit the python script, download a graphical user interface. I use Anaconda.
https://www.continuum.io/downloads

### PROCEDURE ###

1. Put the .mp3 files of the music being added in this directory.

2. Open a command window in the current directory and run "spreadsheet_writer.py"

3. The information from the songs in this drive should now be in the "add_to_master.csv" spreadsheet.
That spreadsheet is conveniently formatted so that it can be directly copy/pasted to the Master Playlist.

4. Copy/paste the info from add_to_master.csv to the Master Playlist

If there are any errors, like say a KeyError, it's most likely because at least 
one of the mp3 files in the directory is corrupt. Either manually edit the properties of the file or
remove that file and manually input it into the master playlist.

### THINGS TO NOTE ###
- By default, the year will be 2017. This will have to be manually changed.
- The genres in the meta-data can be a bit funky because of whoever inputted them. Best double-check on Metal-Archives