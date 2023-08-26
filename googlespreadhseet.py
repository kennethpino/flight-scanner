import os

import requests

from seachengine import SearchEngine

SPREAD_SHEET_ID = os.environ['SPREAD_SHEET_ID']
SPREAD_SHEET_ENDPOINT = f'https://api.sheety.co/{SPREAD_SHEET_ID}/flightDeals/prices'
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']


class GoogleSpreadSheet:
    def __init__(self):
        self.endpoint = SPREAD_SHEET_ENDPOINT
        self.search_engine = SearchEngine()
        self.sheety_token = SHEETY_TOKEN

    def update_iata_codes(self):
        """Updates every record on the spreadsheet with the corresponding iata codes for each city"""

        headers = {
            'Authorization': self.sheety_token
        }

        for item in requests.get(self.endpoint).json()['prices']:  # Get list of items in the spreadsheet
            params = {
                'price': {
                    'city': item['city'].title(),
                    'iataCode': self.search_engine.get_iata_code(item['city']),
                    'lowestPrice': item['lowestPrice']
                }
            }
            requests.put(f"{self.endpoint}/{item['id']}", json=params, headers=headers)
