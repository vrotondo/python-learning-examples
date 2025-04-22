coin_milestones = [100, 500, 1000]
messages = ["Woah...", "Excellent! *plays guitar solo*", "ALL HAIL THE COIN MASTER!"]

for milestone in coin_milestones:
    # Option 1 (index)
    current_message = messages[coin_milestones.index(milestone)]

    # Print the congratulatory message
    print(current_message)