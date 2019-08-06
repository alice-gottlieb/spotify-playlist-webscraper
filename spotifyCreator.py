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

def createPlaylists(jsonData, spot, user):
	r'''Create a playlist for every unique album.
	
	Arguments:
	jsonData -- data extracted by timeLifeAutoCrawler.py including Album Name, Track Name, and Artist
	spot -- authenticated spotify object
	user -- username
	'''
	
	albumNames = set([track['albumName'] for track in data])
	for albumName in albumNames:
		print(spot.user_playlist_create(user, albumName))
		

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