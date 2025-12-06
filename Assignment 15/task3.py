import requests
import json

# Weather API Configuration
WEATHER_API_KEY = "e9472d4e16f3bf36ea92d0b4e2bd9e0c"  # Get free key from https://openweathermap.org/api
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


WEATHER_API_KEY = "e9472d4e16f3bf36ea92d0b4e2bd9e0c"  # Get free key from https://openweathermap.org/api
def extract_and_display_weather(city_name, api_key=WEATHER_API_KEY):
    """
    Extract specific fields from weather API response and display in user-friendly format.
    
    Args:
        city_name (str): Name of the city to get weather for
        api_key (str): OpenWeatherMap API key
        
    Returns:
        dict: Extracted weather data or None if error occurs
    """
    
    # API parameters
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use Celsius
    }
    
    try:
        # Send GET request with timeout
        response = requests.get(WEATHER_API_URL, params=params, timeout=5)

        # If response code is not OK, raise an error
        response.raise_for_status()

        # Parse JSON response
        api_response = response.json()

        # Extract specific fields from API response
        city = api_response.get('name', 'N/A')
        temperature = api_response.get('main', {}).get('temp', 'N/A')
        humidity = api_response.get('main', {}).get('humidity', 'N/A')
        weather_description = api_response.get('weather', [{}])[0].get('description', 'N/A').title()

        # Display in user-friendly format (NOT raw JSON)
        print("\n" + "="*50)
        print("WEATHER INFORMATION")
        print("="*50)
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
        print("="*50 + "\n")

        return {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'weather': weather_description
        }

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


def extract_and_display_multiple_cities(cities_list, api_key=WEATHER_API_KEY):
    """
    Extract and display weather data for multiple cities in user-friendly format.
    
    Args:
        cities_list (list): List of city names
        api_key (str): OpenWeatherMap API key
        
    Returns:
        list: List of extracted weather data dictionaries
    """
    results = []
    
    for city in cities_list:
        result = extract_and_display_weather(city, api_key)
        if result:
            results.append(result)
    
    return results


def display_weather_summary(city_name, api_key=WEATHER_API_KEY):
    """
    Display a summary of weather data in a compact user-friendly format.
    
    Args:
        city_name (str): Name of the city
        api_key (str): OpenWeatherMap API key
    """
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params, timeout=5)
        response.raise_for_status()
        api_response = response.json()

        # Extract fields
        city = api_response.get('name', 'N/A')
        temperature = api_response.get('main', {}).get('temp', 'N/A')
        humidity = api_response.get('main', {}).get('humidity', 'N/A')
        weather_description = api_response.get('weather', [{}])[0].get('description', 'N/A').title()

        # Display in compact format
        print(f"• City: {city} | Temp: {temperature}°C | Humidity: {humidity}% | Weather: {weather_description}")

    except Exception as e:
        print(f"❌ Error fetching data for {city_name}: {str(e)}")


# Example usage
if __name__ == "__main__":
    # NOTE: Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
    # Get a free API key from: https://openweathermap.org/api
    
    print("\n" + "="*50)
    print("WEATHER DATA EXTRACTION AND DISPLAY")
    print("="*50)
    
    # Example 1: Single city with detailed display
    print("\n--- Example 1: Detailed Display (London) ---")
    extract_and_display_weather("London")
    
    # Example 2: Multiple cities with detailed display
    print("\n--- Example 2: Multiple Cities (Detailed) ---")
    cities = ["New York", "Paris", "Tokyo", "Sydney"]
    extract_and_display_multiple_cities(cities)
    
    # Example 3: Compact summary display
    print("\n--- Example 3: Compact Summary Display ---")
    for city in ["London", "Berlin", "Amsterdam"]:
        display_weather_summary(city)
