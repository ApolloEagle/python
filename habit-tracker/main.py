import requests
from datetime import datetime

base = 'https://pixe.la/v1'
username = 'YOUR_USERNAME'
token = 'YOUR_TOKEN'
graphid = 'YOUR_GRAPHID'


def create_user():
    params = {
        'token': token,
        'username': username,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    response = requests.post(url=f'{base}/users', json=params)
    print(response.text)


def create_graph():
    params = {
        'id': graphid,
        'name': 'graph-name',
        'unit': 'commit',
        'type': 'int',
        'color': 'kuro'
    }

    headers = {
        'X-USER-TOKEN': token
    }

    response = requests.post(
        url=f'{base}/users/{username}/graphs', json=params, headers=headers)
    print(response.text)


def post_data():
    params = {
        'date': datetime.now().strftime("%Y%m%d"),
        'quantity': '1',
    }

    headers = {
        'X-USER-TOKEN': token
    }

    response = requests.post(
        url=f'{base}/users/{username}/graphs/{graphid}', headers=headers, json=params)
    print(response.text)


def update_data():
    today = datetime.now().strftime("%Y%m%d")
    params = {
        'quantity': '10',
    }

    headers = {
        'X-USER-TOKEN': token
    }

    response = requests.put(
        url=f'{base}/users/{username}/graphs/{graphid}/{today}', headers=headers, json=params)
    print(response.text)


update_data()
