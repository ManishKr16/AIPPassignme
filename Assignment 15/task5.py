import requests
import json
import os
from datetime import datetime

# Weather API Configuration
WEATHER_API_KEY = "e9472d4e16f3bf36ea92d0b4e2bd9e0c"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Output file configuration
OUTPUT_FILE = "weather_log.txt"


def get_weather_details_json(city_name, api_key=WEATHER_API_KEY):
    """
    Fetch weather details for a city and display as JSON.
    Appends results to a text file in the current directory.
    
    Args:
        city_name (str): Name of the city to get weather for
        api_key (str): OpenWeatherMap API key
        
    Returns:
        dict: Weather data in JSON format or None if error occurs
    """
    
    # Validate input parameter
    if not city_name or not isinstance(city_name, str):
        error_msg = "❌ Error: City name must be a non-empty string."
        print(error_msg)
        log_to_file(error_msg)
        return None
    
    # Strip whitespace and validate
    city_name = city_name.strip()
    if not city_name:
        error_msg = "❌ Error: City name cannot be empty."
        print(error_msg)
        log_to_file(error_msg)
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

        # Extract relevant weather details for JSON output
        weather_details = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "city": api_response.get('name'),
            "country": api_response.get('sys', {}).get('country'),
            "latitude": api_response.get('coord', {}).get('lat'),
            "longitude": api_response.get('coord', {}).get('lon'),
            "temperature": api_response.get('main', {}).get('temp'),
            "feels_like": api_response.get('main', {}).get('feels_like'),
            "temp_min": api_response.get('main', {}).get('temp_min'),
            "temp_max": api_response.get('main', {}).get('temp_max'),
            "pressure": api_response.get('main', {}).get('pressure'),
            "humidity": api_response.get('main', {}).get('humidity'),
            "weather": api_response.get('weather', [{}])[0].get('main'),
            "description": api_response.get('weather', [{}])[0].get('description'),
            "wind_speed": api_response.get('wind', {}).get('speed'),
            "wind_degree": api_response.get('wind', {}).get('deg'),
            "cloudiness": api_response.get('clouds', {}).get('all'),
            "visibility": api_response.get('visibility'),
            "sunrise": api_response.get('sys', {}).get('sunrise'),
            "sunset": api_response.get('sys', {}).get('sunset')
        }

        # Display JSON output to console
        print("\n✔ Weather Details (JSON Format):\n")
        print(json.dumps(weather_details, indent=4))

        # Log to file
        log_to_file(json.dumps(weather_details, indent=4))
        
        return weather_details

    # Invalid URL / Missing Schema
    except requests.exceptions.MissingSchema:
        error_msg = "❌ Error: The API URL is invalid. Please check the URL."
        print(error_msg)
        log_to_file(error_msg)
        return None

    # DNS failure, no internet, etc.
    except requests.exceptions.ConnectionError:
        error_msg = "❌ Error: Failed to connect to the server. Check your network connection."
        print(error_msg)
        log_to_file(error_msg)
        return None

    # Timeout error
    except requests.exceptions.Timeout:
        error_msg = "❌ Error: The request timed out. Try again later."
        print(error_msg)
        log_to_file(error_msg)
        return None

    # Wrong API key / Unauthorized / Forbidden / Not Found
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            error_msg = "❌ Error: Unauthorized – Invalid or missing API key."
        elif response.status_code == 403:
            error_msg = "❌ Error: Forbidden – You do not have permission to access this resource."
        elif response.status_code == 404:
            error_msg = f"❌ Error: City '{city_name}' not found. Please check the city name and try again."
        else:
            error_msg = f"❌ HTTP Error {response.status_code} Occurred: {http_err}"
        
        print(error_msg)
        log_to_file(error_msg)
        return None

    # JSON decoding error
    except json.JSONDecodeError:
        error_msg = "❌ Error: Failed to decode API response as JSON."
        print(error_msg)
        log_to_file(error_msg)
        return None

    # Any other unexpected issue
    except Exception as e:
        error_msg = f"❌ Unexpected Error: {str(e)}"
        print(error_msg)
        log_to_file(error_msg)
        return None


