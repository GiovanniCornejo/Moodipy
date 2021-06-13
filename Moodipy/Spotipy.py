import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Class for the Spotify Client
class Spotify(object):
    # Client Variables
    _client_id = None
    _client_secret = None
    _redirect_uri = None
    _spotify_client = None

    # Constructor
    def __init__(self, client_id=None, client_secret=None, redirect_uri=None):
        if client_id == None or client_secret == None:
            raise Exception("You must set client_id and client_secret")

        if redirect_uri == None:
            raise Exception("You must set a redirect_uri")

        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_uri = redirect_uri
        self.spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

        if not self._spotify_client:
            raise Exception("An error occurred on the client side")

# Class for the User
class User(Spotify):
    # User Variables
    _user_token = None
    _user_client = None
    _user_id = None

    # Constructor
    def __init__(self, user_id=None, scope=None, client=None):
        self._user_id = user_id
        self.user_token = util.prompt_for_user_token(user_id, scope,client._client_id, client._client_secret, client._redirect_uri)
        self._user_client = spotipy.Spotify(auth=self._user_token)

        if not self._user_client:
            raise Exception("An error occurred granting access")

    # Returns the ID of a Desired User Playlist
    def get_playlist_id(self, playlist_name=None):
        if playlist_name == None:
            raise Exception("You must enter a playlist name")
        
        playlist_id = None
        playlists = self._user_client.user_playlists(self.user_id)
        for playlist in playlists['items']:
            if playlist['name'] == playlist_name:
                playlist_id = playlist['id']
        
        if playlist_id == None:
            raise Exception("There is no playlist with that name")
        
        return playlist_id

    # Creates a New Playlist for the User
    def create_playlist(self, playlist_name=None, public=True, collaborative=False, description=""):
        if playlist_name == None:
            raise Exception("You must enter a playlist name")
        
        self._user_client.user_playlist_create(self._user_id, name=playlist_name, public=public, collaborative=collaborative, description=description)
    
    # Adds Tracks to a User's Playlist
    def add_to_playlist(self, playlist_name=None, playlist_tracks=None, amount=100):
        if playlist_name == None:
            raise Exception("You must enter a playlist name")
        if amount > 10000 or amount < 1:
            raise Exception("You must enter a valid amount")
        
        playlist_id = self.get_playlist_id(playlist_name=playlist_name)
        track_ids = (track['id'] for track in playlist_tracks[:amount])

        self._user_client.user_playlist_add_tracks(self._user_id, playlist_id=playlist_id, tracks=track_ids)