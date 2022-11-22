import youtube_dl

link =[' $url']
with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)
