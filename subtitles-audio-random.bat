for %%a in (*.mkv *.avi *.mpg *.mp4 *.m4v) do (
	python C:\path\subtitles-audio-random.py "%%a"
)
PAUSE