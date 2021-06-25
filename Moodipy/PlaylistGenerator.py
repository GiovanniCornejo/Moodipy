# THIS MODULE IS STILL IN THE TESTING PHASE
# Create a Playlist from Sentiment Analysis and Track Analysis
from Spotipy import User
import SpotifyAuthorization
from SpotifyAuthorization import user

""" 
Step 0: Get Users Liked Songs
"""
user_songs = user.get_user_saved_tracks()
# Check that all songs are gotten
for i, track in enumerate(user_songs, 1):
    print(i, track['name'])


"""
Step 1: Create a Playlist for the User
"""
playlist_name = "Testing"
description = "This is a new playlist!"
user.create_playlist(playlist_name=playlist_name, description=description)

"""
Step 2: Add Songs to a Playlist
"""
user.add_to_playlist(playlist_name=playlist_name, playlist_tracks=user_songs)