from dotenv import load_dotenv
import os
import requests

load_dotenv() #loads variables from .env

api_key = os.getenv("API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching weather data...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received succesfully")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occured {e}")
        raise

#fetch_data()

