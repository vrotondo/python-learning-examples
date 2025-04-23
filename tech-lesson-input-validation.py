name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty.")
    if not name.isalpha():
        raise ValueError("Name can only contain letters and spaces.")

def validate_age(age):
    if not age.isdigit():
        raise ValueError("Age must be a positive integer.")
    age = int(age)
    if age <= 0:
        raise ValueError("Age must be a positive integer.")

def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty.")
    if "@" not in email:
        raise ValueError("Email must contain '@'.")
    
try:
    validate_name(name)
    validate_age(age)
    validate_email(email)
    print("Registration successful!")
    # Further processing or storage of validated data
except ValueError as e:
    print("Validation error:", str(e))

'''
def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address.")

def validate_license_number(license_number):
    if not license_number.isalnum():
        raise ValueError("Driver's license number should only contain alphanumeric characters.")

def validate_rental_duration(rental_duration):
    if not rental_duration.isdigit() or int(rental_duration) <= 0:
        raise ValueError("Rental duration should be a positive integer.")
email = input("Enter your email address: ")
license_number = input("Enter your driver's license number: ")
rental_duration = input("Enter the rental duration in days: ")
try:
    validate_email(email)
    validate_license_number(license_number)
    validate_rental_duration(rental_duration)
    rental_duration = int(rental_duration)
    print("Reservation successful!")
    # Further processing or storage of validated data
except ValueError as e:
    print("Validation error:", str(e))
'''