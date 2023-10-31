

by CLI with ffmpeg:
ffmpeg -i video.webm -i audio.mp3 -c:v libx264 -c:a aac -strict experimental output.mp4
