import spotipy
import json

with open('autoCrawler.json', 'r') as crawlerFile:
	data = json.load(crawlerFile)
	print(data)