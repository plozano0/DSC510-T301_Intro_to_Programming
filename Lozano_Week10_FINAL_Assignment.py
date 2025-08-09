# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Peter Lozano
# 08/08/2025
# ####################### Assignment Details ###########################
# Purpose of program:
# 1. Program will return unique word count based on provided text file.
# 2. Program will remove punctuation from words and convert the words.
#   to a common case, and remove any whitespace.
# 3. Program should contain 4 main functions:
#    3a. add_word - adds each word in file.
#    3b. process_line - convert words to common case.
#    3c. pretty_print - prints the results in a legible format.

import requests
import os

# --- Hardcoded values for GET request ---
API_KEY = "f53e22d038e2d31de9e623faf7ea1003"
GEO_API_URL = "http://api.openweathermap.org/geo/1.0/"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_geo_coordinates(location_info: str
                        , api_key: str) -> tuple | None:
    """
    Gets geographic coordinates (latitude, longitude)
        for a given location.

    :Args:
        location_info: A string representing the location
            (e.g., "90210,US" or "London,GB").
        api_key: The API key for OpenWeatherMap.

    :Returns:
        A tuple containing (latitude, longitude, location_name) on
            success, or None on failure.
    """
    parameters = {
        'q': location_info,
        'limit': 1,
        'appid': api_key
    }
    # For zip codes, the API expects 'zip={zip_code},{country_code}'
    # For cities, 'q={city_name},{state_code},{country_code}'
    if location_info.split(',')[0].strip().isdigit():
        geo_url = f"{GEO_API_URL}zip"
        parameters = {'zip': location_info, 'appid': api_key}
    else:
        geo_url = f"{GEO_API_URL}direct"
        parameters = {'q': location_info, 'limit': 1, 'appid': api_key}

    try:
        response = requests.get(geo_url, params=parameters, timeout=5)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        data = response.json()

        # The 'direct' endpoint returns a list, 'zip' returns a dict.
        if isinstance(data, list):
            if not data:
                print("Error: Location not found. "
                      "Please check your city and state."
                )
                return None
            location_data = data[0]
            lat = location_data.get('lat')
            lon = location_data.get('lon')
            name = location_data.get('name', 'Unknown')
            state = location_data.get('state', '')
            country = location_data.get('country', '')
            location_name = f"{name}, {state}, {country}".strip(', ')
        else:  # Handle zip code response
            lat = data.get('lat')
            lon = data.get('lon')
            name = data.get('name', 'Unknown')
            country = data.get('country', '')
            location_name = f"{name}, {country}".strip(', ')

        if lat is None or lon is None:
            print("Error: Could not retrieve valid coordinates.")
            return None

        return lat, lon, location_name

    except requests.exceptions.Timeout:
        print("Error: The request timed out. "
              "Please try again later."
        )
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. "
              "Check your internet connection."
        )
        return None
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            print("Error: Authentication failed. "
                  "Please check your API key."
            )
        else:
            print("Error: Zip Code not found. "
                  "Please only use valid US Zip Codes."
            )
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error: An unexpected error occurred: {err}")
        return None


