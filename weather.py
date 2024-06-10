import requests
import sys

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "Guntur"

# Read API key from the file
try:
    with open('api_key.txt', 'r') as file:
        API_KEY = file.read().strip()
except FileNotFoundError:
    print("Error: 'api_key' file not found. Please create the file and add your API key.")
    sys.exit()  # Use sys.exit() to exit the script

# Construct the complete URL
url = f"{BASE_URL}appid={API_KEY}&q={CITY}&units=metric"

# Make the request and get the response
response = requests.get(url)
weather_data = response.json()

# Check if the response contains weather data
if response.status_code == 200:
    main_data = weather_data.get('main', {})
    temperature = main_data.get('temp')
    humidity = main_data.get('humidity')
    condition_data = weather_data.get('weather', [{}])
    condition = condition_data[0].get('description', '')

    print(f"Temperature: {temperature:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")
else:
    print(f"Error: {weather_data.get('message', 'Unable to fetch weather data.')}")
