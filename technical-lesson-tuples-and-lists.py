# Task 1: Data Preparation
# Define a list to store user listening histories
user_data = [
    ("Rock", ["Metallica", "Guns N' Roses", "AC/DC"]),
    ("Pop", ["Taylor Swift", "Ed Sheeran", "BTS"]),
    ("Hip Hop", ["Drake", "Kendrick Lamar", "J. Cole"]),
    ("Rock", ["Led Zeppelin", "Pink Floyd", "The Who"]),
    ("Pop", ["Ariana Grande", "The Weeknd", "Olivia Rodrigo"]),
    ("Electronic", ["Daft Punk", "Deadmau5", "Skrillex"]),
    ("Jazz", ["Miles Davis", "John Coltrane", "Ella Fitzgerald"]),
    ("R&B", ["Beyoncé", "The Weeknd", "H.E.R."]),
    ("Country", ["Luke Combs", "Morgan Wallen", "Kacey Musgraves"]),
    ("Indie", ["Arctic Monkeys", "Tame Impala", "Vampire Weekend"])
]

# Task 2: Finding the Most Popular Genre
# Create an empty dictionary to track genre frequencies
genre_counts = {}

# Iterate through user_data to count genres
for user_listening in user_data:
    # Extract genre (first element of the tuple)
    genre = user_listening[0]
    
    # Update the count in the dictionary
    if genre in genre_counts:
        # Increment existing count
        genre_counts[genre] += 1
    else:
        # Add new genre with count 1
        genre_counts[genre] = 1

# Find the genre with the highest count
most_popular_genre = max(genre_counts, key=genre_counts.get)

# Display the results
print("Genre Counts:")
for genre, count in genre_counts.items():
    print(f"{genre}: {count} users")
    
print(f"\nMost Popular Genre: {most_popular_genre} with {genre_counts[most_popular_genre]} users")

# Task 3: Finding Users Who Listen to a Specific Artist
# Define the target artist
target_artist = "The Weeknd"

# Create a list to store user indices
users_listening = []

# Iterate through user_data with indices to find users who listen to the target artist
for index, user_listening in enumerate(user_data):
    # Extract the list of artists (second element of the tuple)
    artists = user_listening[1]
    
    # Check if target artist is in the user's listening history
    if target_artist in artists:
        # Store the user's index
        users_listening.append(index)

# Display the results
if users_listening:
    print(f"\nUsers who listen to {target_artist}:")
    for user_index in users_listening:
        # Show user index and their complete listening data
        print(f"User {user_index}: Genre - {user_data[user_index][0]}, Artists - {', '.join(user_data[user_index][1])}")
else:
    print(f"\nNo users found who listen to {target_artist}")