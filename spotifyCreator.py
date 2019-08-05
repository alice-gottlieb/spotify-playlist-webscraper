import sys
import json
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

CLIENT_ID='a66d208e17874246af021cc9b819400d'
CLIENT_SECRET='e79e635054f9404792560a1d99eacc7b' # will be reset after use
REDIRECT_URI='http://localhost:8888/'
scope = 'user-library-read playlist-modify-public'
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
		results = spotify.current_user_saved_tracks()
		print(len(results))
		for item in results['items']:
			track = item['track']
			print(track['name'] + ' - ' + track['artists'][0]['name'])

	# for track in data:
		# # Get data for each track
		# albumName = track['albumName']
		# trackTitle = track['Title']
		# trackArtist = track['Artist']
		# # Spotify search
		# # results = sp.search(q=)
	