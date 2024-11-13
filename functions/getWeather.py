import os
import requests
from difflib import get_close_matches

# Retrieve the API key from environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Known cities for close matching
KNOWN_CITIES = ["Seoul", "Tokyo", "New York", "London", "Paris", "Ulan Bator", "Beijing", "Shanghai"]

def correct_city_name(city):
    # Find the closest match for the city name
    matches = get_close_matches(city, KNOWN_CITIES, n=1, cutoff=0.7)
    return matches[0] if matches else city

def get_weather_response(user_input, default_city="Ulan Bator"):
    words = user_input.split()
    city = None

    # Identify the city in user input if available
    for word in words:
        potential_city = word.capitalize()
        if potential_city in KNOWN_CITIES:
            city = potential_city
            break

    city = correct_city_name(city) if city else default_city

    # API request URL
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        data = response.json()
        description = data["current"]["condition"]["text"].lower()
        temp = data["current"]["temp_c"]
        return f"The weather in {city} is {description} with a temperature of {temp}°C."

    except requests.exceptions.RequestException as e:
        return f"Sorry, I couldn't retrieve the weather information. Error: {e}"

