# Task 1: Define Star Milestones and Messages
star_milestones = [10, 50, 100]
achievement_messages = [
    "Great start! You've earned 10 stars!",
    "Halfway there! 50 stars earned!",
    "Wow! You're a star master with 100 stars!"
]

# Task 2 & 3: Iterate Through Milestones and Print Achievement Messages
for milestone in star_milestones:
    # Find the corresponding message for the current milestone
    message_index = star_milestones.index(milestone)
    current_message = achievement_messages[message_index]
    
    # Print the achievement message
    print(current_message)

# Optional: Display total number of milestones
print(f"\nCongratulations! You've reached {len(star_milestones)} milestones in total!")