def calculate_factorial(number):
    if number < 0 or not isinstance(number, int):
        print("Error: Invalid input. Please enter a non-negative integer.")
        return None
    
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    
    return factorial

# Main program
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    result = calculate_factorial(number)
    if result is not None:
        print("The factorial of", number, "is:", result)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")