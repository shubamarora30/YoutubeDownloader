from __future__ import unicode_literals
import youtube_dl
import pytube
class download:
	def start_download(gui,url,type):
		if type=='Video':
			link=pytube.YouTube(url)
			videos=link.streams.filter(progressive=True).all()
			vid=videos[0]
			destination="C:/Users/arora/Desktop"
			vid.download(destination)
		else:
			ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			    ydl.download([url])
