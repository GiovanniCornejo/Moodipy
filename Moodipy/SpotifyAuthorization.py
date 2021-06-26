#Spotify Web API authorization

#from UserSummary import Person                 <== Use this if testing the GUI
import requests.exceptions
import spotipy
from Spotipy import Spotify, User

# Moodipy Client Environment Variables
def Authorization():
    client_id = "17c9e6c9abe14de9bbfbb10c7d89afa4"
    client_secret = ""
    redirect_uri = "http://localhost:8080"

# User Environent Variables
    #user_id = Person.userID                    <== Use this if testing the GUI
    user_id = "igjsqvqpbxeuhoxlgvplj68qf"
    scope = "user-library-read  playlist-modify-public"

# Spotify Entry Points Created

    try:
        client = Spotify(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        user = User(user_id=user_id, scope=scope, client=client)
        return user, client
    except (spotipy.exceptions.SpotifyException, requests.exceptions.HTTPError,spotipy.oauth2.SpotifyOauthError):
        return None
