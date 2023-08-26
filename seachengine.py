import os

import requests

ENV_KIWI_API_KEY = os.environ['ENV_KIWI_API_KEY']
ENDPOINT_SEARCH = 'https://api.tequila.kiwi.com'
IATA_CODE_SEARCH_ENDPOINT = '/locations/query'


class SearchEngine:
    def __init__(self):
        self.endpoint = ENDPOINT_SEARCH
        self.endpoint_iata_code = IATA_CODE_SEARCH_ENDPOINT
        self.apikey = ENV_KIWI_API_KEY

    def get_iata_code(self, city):
        params = {
            'term': city,
            'location_types': 'city',
            'limit': 1
        }

        headers = {
            'apikey': self.apikey
        }

        response = requests.get(f'{self.endpoint}{self.endpoint_iata_code}', params=params, headers=headers)
        response.raise_for_status()
        return response.json()['locations'][0]['code']
