import subprocess
import re
import sys
import codecs
import urllib
import os, random




def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
  stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  duration_str = [x for x in result.stdout.readlines() if "Duration" in x]
  m = re.search('(\d{2}):(\d{2}):(\d{2})', duration_str[0])
  print m
  return (m.group(1), m.group(2), m.group(3) )

def get_video_time(filename):
  print filename
  hours, minutes, secons = getLength(filename)
  total_seconds = int(hours) * 60 * 60
  total_seconds += int(minutes) * 60
  total_seconds += int(secons)
  return total_seconds

def get_random_video(folder):
  pathdir = "C:\\\path\\%s\\" % folder
  return pathdir + random.choice(os.listdir(pathdir)) #change dir name to whatever

def get_file_extension(filename):
  return filename[-3:]

class Playlist():
  def __init__(self):
    self.playlist = ""


def get_playlist_header():
  return u"""<?xml version="1.0" encoding="UTF-8"?>
 <playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">
  <trackList>
  """
def get_playlist_footer():
  return u"\n</trackList>\n</playlist>"

def get_track(filename, start, end, vlc_id):
  track_str = u"\t<track>\n"
  track_str += u"\t\t<location>file:///%s</location>\n" % urllib.quote(filename)
  track_str += u"\t\t<trackNum>%s</trackNum>\n" % (vlc_id)
  track_str += u"\t\t<extension application=\"http://www.videolan.org/vlc/playlist/0\">\n"
  track_str += u"\t\t\t<vlc:option>start-time=%s</vlc:option>\n" % (start-3)
  track_str += u"\t\t\t<vlc:option>stop-time=%s</vlc:option>\n" % end
  track_str += u"\t\t\t<vlc:option>--no-random</vlc:option>\n"
  track_str += u"\t\t\t<vlc:id>%s</vlc:id>\n" % vlc_id
  track_str += u"\t\t</extension>\n"
  track_str += u"\t</track>\n"
  return track_str

def add_track(filename, vlc_id):
  track_str = u"\t<track>\n"
  track_str += u"\t\t<title>%s - %s</title>\n" % (vlc_id, urllib.quote(filename))
  track_str += u"\t\t<location>file:///%s</location>\n" % urllib.quote(filename)
  track_str += u"\t\t<trackNum>%s</trackNum>\n" % (vlc_id)
  track_str += u"\t\t<extension application=\"http://www.videolan.org/vlc/playlist/0\">\n"
  track_str += u"\t\t\t<vlc:id>%s</vlc:id>\n" % vlc_id
  track_str += u"\t\t\t<vlc:option>--no-random</vlc:option>\n"
  track_str += u"\t\t</extension>\n"
  track_str += u"\t</track>\n"
  return track_str  

interval = 600
current_time = 0
if len(sys.argv) > 1:
  interval = int(sys.argv[1])
  movie = sys.argv[2]
  print "Movie: %s " % movie
  print "Interval: %s " % interval
else:
  print "You need to provide the name of the file without the extension.\n"
  sys.exit(-1)

total_seconds = get_video_time(movie)

playlist_str = get_playlist_header()
vlc_id = 1
while current_time < total_seconds:
  play_until = current_time + interval
  playlist_str += get_track(movie, current_time, play_until, vlc_id)
  vlc_id += 1
  current_time += interval
  if current_time < total_seconds:
	  playlist_str += add_track(get_random_video("clases"), vlc_id)
	  vlc_id += 1
	  playlist_str += add_track(get_random_video("bussu"), vlc_id)
	  vlc_id += 1

  


playlist_str += get_playlist_footer()


fp = codecs.open(movie[:-4] + ".xspf", "w+")
fp.write(playlist_str)
fp.close()

print "Done.\n"
