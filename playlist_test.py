#Spotify Web API authorization
from Spotipy import Spotify, User
from random import sample

# Moodipy Client Environment Variables
client_id = "17c9e6c9abe14de9bbfbb10c7d89afa4"
client_secret = "1a8fdfd3501a4c2da9e6bd3fe300b7c8"
redirect_uri = "http://localhost:8080"

# User Environent Variables
user_id = "igjsqvqpbxeuhoxlgvplj68qf"
scope = "user-library-read  user-top-read playlist-modify-public"

# Spotify Entry Points Created
client = Spotify(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
user = User(user_id=user_id, scope=scope, client=client)

## TESTING PLAYLIST GENERATION FROM PLAYLIST ##

"""
Step 0: Get Users Playlists
"""
user_playlists = user.get_user_playlists() # Get Playlists Data
user_playlist_data = {} # Get Playlist Names and IDs
for playlist in user_playlists:
    user_playlist_data[playlist['name']] = playlist['id']

"""
Step 1: Get Desired Playlist
"""
playlist_name = '2021 Likes'
playlist_id = user_playlist_data[playlist_name]

"""
Step 2: Get Playlist Tracks
"""
print(playlist_name + " Playlist Songs")
playlist_tracks = user.get_user_playlist_tracks(playlist_id)

for i, track in enumerate(playlist_tracks, 1):
    print(i, track['name'])


# playlist_name = (user._user_client.user_playlist_create(user._user_id, name='Testing'))['id']

# print(playlist_name)