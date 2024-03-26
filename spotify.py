import json 
import spotipy 
import webbrowser
import time
import os

with open('inputs.json') as f:
    data = json.load(f)

username = data['username']
clientID = data['clientID']
clientSecret = data['clientSecret']
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

print(json.dumps(user_name, sort_keys=True, indent=4))

playlist_id = data['playlist_url'].split('/')[-1]

album = spotifyObject.playlist(playlist_id)

with open('test.json', 'w') as outfile:
    json.dump(album, outfile)

tracks = album['tracks']['items']

for track in tracks:
    print(track['track']['name'])
    url = track['track']['external_urls']['spotify']
    webbrowser.open(url)
    time.sleep((track['track']['duration_ms']/1000)-1)
    os.system("taskkill /im spotify.exe /f")