def get_weather_data(lat: float
                     , lon: float
                     , api_key: str
                     # Standard is in Kelvin (K). Imperial is °F
                     , units: str = 'imperial') -> dict | None:
    """
    Gets weather data using latitude and longitude.

    :Args:
        lat: Latitude of the location.
        lon: Longitude of the location.
        api_key: The API key for OpenWeatherMap.
        units: The unit system
        ('imperial' for Fahrenheit, 'metric' for Celsius).

    :Returns:
        Dictionary containing weather data on success,
        or None on failure.
    """
    parameters = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': units
    }
    try:
        response = requests.get(WEATHER_API_URL
                                , params=parameters
                                , timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: The weather data request timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the weather service.")
        return None
    except requests.exceptions.RequestException as err:
        print("Error: An unexpected error occurred while fetching "
              f"weather: {err}"
        )
        return None


def display_weather(weather_data: dict
                    , location_name: str
                    , units: str = 'imperial'):
    """
    Displays the parsed weather data in a readable format.

    :Args:
        weather_data: A dictionary of weather information from the API.
        location_name: The formatted name of the location.
        units: The unit system to display correct symbols.
    """
    if not weather_data:
        print("Cannot display weather data as none was provided.")
        return

    temp_unit = "°F" if units == 'imperial' else "°C"

    # Extract data using .get() and avoid errors
    #   if a key is missing
    main_weather = weather_data.get('weather'
                                    , [{}]
                                    )[0].get('main', 'N/A')
    # Description provides details of main_weather
    #   (e.g., heavy intensity rain)
    description = weather_data.get('weather'
                                   , [{}]
                                   )[0].get('description', 'N/A')
    temp = weather_data.get('main'
                            , {}
                            ).get('temp', 'N/A')
    feels_like = weather_data.get('main'
                                  , {}
                                  ).get('feels_like', 'N/A')
    temp_min = weather_data.get('main'
                                , {}
                                ).get('temp_min', 'N/A')
    temp_max = (weather_data.get('main'
                                , {}
                                 ).get('temp_max', 'N/A'))
    pressure = weather_data.get('main'
                                , {}
                                ).get('pressure', 'N/A')
    humidity = weather_data.get('main'
                                , {}
                                ).get('humidity', 'N/A')
    cloud_coverage = weather_data.get('clouds'
                                      , {}
                                      ).get('all', 'N/A')
    wind_speed = weather_data.get('wind'
                                  , {}
                                   ).get('speed', 'N/A')
    visibility = weather_data.get('visibility', 'N/A')

    # Max visibility = 10,000
    percentage_visibility = (float(visibility) / 10000) * 100

    print("\n" + "=" * 40)
    print(f"Weather Forecast for: {location_name}")
    print("=" * 40)
    print(f"Conditions:       {main_weather} ({description})")
    print(f"Temperature:      {temp}{temp_unit}")
    print(f"Feels Like:       {feels_like}{temp_unit}")
    print(f"Wind Speed:       {wind_speed} m/s")
    print("-" * 20)
    print(f"High Temp:        {temp_max}{temp_unit}")
    print(f"Low Temp:         {temp_min}{temp_unit}")
    print("-" * 20)
    print(f"Pressure:         {pressure} hPa")
    print(f"Humidity:         {humidity}%")
    print(f"Cloud Coverage:   {cloud_coverage}%")
    print(f"Visibility:       {percentage_visibility:.0f}%")
    print("=" * 40 + "\n")


def get_lookup_choice() -> str:
    """
    Prompts the user to choose their lookup method and
        validates the input.

    :Returns:
        The validated user choice ('1' or '2').
    """
    while True:
        print("How would you like to look up the weather?")
        print("  1. By US Zip Code")
        print("  2. By City and State")
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            return choice
        print("Invalid input. Please enter '1' or '2'.\n")


def get_location_query(choice: str) -> str | None:
    """
    Gets the location query from the user based on their chosen method.

    :Parameter:
        choice: The lookup method ('1' for zip, '2' for city/state).

    :Returns:
        A formatted query string for the API, or None.
    """
    if choice == '1':  # Zip Code Lookup
        while True:
            zip_code = input("Enter the 5-digit US zip code: ").strip()

            # Error handling prior to sending GET request to API
            if len(zip_code) == 5 and zip_code.isdigit():
                # Format for Geocoding API: zip_code, country_code
                return f"{zip_code},US"
            print("Invalid zip code. Please enter exactly 5 digits.")

    elif choice == '2':  # City/State Lookup
        city = input("Enter the city: ").strip()
        state = input("Enter the 2-letter state abbreviation "
                      "(e.g., NC, CA): "
        ).strip()

        if not city or not state:
            print("City and state cannot be empty.")
            return None

        # Error handling prior to sending GET request to API
        if len(state) != 2 or not state.isalpha():
            print("Invalid state abbreviation. "
                  "Please enter a 2-letter code."
            )
            return None
        # Format for Geocoding API: city, state_code, country_code
        return f"{city},{state},US"
    return None


def main():
    """Main function to run the weather application.
    Order of application:
    1. Receives choice from user.
    2. Receives location query from user.
    3. Sends GET request to OpenWeatherMap API.
    4. Parses and displays the weather data.
    5. Asks user if they want to run again.
    """
    print(f'\'{os.path.basename(__file__)}\'\n')
    print("--- Welcome to the Python Weather App ---")

    while True:
        choice = get_lookup_choice()
        location_query = get_location_query(choice)

        if location_query:
            # Step 1: Get geographic coordinates
            geo_info = get_geo_coordinates(location_query, API_KEY)

            if geo_info:
                lat, lon, location_name = geo_info
                # Step 2: Get weather data using coordinates
                weather_data = get_weather_data(lat, lon, API_KEY)

                if weather_data:
                    # Step 3: Display the weather
                    display_weather(weather_data, location_name)

        # Ask to run again
        while True:
            again = input(
                "Look up another location? (y/n): "
            ).strip().lower()
            if again in [
                 'yes'
                , 'yea'
                , 'yep'
                , 'yes sir'
                , 'y'
                , 'nah'
                , 'na'
                , 'nope'
                , 'not a chance'
                , 'no'
                , 'n'
            ]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if again in [
             'nah'
            , 'na'
            , 'nope'
            , 'not a chance'
            , 'no'
            , 'n'
        ]:
            break

    print("\nThank you for using the Weather App. Goodbye!")


if __name__ == "__main__":
    main()