for %%a in (*.mkv *.avi *.mpg *.mp4) do (
	python C:\path\inject-videos-into-video-no-subs-french.py 400 "%%a"
)
PAUSE