import requests

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=demo&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['current']['condition']['text']}")
    else:
        print("Failed to retrieve weather data.")

get_weather("London")

if __name__ == "__main__":
    import sys
    city = sys.argv[1] if len(sys.argv) > 1 else "London"
    get_weather(city)