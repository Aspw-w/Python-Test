from yt_dlp import YoutubeDL

input_url = str(input('URL: '))

config = {
    'outtmpl' : 'C:/Users/0kcab/Documents/GitHub/Python-Test/yt-dl/%(title)s.%(ext)s',
    'format' : 'bestvideo+bestaudio/best'
}

try:
    with YoutubeDL(config) as ydl:
        request = ydl.download([input_url])
    print('Success')
except:
    print('Failed')