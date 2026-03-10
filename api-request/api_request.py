from dotenv import load_dotenv
import os
import requests

api_key = os.getenv("API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    response = requests.get(api_url)
    print(response)

fetch_data()