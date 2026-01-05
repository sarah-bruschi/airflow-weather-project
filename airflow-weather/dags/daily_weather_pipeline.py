from airflow.sdk import Asset, dag, task
from datetime import datetime
from include.weather_api import fetch_weather


@dag(
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def daily_weather_pipeline():

    @task()
    def fetch_weather_task(date):
       """
       Task to fetch weather data for a given date.
       """
       return fetch_weather(date)
    
    @task()
    def validate_weather(weather_json: dict):
        """Validate JSON has the expected keys"""
        if "hourly" not in weather_json:
            raise ValueError("Missing 'hourly' key in weather data")
        print("Validation passed")
        return weather_json
       
    weather_data = fetch_weather_task("{{ ds }}")
    validated = validate_weather(weather_data)

daily_weather_pipeline()