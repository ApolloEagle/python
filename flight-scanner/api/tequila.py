import requests
import os
from dotenv import load_dotenv

load_dotenv()


class TequilaAPI:
    def get_iata(self, iata):
        header = {
            'apiKey': os.getenv('tequilaToken')
        }

        params = {
            'term': iata,
            'locale': 'en-US',
            'location_type': 'airport',
            'limit': '10',
            'active_only': 'true'
        }

        response = requests.get(
            url='https://api.tequila.kiwi.com/locations/query', headers=header, params=params)
        return response.json()

    def search_flights(self, fly_from, fly_to):
        header = {
            'apiKey': os.getenv('tequilaToken')
        }

        params = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            # 'date_from': date_from,
            # 'date_to': date_to,
            # 'price_to': price_to
        }

        response = requests.get(
            url='https://api.tequila.kiwi.com/search', headers=header, params=params)
        response.raise_for_status()

        return response.json()
