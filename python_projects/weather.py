import requests

# Example weather API (replace with a real API endpoint)
API_KEY = 'your_api_key'
CITY = 'London'
URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}'

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Print relevant weather info
temperature = data['current']['temp_c']
description = data['current']['condition']['text']
print(f'Temperature: {temperature}°C')
print(f'Weather: {description}')
