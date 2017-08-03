import subprocess
import re
import sys
import codecs
import urllib


def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  duration_str = [x for x in result.stdout.readlines() if "Duration" in x]
  print duration_str
  m = re.search('(\d{2}):(\d{2}):(\d{2})', duration_str[0])
  return (m.group(1), m.group(2), m.group(3) )

def get_video_time(filename):
  try:
    hours, minutes, secons = getLength(filename)
  except Exception, e:
    hours, minutes, secons = (5, 1, 1)

  total_seconds = int(hours) * 60 * 60
  total_seconds += int(minutes) * 60
  total_seconds += int(secons)
  return total_seconds

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

def get_track(filename, start, end, subtitles, vlc_id):
  track_str = u"\t<track>\n"
  if subtitles:
    track_str += u"\t\t<title>%s - subs %s %s-%s</title>\n" % (vlc_id, filename, start, end)
  else:
    track_str += u"\t\t<title>%s - %s %s-%s</title>\n" % (vlc_id, filename, start, end)

  track_str += u"\t\t<location>%s</location>\n" % urllib.quote(filename)
  track_str += u"\t\t<trackNum>%s</trackNum>\n" % (vlc_id+1)
  track_str += u"\t\t<extension application=\"http://www.videolan.org/vlc/playlist/0\">\n"
  track_str += u"\t\t\t<vlc:option>start-time=%s</vlc:option>\n" % (start-5)
  track_str += u"\t\t\t<vlc:option>stop-time=%s</vlc:option>\n" % end
  track_str += u"\t\t\t<vlc:id>%s</vlc:id>\n" % vlc_id
  if subtitles:
    track_str += u"\t\t\t<vlc:option>sub-file=%s</vlc:option>\n" % urllib.quote(subtitles)
  track_str += u"\t\t</extension>\n"
  track_str += u"\t</track>\n"
  return track_str


INCREMENTS = 30
current_time = 0
if len(sys.argv) > 2:
  INCREMENTS = int(sys.argv[1])
  movie = sys.argv[2]
  subs1 = sys.argv[3]
  subs2 = sys.argv[4]
  subs3 = sys.argv[5]
else:
  print "You need to provide the name of the file without the extension. movie sub1 sub2\n"
  sys.exit(-1)

total_seconds = get_video_time(movie)

playlist_str = get_playlist_header()
vlc_id = 0
while current_time < total_seconds:
  playlist_str += get_track(movie, current_time, (current_time+INCREMENTS), subs1, vlc_id)
  vlc_id += 1
  playlist_str += get_track(movie, current_time, (current_time+INCREMENTS), subs2, vlc_id)
  vlc_id += 1
  playlist_str += get_track(movie, current_time, (current_time+INCREMENTS), subs3, vlc_id)
  vlc_id += 1
  playlist_str += get_track(movie, current_time, (current_time+INCREMENTS), False, vlc_id)
  vlc_id += 1

  current_time += INCREMENTS


playlist_str += get_playlist_footer()


fp = codecs.open(movie[:-4] + ".xspf", "w+")
fp.write(playlist_str)
fp.close()

print "Done.\n"
