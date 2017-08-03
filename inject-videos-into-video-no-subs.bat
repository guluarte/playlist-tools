for %%a in (*.mkv *.avi *.mpg *.mp4) do (
	python C:\path\inject-videos-into-video-no-subs.py 800 "%%a"
)
PAUSE