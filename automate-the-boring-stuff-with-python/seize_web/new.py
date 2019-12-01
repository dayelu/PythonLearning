import requests

def downing(url):
	res = requests.get(url)
	res.raise_for_status()
	playFile = open('1.png','wb')
	for chunk in res.iter_content(100000):
		playFile.write(chunk)


url = "http://static.ws.126.net/video/2013/4/22/2013042211092411038.png"
downing(url)