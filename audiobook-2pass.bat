for %%a in (*.mkv *.avi *.mpg *.mp4 *.mp3 *.m4a) do (
	python C:\path\audiobook-2-pass.py 60 "%%a"
)
PAUSE