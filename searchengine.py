import json
import os
from datetime import datetime as dt

import requests
from dateutil.relativedelta import relativedelta

from flight import Flight

ENV_KIWI_API_KEY = os.environ['ENV_KIWI_API_KEY']
ENDPOINT_SEARCH = 'https://api.tequila.kiwi.com'
ENDPOINT_FLIGHT_SEARCH = '/v2/search'
ENDPOINT_IATA_SEARCH = '/locations/query'
FLY_FROM_IATA = 'BCN'


class SearchEngine:

    def __init__(self):
        print('Initializing Search Engine.')
        self.endpoint_location = ENDPOINT_SEARCH
        self.endpoint_iata_code = ENDPOINT_IATA_SEARCH
        self.endpoint_flight_search = ENDPOINT_FLIGHT_SEARCH
        self.apikey = ENV_KIWI_API_KEY
        self.flights = []

    def search_for_iata_code(self, city):
        print('Looking up IATA Code.')
        params = {
            'term': city,
            'location_types': 'city',
            'limit': 1
        }

        headers = {
            'apikey': self.apikey
        }

        response = requests.get(f'{self.endpoint_location}{self.endpoint_iata_code}', params=params, headers=headers)
        response.raise_for_status()
        return response.json()['locations'][0]['code']

    def search_for_flights(self, spreadsheet_records):
        print('Searching for flights.')
        headers = {
            'apikey': self.apikey
        }

        flights = '{"results":['

        for item in spreadsheet_records['results']:
            print(f'Searching for flights to {item["City"]}')
            params = {
                'fly_from': FLY_FROM_IATA,
                'fly_to': item['IATA Code'],
                'date_from': dt.now().strftime('%d/%m/%Y'),
                'date_to': (dt.now() + relativedelta(months=+6)).strftime('%d/%m/%Y'),
                'price_to': item['Lowest Price'],
                'one_for_city': 1,
                'curr': 'GBP'
            }
            response = requests.get(f'{self.endpoint_location}{self.endpoint_flight_search}', params=params,
                                    headers=headers)
            response.raise_for_status()

            if response.json()['_results'] > 0:
                flights += f"{response.text},"
                flight = Flight(response)
                if flight.price < int(item['Lowest Price']):
                    self.flights.append(flight)

        flights += ']}'

        print(f'{len(self.flights)} flights found.')

        with open('flight_results.json', 'w') as file:
            file.write(flights)
