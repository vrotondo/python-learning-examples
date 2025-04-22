# Task 1: Data Preparation
# Define a list to store user listening histories
user_data = [
    ("Rock", ["Metallica", "Guns N' Roses", "AC/DC"]),
    ("Pop", ["Taylor Swift", "Ed Sheeran", "BTS"]),
    ("Hip Hop", ["Drake", "Kendrick Lamar", "J. Cole"]),
    ("Rock", ["Led Zeppelin", "Pink Floyd", "The Who"]),
    ("Pop", ["Ariana Grande", "The Weeknd", "Olivia Rodrigo"]),
    ("Electronic", ["Daft Punk", "Calvin Harris", "Skrillex"]),
    ("Jazz", ["Miles Davis", "John Coltrane", "Ella Fitzgerald"]),
    ("R&B", ["Beyoncé", "The Weeknd", "H.E.R."]),
    ("Classical", ["Ludovico Einaudi", "Yo-Yo Ma", "Hans Zimmer"]),
    ("Indie", ["Arctic Monkeys", "Tame Impala", "Vampire Weekend"])
]

# Task 2: Finding the Most Popular Genre
# Create an empty dictionary to track genre frequencies
genre_counts = {}

# Iterate through user_data to count genres
for listening_history in user_data:
    # Extract genre (first element of the tuple)
    genre = listening_history[0]
    
    # Update the count in the dictionary
    if genre in genre_counts:
        # Increment existing count
        genre_counts[genre] += 1
    else:
        # Add new genre with count 1
        genre_counts[genre] = 1

# Find the genre with the highest count
most_popular_genre = max(genre_counts, key=genre_counts.get)

# Display the genre counts and most popular genre
print("Genre Frequency Analysis:")
print("-" * 25)
for genre, count in genre_counts.items():
    print(f"{genre}: {count} users")
    
print("\nMost Popular Genre:", most_popular_genre)
print(f"Listened to by {genre_counts[most_popular_genre]} users")

# Task 3: Finding Users Who Listen to a Specific Artist
# Define the targeted artist
targeted_artist = "The Weeknd"
users_listening = []

# Iterate through user_data with indices
for index, listening_history in enumerate(user_data):
    # Extract the list of artists (second element of the tuple)
    artists = listening_history[1]
    
    # Check if targeted artist is in the list of artists
    if targeted_artist in artists:
        users_listening.append(index)

# Display users who listen to the targeted artist
print("\nUser Targeting Analysis:")
print("-" * 25)
print(f"Users who listen to {targeted_artist}:")

if users_listening:
    for user_index in users_listening:
        print(f"User {user_index}: Genre - {user_data[user_index][0]}, Artists - {', '.join(user_data[user_index][1])}")
    print(f"\nTotal users found: {len(users_listening)}")
else:
    print(f"No users found who listen to {targeted_artist}")

# Additional analysis - Print percentage of users who listen to the targeted artist
percentage = (len(users_listening) / len(user_data)) * 100
print(f"\nPercentage of users who listen to {targeted_artist}: {percentage:.1f}%")

'''# Sample user data (replace with your own data creation)
user_data = [
    ("Rock", ["Metallica", "Guns N' Roses", "AC/DC"]),
    ("Pop", ["Taylor Swift", "Ed Sheeran", "BTS"]),
    ("Hip Hop", ["Drake", "Kendrick Lamar", "J. Cole"]),
    ("Rock", ["Led Zeppelin", "Pink Floyd", "The Who"]),
    ("Pop", ["Ariana Grande", "The Weeknd", "Olivia Rodrigo"]),
]

# Finding most popular genre
genre_counts = {}
for genre, _ in user_data:
  if genre in genre_counts:
    genre_counts[genre] += 1
  else:
    genre_counts[genre] = 1

most_popular_genre = max(genre_counts, key=genre_counts.get)
print("Most popular genre:", most_popular_genre)

# Finding users who listen to a specific artist
target_artist = "BTS"
users_listening = []
for i, (_, artists) in enumerate(user_data):
  if target_artist in artists:
    users_listening.append(i)

if users_listening:
  print(f"Users who listened to {target_artist}:", users_listening)
else:
  print(f"No users listened to {target_artist} this week.")'''