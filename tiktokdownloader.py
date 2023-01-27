import yt_dlp
URL="https://www.tiktok.com/@willsmith/video/7183027161987583278"
ydl_opts={}
with yt_dlp.YoutubeDL(ydl_opts) as yt:
    download_video=yt.extract_info(URL,download=True)
