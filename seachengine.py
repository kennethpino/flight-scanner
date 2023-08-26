import os
import json

import requests

ENV_KIWI_API_KEY = os.environ['ENV_KIWI_API_KEY']
ENDPOINT_SEARCH = 'https://api.tequila.kiwi.com'
IATA_CODE_SEARCH_ENDPOINT = '/locations/query'
CITY_SEARCH_RESULTS = 'city_search_results.json'


def save_data(response):
    with open(CITY_SEARCH_RESULTS, 'w') as file:
        file.write(json.dumps(response.json(), indent=4))


class SearchEngine:
    def __init__(self):
        self.endpoint = ENDPOINT_SEARCH
        self.endpoint_iata_code = IATA_CODE_SEARCH_ENDPOINT
        self.apikey = ENV_KIWI_API_KEY

    def get_iata_code(self, city):
        params = {
            'term': city,
            'location_types': 'city'
        }

        headers = {
            'apikey': self.apikey
        }

        print(f'{self.endpoint}{self.endpoint_iata_code}')

        # response = requests.get(f'{self.endpoint}{self.endpoint_iata_code}', params=params, headers=headers)
        # response.raise_for_status()
        # save_data(response)

        try:
            with open('city_search_results.json') as file:
                city_search_results_dict = json.load(file)
        except FileNotFoundError:
            print(f'Unable to locate {CITY_SEARCH_RESULTS}')
        else:
            print(city_search_results_dict['locations'][0]['code'])

