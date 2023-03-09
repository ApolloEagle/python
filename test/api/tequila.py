import requests
import os
from dotenv import load_dotenv

load_dotenv()


class TequilaAPI:
    def __init__(self):
        self.url = 'https://api.tequila.kiwi.com/locations/query'
        self.api_key = os.getenv('tequilaToken')

    def get(self, iata):
        header = {
            'apiKey': self.api_key
        }

        params = {
            'term': iata,
            'locale': 'en-US',
            'location_type': 'airport',
            'limit': '10',
            'active_only': 'true'
        }

        response = requests.get(url=self.url, headers=header, params=params)
        return response.json()