def log_to_file(content):
    """
    Append weather details or errors to a text file in the current directory.
    
    Args:
        content (str): Content to append to the file
    """
    try:
        # Get current directory
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, OUTPUT_FILE)
        
        # Append to file with separator
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*80 + "\n")
            f.write(f"Logged at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*80 + "\n")
            f.write(content)
            f.write("\n\n")
        
        # Notify user
        print(f"\n✓ Data logged to: {file_path}")
        
    except IOError as e:
        print(f"❌ Error writing to file: {str(e)}")


def get_multiple_cities_json(cities_list, api_key=WEATHER_API_KEY):
    """
    Fetch and display weather data for multiple cities as JSON.
    
    Args:
        cities_list (list): List of city names
        api_key (str): OpenWeatherMap API key
        
    Returns:
        list: List of weather data dictionaries
    """
    results = []
    
    for city in cities_list:
        print(f"\nFetching weather for {city}...")
        result = get_weather_details_json(city, api_key)
        if result:
            results.append(result)
    
    return results


def display_log_file():
    """
    Display the contents of the weather log file.
    """
    file_path = os.path.join(os.getcwd(), OUTPUT_FILE)
    
    if not os.path.exists(file_path):
        print(f"❌ Log file not found at: {file_path}")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("\n" + "="*80)
        print("WEATHER LOG FILE CONTENTS")
        print("="*80)
        print(content)
        print("="*80)
        
    except IOError as e:
        print(f"❌ Error reading file: {str(e)}")


def clear_log_file():
    """
    Clear/reset the weather log file.
    """
    file_path = os.path.join(os.getcwd(), OUTPUT_FILE)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"Weather Log File\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        print(f"✓ Log file cleared and reset: {file_path}")
        
    except IOError as e:
        print(f"❌ Error clearing file: {str(e)}")


# Interactive menu
def interactive_menu(api_key=WEATHER_API_KEY):
    """
    Interactive menu for weather lookup and log management.
    
    Args:
        api_key (str): OpenWeatherMap API key
    """
    print("\n" + "="*80)
    print("WEATHER API WITH FILE LOGGING")
    print("="*80)
    print("\nOptions:")
    print("1. Get weather for a city")
    print("2. Get weather for multiple cities")
    print("3. View weather log file")
    print("4. Clear weather log file")
    print("5. Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            city = input("Enter city name: ").strip()
            if city:
                get_weather_details_json(city, api_key)
            else:
                print("❌ Please enter a valid city name.")
        
        elif choice == "2":
            cities_input = input("Enter city names separated by commas (e.g., London, Paris, Tokyo): ").strip()
            if cities_input:
                cities = [city.strip() for city in cities_input.split(',')]
                get_multiple_cities_json(cities, api_key)
            else:
                print("❌ Please enter at least one city name.")
        
        elif choice == "3":
            display_log_file()
        
        elif choice == "4":
            confirm = input("Are you sure you want to clear the log file? (yes/no): ").strip().lower()
            if confirm == 'yes':
                clear_log_file()
            else:
                print("Clear operation cancelled.")
        
        elif choice == "5":
            print("\nThank you for using Weather API Logger. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")
        
        print()


# Example usage
if __name__ == "__main__":
    # Show menu options
    print("\n" + "="*80)
    print("TASK 5: WEATHER API WITH JSON OUTPUT AND FILE LOGGING")
    print("="*80)
    print("\nChoose mode:")
    print("1. Interactive Mode")
    print("2. Demo Mode (predefined examples)")
    
    mode_choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if mode_choice == "1":
        interactive_menu()
    
    elif mode_choice == "2":
        # Demo mode
        print("\n--- Demo: Getting weather for New York ---")
        get_weather_details_json("New York")
        
        print("\n--- Demo: Getting weather for London ---")
        get_weather_details_json("London")
        
        print("\n--- Demo: Getting weather for invalid city (xyz123) ---")
        get_weather_details_json("xyz123")
        
        print("\n--- Demo: View log file ---")
        display_log_file()
    
    else:
        print("❌ Invalid choice. Please run the script again.")
