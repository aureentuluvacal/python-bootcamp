playlist = {
  "title": "Sample Playlist",
  "author": "Caryssa",
  "songs": [
    {
      "title": "Bootylicious",
      "artist": "Destiny's Child",
      "duration": 2.5
    },
    {
      "title": "Ego",
      "artist": "Beyonce",
      "duration": 2.5
    }
  ]
}

print(playlist)

total_length = 0
for song in playlist["songs"]:
  total_length += song["duration"]

print(total_length)