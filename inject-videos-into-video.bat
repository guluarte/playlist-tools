for %%a in (*.mkv *.avi *.mpg *.mp4) do (
	python C:\path\inject-videos-into-video.py 800 "%%a"
)
PAUSE