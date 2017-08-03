import subprocess
import re
import sys
import codecs
import urllib
import os, string, random
import glob
import uuid

class Playlist():
  def __init__(self):
    self.playlist = ""


def get_playlist_header():
  return u"""#EXTM3U
"""

def get_track(filename, vlc_id):
  track_str = u"%s\n" % urllib.quote(filename)
  return track_str
  
def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

   
num_files_per_file = 100

files = [f for f in os.listdir('.') if f.endswith('xspf')]

random_file_num = 1

while random_file_num < 50:
  vlc_id = 0
  playlist_str = get_playlist_header()
  while vlc_id < num_files_per_file:
    random_playlist = random.choice(files)
    playlist_str += get_track(random_playlist, vlc_id)
    vlc_id += 1

  random_playlist_filename = "0000aaa_" + str(random_file_num) + "_random_" + randomword(10) + ".m3u"
  fp = codecs.open(random_playlist_filename, "w+")
  print random_playlist_filename + ".\n"
  fp.write(playlist_str)
  fp.close()
  random_file_num += 1
  
print "Adding random files"
# add random playlist to the end of the files
random_playlist_files = [f for f in os.listdir('.') if f.endswith('m3u')]

for random_playlist_file in random_playlist_files:
  random_playlist_end = ""
  random_playlist_selected = random.choice(random_playlist_files)
  if random_playlist_selected:
    print random_playlist_selected + "\n"
    random_playlist_end += get_track(random_playlist_selected, vlc_id)
  random_playlist_selected_2 = random.choice(random_playlist_files)
  if random_playlist_selected_2 and random_playlist_selected != random_playlist_selected_2:
    print random_playlist_selected_2 + "\n"
    random_playlist_end += get_track(random_playlist_selected_2, vlc_id)

  pfp = codecs.open(random_playlist_file, "a+")
  pfp.write(random_playlist_end)
  pfp.close()

print "Done.\n"
