import requests
import json
import os

def get_weather_data(city, api_key="e9472d4e16f3bf36ea92d0b4e2bd9e0c"
):
    # Geocoding to get coordinates
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    
    response = requests.get(geocoding_url)
    location = response.json()['results'][0]
    
    # Get weather data with optional API key
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
    
    headers = {}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'
    
    weather_response = requests.get(weather_url, headers=headers)
    weather_data = weather_response.json()
    
    # Combine and display
    combined_data = {
        "city": location['name'],
        "country": location.get('country'),
        "weather": weather_data['current']
    }
    
    print("✔ Weather Details (JSON):\n")
    print(json.dumps(combined_data, indent=4))

# Run function with API key from environment variable
api_key = os.getenv('WEATHER_API_KEY')
get_weather_data("London", api_key)
