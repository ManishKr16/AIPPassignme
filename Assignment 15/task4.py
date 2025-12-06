import requests
import json

# Weather API Configuration
WEATHER_API_KEY = "e9472d4e16f3bf36ea92d0b4e2bd9e0c"  # Get free key from https://openweathermap.org/api
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_by_city(city_name, api_key=WEATHER_API_KEY):
    """
    Fetch and display weather information for a given city.
    
    Args:
        city_name (str): Name of the city to get weather for
        api_key (str): OpenWeatherMap API key
        
    Returns:
        dict: Weather data dictionary or None if error occurs
    """
    
    # Validate input parameter
    if not city_name or not isinstance(city_name, str):
        print("❌ Error: City name must be a non-empty string.")
        return None
    
    # Strip whitespace and validate
    city_name = city_name.strip()
    if not city_name:
        print("❌ Error: City name cannot be empty.")
        return None
    
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
        country = api_response.get('sys', {}).get('country', '')
        temperature = api_response.get('main', {}).get('temp', 'N/A')
        humidity = api_response.get('main', {}).get('humidity', 'N/A')
        weather_main = api_response.get('weather', [{}])[0].get('main', 'N/A')
        weather_description = api_response.get('weather', [{}])[0].get('description', 'N/A').title()

        # Display in user-friendly format
        print("\n" + "="*50)
        print(f"WEATHER INFORMATION FOR {city.upper()}, {country}")
        print("="*50)
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
        print("="*50 + "\n")

        return {
            'city': city,
            'country': country,
            'temperature': temperature,
            'humidity': humidity,
            'weather_main': weather_main,
            'weather_description': weather_description
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

    # Wrong API key / Unauthorized / Forbidden / Not Found
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("❌ Error: Unauthorized – Invalid or missing API key.")
        elif response.status_code == 403:
            print("❌ Error: Forbidden – You do not have permission to access this resource.")
        elif response.status_code == 404:
            print(f"❌ Error: City '{city_name}' not found. Please check the city name and try again.")
        else:
            print(f"❌ HTTP Error {response.status_code} Occurred: {http_err}")
        return None

    # JSON decoding error
    except json.JSONDecodeError:
        print("❌ Error: Failed to decode API response as JSON.")
        return None

    # Any other unexpected issue
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")
        return None


def get_weather_for_cities(*city_names, api_key=WEATHER_API_KEY):
    """
    Fetch weather information for multiple cities using variable arguments.
    
    Args:
        *city_names: Variable number of city name arguments
        api_key (str): OpenWeatherMap API key
        
    Returns:
        dict: Dictionary containing weather data for all cities
    """
    results = {}
    
    if not city_names:
        print("❌ Error: Please provide at least one city name.")
        return results
    
    for city in city_names:
        result = get_weather_by_city(city, api_key)
        if result:
            results[city] = result
    
    return results


def interactive_weather_lookup(api_key=WEATHER_API_KEY):
    """
    Interactive function for users to look up weather by city name.
    
    Args:
        api_key (str): OpenWeatherMap API key
    """
    print("\n" + "="*50)
    print("INTERACTIVE WEATHER LOOKUP")
    print("="*50)
    print("Enter city names to get weather information.")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("Enter city name: ").strip()
        
        if user_input.lower() == 'quit':
            print("Thank you for using Weather Lookup. Goodbye!")
            break
        
        if not user_input:
            print("❌ Please enter a valid city name.\n")
            continue
        
        get_weather_by_city(user_input, api_key)


# Example usage
if __name__ == "__main__":
    # NOTE: API key is already configured
    
    print("\n" + "="*50)
    print("TASK 4: WEATHER LOOKUP WITH USER INPUT")
    print("="*50)
    
    # Ask user for mode of operation
    print("\nChoose an option:")
    print("1. Interactive Mode (Enter city names one by one)")
    print("2. Demo Mode (See example outputs)")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "1":
        # Interactive mode
        interactive_weather_lookup()
    
    elif choice == "2":
        # Demo mode with examples
        print("\n--- Example 1: Valid City Input ---")
        print("Input: 'New York'")
        get_weather_by_city("New York")
        
        print("\n--- Example 2: Invalid City Input ---")
        print("Input: 'xyz123'")
        get_weather_by_city("xyz123")
        
        print("\n--- Example 3: Another Valid City ---")
        print("Input: 'London'")
        get_weather_by_city("London")
        
        print("\n--- Example 4: Empty String Input ---")
        print("Input: ''")
        get_weather_by_city("")
        
        print("\n--- Example 5: Multiple Cities ---")
        print("Input: 'Paris', 'Tokyo', 'Sydney'")
        print("Getting weather for multiple cities...\n")
        weather_data = get_weather_for_cities("Paris", "Tokyo", "Sydney")
    
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")
