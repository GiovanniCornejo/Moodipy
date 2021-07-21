#Spotify Web API authorization

from UserSummary import Person
import requests.exceptions
import spotipy
from Spotipy import Spotify, User
from os import path
import time
import os

# Moodipy Client Environment Variables
def Authorization():
    client_id = "17c9e6c9abe14de9bbfbb10c7d89afa4"
    client_secret = "1a8fdfd3501a4c2da9e6bd3fe300b7c8"
    redirect_uri = "http://localhost:8080"

# User Environent Variables
    user_id = Person.userID
    scope = "user-library-read  playlist-modify-public user-top-read user-follow-read"

# Spotify Entry Points Created

    try:
        cache_name = ".cache-" + user_id
        cache_file_path = path.join(path.dirname(__file__), cache_name)
        if os.path.isfile(cache_file_path):
            cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=cache_file_path)
            token_info = cache_handler.get_cached_token()
            now = int(time.time())
            if token_info["expires_at"] - now < 60:
                os.remove(cache_file_path)
        client = Spotify(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        user = User(user_id=user_id, scope=scope, client=client)
        return user, client
    except (spotipy.exceptions.SpotifyException, requests.exceptions.HTTPError,spotipy.oauth2.SpotifyOauthError):
        return None
