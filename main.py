import requests
import os
from dotenv import load_dotenv

load_dotenv()

city = os.getenv('CITY')
API_KEY = os.getenv('WEATHER_API_KEY')

print(API_KEY)

params = {
    'q': city,
    'appid': API_KEY
}

response = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather', params=params)
response.raise_for_status()

print(response.json())
