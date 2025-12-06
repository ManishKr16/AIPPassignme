import requests
import json

# Weather API Configuration
WEATHER_API_KEY = "e9472d4e16f3bf36ea92d0b4e2bd9e0c"  # Get free key from https://openweathermap.org/api
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_details(city_name, api_key="e9472d4e16f3bf36ea92d0b4e2bd9e0c"):
    """
    Fetch and display weather details for a city using OpenWeatherMap API.
    
    Args:
        city_name (str): Name of the city to get weather for
        api_key (str): OpenWeatherMap API key
        
    Returns:
        dict: Weather data in JSON format or None if error occurs
    """
    
    # API parameters
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use Celsius
    }
    
    try:
        # Send GET request with a timeout
        response = requests.get(WEATHER_API_URL, params=params, timeout=5)

        # If response code is not OK, raise an error
        response.raise_for_status()

        # Convert to JSON
        data = response.json()
        
        # Extract relevant weather details for cleaner JSON output
        weather_details = {
            "city": data.get('name'),
            "country": data.get('sys', {}).get('country'),
            "temperature": data.get('main', {}).get('temp'),
            "feels_like": data.get('main', {}).get('feels_like'),
            "humidity": data.get('main', {}).get('humidity'),
            "pressure": data.get('main', {}).get('pressure'),
            "weather": data.get('weather', [{}])[0].get('main'),
            "description": data.get('weather', [{}])[0].get('description'),
            "wind_speed": data.get('wind', {}).get('speed'),
            "cloudiness": data.get('clouds', {}).get('all')
        }

        # Print formatted JSON output
        print(f"✔ Weather Details for {city_name} (JSON Format):\n")
        print(json.dumps(weather_details, indent=4))
        
        return weather_details

    # Invalid URL / Missing Schema
    except requests.exceptions.MissingSchema:
        print("❌ Error: The API URL is invalid. Please check the URL.")
        return None

    # DNS failure, no internet, etc.
    except requests.exceptions.ConnectionError:
        print("❌ Error: Failed to connect to the server. Check your network connection.")
        return None

    # Timeout error
    except requests.exceptions.Timeout:
        print("❌ Error: The request timed out. Try again later.")
        return None

    # Wrong API key / Unauthorized / Forbidden
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ Error: Unauthorized – Invalid or missing API key.")
        elif response.status_code == 403:
            print("❌ Error: Forbidden – You do not have permission to access this resource.")
        elif response.status_code == 404:
            print(f"❌ Error: City '{city_name}' not found. Please check the city name.")
        else:
            print(f"❌ HTTP Error Occurred: {http_err}")
        return None

    # JSON decoding error
    except json.JSONDecodeError:
        print("❌ Error: Failed to decode API response as JSON.")
        return None

    # Any other unexpected issue
    except Exception as e:
        print("❌ Unexpected Error:", str(e))
        return None


def get_multiple_cities_weather(cities_list, api_key=WEATHER_API_KEY):
    """
    Fetch weather details for multiple cities.
    
    Args:
        cities_list (list): List of city names
        api_key (str): OpenWeatherMap API key
        
    Returns:
        dict: Combined weather data for all cities
    """
    all_weather_data = {}
    
    for city in cities_list:
        print(f"\n{'='*50}")
        result = get_weather_details(city, api_key)
        if result:
            all_weather_data[city] = result
    
    return all_weather_data


# Run function
if __name__ == "__main__":
    # NOTE: Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
    # Get a free API key from: https://openweathermap.org/api
    
    print("WEATHER API - Error Handling Demo\n")
    print("="*50)
    
    # Example 1: Single city
    print("\n--- Example 1: Single City Weather ---")
    get_weather_details("London")
    
    # Example 2: Multiple cities
    print("\n" + "="*50)
    print("\n--- Example 2: Multiple Cities Weather ---")
    cities = ["New York", "Paris", "Tokyo"]
    weather_data = get_multiple_cities_weather(cities)
