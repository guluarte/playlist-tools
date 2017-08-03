for %%a in (*.mkv *.avi *.mpg *.mp4 *.m4v) do (
	python C:\path\pimslur-audio-15sec.py "%%a"
)
PAUSE