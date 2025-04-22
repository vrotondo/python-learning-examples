import random

# Define desired outcome and number of occurrences
desired_outcome = "heads"  # Or "tails"
num_occurrences = 3

# Initialize counters
total_tosses = 0
occurrences = 0

# Start the loop
while occurrences < num_occurrences:
  # Simulate coin toss (random choice)
  toss_result = random.choice(["heads", "tails"])
  total_tosses += 1

  # Check if the toss matches the desired outcome
  if toss_result == desired_outcome:
    occurrences += 1  # Increment counter for desired outcome

# Loop finishes when desired outcome happens enough times

# Display results
print("Total tosses:", total_tosses)
print(desired_outcome, "occurred", occurrences, "times")