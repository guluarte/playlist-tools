for %%a in (*.mkv *.avi *.mpg *.mp4) do (
	python C:\path\subtitles-3pass--origin-target-doble-ass.py 15 "%%a" "%%a.en.srt" "%%a.fr.srt" "%%a.both.ass"
)
PAUSE