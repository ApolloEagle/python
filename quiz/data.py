import requests
import json

params = {
    'amount': 10,
    'type': 'boolean'
}
question_data = requests.get(url='https://opentdb.com/api.php',
                             params=params).json().get('results')
