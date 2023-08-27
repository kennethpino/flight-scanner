import json
import os

import requests

SPREADSHEET_ID = os.environ['SHEETSON_SPREADSHEET_ID']
SHEETSON_API_KEY = os.environ['SHEETSON_API_KEY']
ENDPOINT_SPREADSHEET_PRICES = 'https://api.sheetson.com/v2/sheets/prices'
ENDPOINT_SPREADSHEET_USERS = 'https://api.sheetson.com/v2/sheets/users'

class DataManager:

    def __init__(self):
        print('Initializing Spreadsheet.')
        self.endpoint_spreadsheet_prices = ENDPOINT_SPREADSHEET_PRICES
        self.endpoint_spreadsheet_users = ENDPOINT_SPREADSHEET_USERS
        self.city_records = None
        self.apiKey_sheetson = SHEETSON_API_KEY
        self.spreadsheetId = SPREADSHEET_ID
        self.user_records = None

    def update_iata_codes(self, searchengine):
        print('Updating IATA Codes.')
        headers = {
            'Authorization': f'Bearer {SHEETSON_API_KEY}',
            'X-Spreadsheet-Id': SPREADSHEET_ID,
            'Content-Type': 'application/json'
        }

        params = {
            'apiKey': SHEETSON_API_KEY,
            'spreadsheetId': SPREADSHEET_ID
        }

        for item in requests.get(self.endpoint_spreadsheet_prices, params=params).json()['results']:
            if len(item['City']) == 0:
                print(f'Updating {item["City"]} IATA Code.')
                params = {
                    'IATA Code': searchengine.search_for_iata_code(item['City'])
                }
                response = requests.put(f"{self.endpoint_spreadsheet_prices}/{item['rowIndex']}", json=params, headers=headers)
                response.raise_for_status()

    def get_city_records(self):
        print('Getting all city_records from Spreadsheet.')
        params = {
            'apiKey': SHEETSON_API_KEY,
            'spreadsheetId': SPREADSHEET_ID
        }

        response = requests.get(f'{self.endpoint_spreadsheet_prices}', params=params)
        response.raise_for_status()
        with open('spreadsheet.json', 'w') as file:
            file.write(json.dumps(response.json(), indent=4))
        self.city_records = response.json()

    def get_user_records(self):
        params = {
            'apiKey': self.apiKey_sheetson,
            'spreadsheetId': self.spreadsheetId
        }

        response = requests.get(url=self.endpoint_spreadsheet_users, params=params)
        response.raise_for_status()
        self.user_records = response.json()
