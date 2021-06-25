#Spotify Web API authorization
from Spotipy import Spotify, User

# Moodipy Client Environment Variables
client_id = "17c9e6c9abe14de9bbfbb10c7d89afa4"
client_secret = ""
redirect_uri = "http://localhost:8080"

# User Environent Variables
user_id = "igjsqvqpbxeuhoxlgvplj68qf"
scope = "user-library-read  playlist-modify-public"

# Spotify Entry Points Created
client = Spotify(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
user = User(user_id=user_id, scope=scope, client=client)
