import requests

# Define the API endpoint and parameters
api_key = "11ca5bc346a77d53d4dc1277552ae50f"  # Replace with your actual API key
city = "San Francisco"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send the GET request
response = requests.get(url)

# Convert the response to JSON
data = response.json()

# Extract relevant information
temperature = data["main"]["temp"]
condition = data["weather"][0]["description"]

# Display the result
print(f"The temperature in {city} is {temperature}°C with {condition}.")