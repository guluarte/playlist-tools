for %%a in (*.mkv *.avi *.mpg *.mp4 *.mp3) do (
	python C:\path\subtitles-3pass--origin-target-none.py 30 "%%a" "%%~na.en.srt" "%%~na.fr.srt"
)
PAUSE