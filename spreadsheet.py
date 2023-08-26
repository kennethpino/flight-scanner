import json
import os

import requests

SPREADSHEET_ID = os.environ['SHEETSON_SPREADSHEET_ID']
SHEETSON_API_KEY = os.environ['SHEETSON_API_KEY']
ENDPOINT_SPREADSHEET = 'https://api.sheetson.com/v2/sheets/prices'


class SpreadSheet:

    def __init__(self):
        print('Initializing Spreadsheet.')
        self.endpoint_spreadsheet = ENDPOINT_SPREADSHEET
        self.records = None

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

        for item in requests.get(self.endpoint_spreadsheet, params=params).json()['results']:
            if len(item['City']) == 0:
                print(f'Updating {item["City"]} IATA Code.')
                params = {
                    'IATA Code': searchengine.search_for_iata_code(item['City'])
                }
                response = requests.put(f"{self.endpoint_spreadsheet}/{item['rowIndex']}", json=params, headers=headers)
                response.raise_for_status()

    def get_records(self):
        print('Getting all records from Spreadsheet.')
        params = {
            'apiKey': SHEETSON_API_KEY,
            'spreadsheetId': SPREADSHEET_ID
        }

        response = requests.get(f'{self.endpoint_spreadsheet}', params=params)
        response.raise_for_status()
        with open('spreadsheet.json', 'w') as file:
            file.write(json.dumps(response.json(), indent=4))
        self.records = response.json()
