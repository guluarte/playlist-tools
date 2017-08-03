for %%a in (*.mkv *.avi *.mpg *.mp4) do (
	python C:\path\subtitles-2pass-origin-target-subtitles.py 15 "%%a" "%%a.en.srt" "%%a.fr.srt"
)
PAUSE