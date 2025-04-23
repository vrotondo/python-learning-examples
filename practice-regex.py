import re

def test_regex(pattern, test_cases):
    compiled_pattern = re.compile(pattern)
    all_passed = True

    print(f"\nTesting pattern: {pattern}")
    print("-" * 60)

    for test_input, expected in test_cases:
        result = bool(compiled_pattern.fullmatch(test_input))
        passed = result == expected

        status = "Passed" if passed else "Failed"
        expected_str = "Matched" if expected else "Did not match"
        result_str = "Matched" if result else "Did not match"

        print(f"{status} Input: {test_input:<30} Expected: {expected_str:<10} Result: {result_str}")
        
        if not passed:
            all_passed = False

    print("-" * 60)
    print("All tests passed!" if all_passed else "Some tests failed.")
    return all_passed

def explain_pattern(pattern):
    print("\nPattern Explanation:")
    print("-" * 60)

    parts = [
        (r'^', "Start of string"),
        (r'[a-zA-Z0-9._%+-]+', "Username: one or more letters, numbers, or special characters (._%+-)"),
        (r'@', "@ symbol"),
        (r'[a-zA-Z0-9.-]+', "Domain name: one or more letters, numbers, dots, or hyphens"),
        (r'\.', "Dot before the top-level domain"),
        (r'[a-zA-Z]{2,}', "Top-level domain: two or more letters"),
        (r'$', "End of string")
    ]
   
    for component, explanation in parts:
        if component in pattern:
            print(f"{component:<20} : {explanation}")
    
    print("-" * 60)
   
def main():
    email_test_cases = [
        ("user@example.com", True),
        ("john.doe@company.co.uk", True),
        ("jane_doe123@school.edu", True),
        ("test+label@gmail.com", True),
        ("admin@server-name.io", True),
        ("user@domain", False),           # Missing top-level domain
        ("user@.com", False),             # Missing domain name
        ("@domain.com", False),           # Missing username
        ("user@domain..com", False),      # Double dot
        ("user@domain.c", False),         # TLD too short
        ("user space@domain.com", False), # Space in username
        ("user@domain com", False),       # Space in domain
        ("usernamelongerthan64characters" + "x" * 40 + "@domain.com", False) # Too long username
    ]
    
    # Step 1: Simple pattern - just checking for @ symbol
    simple_pattern = r'.+@.+'
    print("STEP 1: Start with a simple pattern")
    test_regex(simple_pattern, email_test_cases)
    
    # Step 2: Basic email pattern with some structure
    basic_pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    print("\nSTEP 2: Add basic structure (letters, numbers, dots)")
    test_regex(basic_pattern, email_test_cases)
    
    # Step 3: Allow more characters in username and domain
    improved_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    print("\nSTEP 3: Allow more special characters and ensure TLD is at least 2 chars")
    test_regex(improved_pattern, email_test_cases)
    
    # Step 4: Add length constraints (simplified for demonstration)
    final_pattern = r'^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    print("\nSTEP 4: Add username length constraint")
    test_regex(final_pattern, email_test_cases)
    
    # Explain the final pattern
    explain_pattern(final_pattern)
    
    print("\nKey Insights from Regex Development:")
    print("1. Start simple, then refine - we began with just checking for @ and gradually added constraints")
    print("2. Each iteration improved the pattern to handle more valid cases while rejecting invalid ones")
    print("3. Documentation is crucial - the pattern explanation helps others understand the regex")
    print("4. Test with diverse examples - our test suite includes various edge cases")

if __name__ == "__main__":
    main()

'''
import re
from datetime import datetime

def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty.")
    if not re.match(r'^[A-Za-z ]+$', name):
        raise ValueError("Name can only contain letters and spaces.")

def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty.")
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError("Invalid email format.")

def validate_dob(dob):
    if not dob:
        raise ValueError("Date of birth cannot be empty.")
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

# Student registration
name = input("Enter your name: ")
email = input("Enter your email address: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    validate_name(name)
    validate_email(email)
    validate_dob(dob)
    
    # If all validations pass, store the data in the database
    print("Student registration successful!")
    # Code to store the data in the database goes here
    
except ValueError as e:
    print(f"Error: {str(e)}")
'''