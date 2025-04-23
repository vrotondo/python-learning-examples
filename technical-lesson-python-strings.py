# Getting user input
password = input("Enter your password: ")

# Checking password length
min_length = 8 # Define minimum password length
password_length = len(password) # Get the length of the password
if password_length < min_length:
    print(f"Password must be at least {min_length} characters long.")
else:
    print(f"Password length is valid: {password_length} characters.")

# Validating character types
has_uppercase = False
has_lowercase = False
has_number = False
has_symbol = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_number = True
    elif not char.isalnum(): # Check for symbols
        has_symbol = True

# Evaluating password strength
if has_uppercase and has_lowercase and has_number and has_symbol:
    print("Password is strong.")
else:
    print("Password is weak. It must contain at least one uppercase letter, one lowercase letter, one number, and one symbol.")
    if not has_uppercase:
        print("Add at least one uppercase letter.")
    if not has_lowercase:
        print("Add at least one lowercase letter.")
    if not has_number:
        print("Add at least one number.")
    if not has_symbol:
        print("Add at least one symbol.")

'''
# Minimum password length
min_length = 8

# Get user input
password = input("Enter your password: ")

# Check password length
password_length = len(password)
if password_length < min_length:
    print(f"Password is too short. Minimum length is {min_length} characters.")
else:
    # Initialize tracking variables
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_symbol = False

    # Validate character types
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():  # Check for symbols (not alphanumeric)
            has_symbol = True

    # Evaluate password strength
    if has_uppercase and has_lowercase and has_number and has_symbol:
        print("Strong password! You're using a good mix of characters.")
    else:
        print("Password could be improved. Consider including:")
        if not has_uppercase:
            print("- Uppercase letters (A-Z)")
        if not has_lowercase:
            print("- Lowercase letters (a-z)")
        if not has_number:
            print("- Numbers (0-9)")
        if not has_symbol:
            print("- Symbols (e.g., !@#$%^&*)")'''