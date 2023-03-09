import requests
import os
from dotenv import load_dotenv

load_dotenv()


class SheetyAPI:
    def __init__(self):
        self.url = os.getenv('sheetyURL')
        self.header = {'Authorization': 'Bearer ' + os.getenv('sheetyToken')}

    def get(self):
        response = requests.get(url=self.url, headers=self.header)
        return response.json()

    def post(self, payload):
        response = requests.post(
            url=self.url, json=payload, headers=self.header)
        return response.json()

    def put(self, payload, id):
        response = requests.put(
            url=f'{self.url}/{id}', json=payload, headers=self.header)
        return response.json()

    def delete(self, id):
        response = requests.delete(url=f'{self.url}/{id}', headers=self.header)
        return response.json()
