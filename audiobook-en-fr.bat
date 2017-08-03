for %%a in (*.mkv *.avi *.mpg *.mp4 *.mp3) do (
	python C:\path\audiobook.py 15 "%%a" "2.%%a"
)
PAUSE