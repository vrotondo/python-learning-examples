# Package to generate a random number
import random

# Define the random value, integer between 0 and 10
value = random.randint(0,10)

# Define the user inputted guess and make it an integer
guess = int(input("Please guess a number between 0 and 10: ")) # input by default will return a string type

# Construct the if-elif-else block
if guess == value:
	print("You guessed correctly!")
elif guess < value:
	print(f"Your guess was too low, the actual number was {value}")
else: # Use an else statement here
	print(f"Your guess was too high, the actual number was {value}") 