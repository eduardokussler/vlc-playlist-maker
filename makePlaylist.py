#!python3
import sys
import os

#Receive the directory to look for files
#And the name of the playlist
def createPlaylist(dir, name):
  #files with this extensions will be added to the playlist
  extensions = ['mp4', 'mkv', 'avi']
  #create the playlist file
  f = open(f'{dir}/{name}.m3u', 'w+')
  #get all the files in the directory
  files = os.listdir(dir)
  
  for file in files:
    #if the file is a video, add to the playlist
    if file[-3:] in extensions:
      f.write(f'{dir}/{file}\n')
  f.close()

createPlaylist(sys.argv[1], sys.argv[2])
