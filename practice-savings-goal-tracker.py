# Define savings goal
savings_goal = 1000

# Prompt user for initial current savings
current_savings = float(input("Enter your current savings amount: $"))

# Initialize the number of months
while current_savings < savings_goal:
    # Prompt user for monthly savings
    monthly_savings = float(input("Enter your monthly savings amount: "))
    # Validate monthly savings
    if monthly_savings <= 0:
        print("Invalid input. Please enter a positive amount.")
        continue  # Skip to the next iteration if input is invalid
    # Update current savings
    current_savings += monthly_savings
    # Display current savings
    print("Current savings amount:", current_savings)
# Check if savings goal is reached
if current_savings >= savings_goal:
    print("Congratulations! You've reached your savings goal of", savings_goal, "dollars!")
else:
    print("You need", savings_goal - current_savings, "more dollars to reach your goal.")
# End of the program