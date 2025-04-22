'''
This script takes in three inputs
-Number of rental days : integer
-Cost per day : integer
-Includes weekend or not : (yes/no) string
'''

days = int(input("Enter the number of days the car will be rented for: "))
cost = int(input("What is the current cost per day in dollars?: "))
weekend = input("Does the rental period include a weekend day (yes/no): ")

# Calculate base cost first
base_cost = days * cost

# Check if rental includes a weekend (yes) apply 10% discount
if weekend == "yes":
	total_cost = base_cost * .9
	print(f"The total cost of the car rental for {days} days at ${cost} per day and with a 10% weekend discount comes to {total_cost}")
else:
	print(f"The total cost of the car rental for {days} days at ${cost} per day comes out to {base_cost}")