import json
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials

with open('autoCrawler.json', 'r') as crawlerFile:
	data = json.load(crawlerFile)
	spotify = sp.Spotify()
	songTestLink = 'spotify:track:3MECtlvsjOopA66odGHa5P'
	client_credentials_manager = SpotifyClientCredentials()
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	playlists = sp.user_playlists('spotify')
	for track in data:
		# Get data for each track
		albumName = track['albumName']
		trackTitle = track['Title']
		trackArtist = track['Artist']
		# Spotify search
		# results = sp.search(q=)
	