from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# Spotify OAuth setup
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "https://examples.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]


# Scrape Billboard Hot 100

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

response = requests.get(BILLBOARD_URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

songs_html = soup.find_all("h3", id="title-of-a-story", class_="c-title")
song_titles = [song.getText().strip() for song in songs_html]

remove_items = {'Songwriter(s)', 'Producer(s)', 'Imprint/Label'}
songs_list = [item for item in song_titles if item not in remove_items]
top_100_songs = songs_list[2:102]


# Search songs on Spotify

spotify_uris = []

for song in top_100_songs:
    result = sp.search(q=song, type="track", limit=1)
    items = result["tracks"]["items"]
    if items:
        uri = items[0]["uri"]
        spotify_uris.append(uri)
        print(f"✅ Found: {song}")
    else:
        print(f"❌ Not found: {song}")
    time.sleep(0.1)

# Create playlist and add songs
playlist_name = "27.10.2025 Billboard Hot 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
print(f"\n🎵 Created playlist: {playlist['name']}")

# Add tracks to playlist in batches of 100 (Spotify limit)
for i in range(0, len(spotify_uris), 100):
    sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_uris[i:i+100])

print(f"✅ Added {len(spotify_uris)} songs to '{playlist_name}'!")