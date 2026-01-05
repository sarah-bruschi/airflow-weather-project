import requests
import json
import os

# Configuration
LAT = 39.7392      
LON = -104.9903     
BASE_PATH = os.path.join(os.getcwd(), "data/raw")
os.makedirs(BASE_PATH, exist_ok=True)

def fetch_weather(date: str):
    """
    Fetches hourly temperature data from Open-Meteo for a given date.
    Saves the raw JSON locally for further processing.
    
    Args:
        date (str): Date string in YYYY-MM-DD format
    """

    # Build API URL
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        f"&hourly=temperature_2m"
        f"&start_date={date}&end_date={date}"
    )

    # Make the request
    response = requests.get(url)
    response.raise_for_status()
    weather_data = response.json()


    print(f"Fetched weather data for {date}, size={len(str(weather_data))} chars")
    return weather_data
