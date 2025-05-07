from datetime import datetime # Import external module for timestamps

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H: %M: %S")
    with open("user_logs.txt", "a") as file:
        file.write(f"[{timestamp}] {action}\n")

# Logging user actions
log_action("User logged in")
log_action("User updated profile")

def search_logs(keyword):
    with open("user_logs.txt", "r") as file:
        for line in file:
            if keyword in line:
                print(line.strip())

# Searching for logs related to 'profile'
search_logs("profile")

def search_logs_safe(keyword):
    try:
        with open("user_logs.txt", "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
    except FileNotFoundError:
        print("No logs found. Log file does not exist.")

# Example use
search_logs_safe("login")