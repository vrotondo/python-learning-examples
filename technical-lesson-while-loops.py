# Defining the step goal
goal_steps = 10000

# Initializing the step count
while True: # Infinite loop (user exits with 'q' or 'quit')
    current_steps = int(input("Enter your current step count (or 'q' to quit): "))

    if current_steps < 0:
        print("Invalid input. Please enter a non-neative step count.")
        continue # Skip to the next iteration if input is invalid

    if current_steps >= goal_steps:
        print("Congratulations! You've reached your step goal of", goal_steps, "steps!")
        break # Exit the loop if goal is reached

    print("Keep going! You need", goal_steps - current_steps, "more steps to reach your goal.")