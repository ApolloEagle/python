import requests
import os
from dotenv import load_dotenv

load_dotenv()


class CurrencyAPI:
    def convert(self, from_country, to_country, amount):
        header = {
            'apikey': os.getenv('fixerToken')
        }

        params = {
            'from': from_country,
            'to': to_country,
            'amount': amount,
        }

        response = requests.get(url='https://api.apilayer.com/fixer/convert',
                                headers=header, params=params)
        response.raise_for_status()

        return response.json()
