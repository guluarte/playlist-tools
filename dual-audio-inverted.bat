for %%a in (*.mkv *.avi *.mpg *.mp4 *.m4v) do (
	python C:\path\movie-audio-inverted.py "%%a"
)
PAUSE