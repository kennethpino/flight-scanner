import json
import os

import requests

SPREAD_SHEET_ID = os.environ['SPREAD_SHEET_ID']
ENDPOINT_SPREADSHEET = f'https://api.sheety.co/{SPREAD_SHEET_ID}/flightDeals/prices'
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']


class SpreadSheet:
    def __init__(self):
        self.endpoint_spreadsheet = ENDPOINT_SPREADSHEET
        self.sheety_token = SHEETY_TOKEN
        self.records = None

    def update_iata_codes(self, searchengine):
        headers = {
            'Authorization': self.sheety_token
        }

        for item in requests.get(self.endpoint_spreadsheet).json()['prices']:
            params = {
                'price': {
                    'city': item['city'].title(),
                    'iataCode': searchengine.search_for_iata_code(item['city']),
                    'lowestPrice': item['lowestPrice']
                }
            }
            requests.put(f"{self.endpoint_spreadsheet}/{item['id']}", json=params, headers=headers)

    def get_records(self):
        response = requests.get(self.endpoint_spreadsheet)
        response.raise_for_status()
        with open('spreadsheet.json', 'w') as file:
            file.write(json.dumps(response.json(), indent=4))
        self.records = response.json()
