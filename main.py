import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from playlist import Playlist
file = open('program_info', 'r')
spotify_info = file.readlines(0)
file.close()
SPOTIFY_CLIENT_ID = spotify_info[0]
CLIENT_SECRET = spotify_info[1]
REDIRECT_URI = 'http://localhost:8888/callback'

scope = 'playlist-modify-public'
username = '(YOUR SPOTIFY USERNAME)'

year = input('What date would you like to get the top 100 from? (format - YYYY-MM-DD ex: 2018-05-23): ')

token = SpotifyOAuth(scope=scope, username=username, client_id=SPOTIFY_CLIENT_ID, client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI)
spotify = spotipy.Spotify(auth_manager=token)

playlist = Playlist()
playlist.set_namedesc(input('Enter the playlist name: '), input('Enter the playlist description: '))
playlist.generate_songs('hot-100', year)
pl = spotify.user_playlist_create(user=username, name=playlist.name, description=playlist.description, public=True)
song_list = []
counter = 0
for song in playlist.songs:
    result = spotify.search(q=song, type='track')
    print(result)
    try:
        if counter < 100:
            song_list.append(result['tracks']['items'][0]['uri'])
    except:
        print('Unable to find song....')
    counter += 1

spotify.playlist_add_items(pl['id'], items=song_list)
