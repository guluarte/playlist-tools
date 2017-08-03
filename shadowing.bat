for %%a in (*.mkv *.avi *.mpg *.mp4) do (
	python C:\path\shadowing.py 10 "%%a" "%%a.srt" 
)
PAUSE