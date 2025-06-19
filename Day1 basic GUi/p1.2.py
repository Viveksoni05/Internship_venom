# youtube-dl script to download a video from a given URL
import yt_dlp
url = input("Enter youtube video url: ")
with yt_dlp.YoutubeDL() as ydl:
    ydl.download([url])
