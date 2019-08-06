import sys
import json
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

CLIENT_ID='a66d208e17874246af021cc9b819400d'
CLIENT_SECRET='e79e635054f9404792560a1d99eacc7b' # will be reset after use
REDIRECT_URI='http://localhost:8888/'
scope = 'playlist-modify-public playlist-read-private'

def createPlaylists(jsonData, spot, user):
	r'''Create a playlist for every unique album.
	Skips playlists if they already exist
	
	Arguments:
	jsonData -- data extracted by timeLifeAutoCrawler.py including Album Name, Track Name, and Artist
	spot -- authenticated spotify object
	user -- username
	'''
	
	albumNames = set([track['albumName'] for track in data])
	playlists = spotify.user_playlists(user)
	# Check for playlists that already exists
	playlistNames = []
	for playlist in playlists['items']:
		if playlist['owner']['id'] == user:
			playlistNames.append(playlist['name'])
				
	for albumName in albumNames:
		if not albumName in playlistNames:
			spot.user_playlist_create(user, albumName)
		

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
		createPlaylists(data, spotify, username)