import sys
import json
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

CLIENT_ID='a66d208e17874246af021cc9b819400d'
CLIENT_SECRET='e79e635054f9404792560a1d99eacc7b' # will be reset after use
REDIRECT_URI='http://localhost:8888/'
scope = 'user-library-read playlist-modify-public playlist-read-private'
songTestLink = 'spotify:track:3MECtlvsjOopA66odGHa5P'

#get username from console
if len(sys.argv) > 1:
    username = sys.argv[1]
    print('username: ' + username)
else:
    print('Need username')
    sys.exit()

with open('autoCrawler.json', 'r') as crawlerFile:
	data = json.load(crawlerFile)
	token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
	
	if token:
		spotify = sp.Spotify(auth=token)
		playlists = spotify.user_playlists(username)
		for playlist in playlists['items']:
			if playlist['owner']['id'] == username:
				print(playlist['name'])
				print('  total tracks', playlist['tracks']['total'])
				tracks = spotify.user_playlist(username, playlist['id'], fields='tracks')['tracks']
				i = 0
				for track in tracks['items']:
					print(track['track']['name'])
					i += 1
					if i == 10:
						break

	# for track in data:
		# # Get data for each track
		# albumName = track['albumName']
		# trackTitle = track['Title']
		# trackArtist = track['Artist']
		# # Spotify search
		# # results = sp.search(q=)
	