artist_songs = {
    "The Beatles": ["Hey Jude", "Let It Be", "Yesterday"],
    "Taylor Swift": ["Shake It Off", "Love Story", "Blank Space"],
    "Ed Sheeran": ["Perfect", "Thinking Out Loud", "Photograph"]
}

'''beatles_songs = artist_songs["The Beatles"]

for song in beatles_songs:
    print(f"- {song}")'''

favorite_artist = input("Enter your favorite artist: ")

if favorite_artist in artist_songs:
    recommended_songs = artist_songs[favorite_artist]
    print(f"Recommended songs by {favorite_artist}:")
    for song in recommended_songs:
        print(f"- {song}")
else:
    print(f"Sorry, we don't have recommendations for {favorite_artist}.")