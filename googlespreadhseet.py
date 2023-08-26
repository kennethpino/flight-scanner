import json
import os

import requests

from seachengine import SearchEngine

SPREAD_SHEET_ID = os.environ['SPREAD_SHEET_ID']
SPREAD_SHEET_ENDPOINT = f'https://api.sheety.co/{SPREAD_SHEET_ID}/flightDeals/prices'
CITY_WISH_LIST = 'flight_wish_list.json'


def save_data(response):
    with open(CITY_WISH_LIST, 'w') as file:
        file.write(json.dumps(response.json(), indent=4))


def get_city_list():
    """Returns a list of cities previously saved from the online spreadsheet"""
    try:
        with open(CITY_WISH_LIST) as file:
            flight_wish_list_dict = json.load(file)
    except FileNotFoundError:
        print(f'Unable to locate {CITY_WISH_LIST}')
    else:
        return [item['city'] for item in flight_wish_list_dict['prices']]


class GoogleSpreadSheet:
    def __init__(self):
        self.endpoint = SPREAD_SHEET_ENDPOINT
        self.search_engine = SearchEngine()

    def update_iata_codes(self):
        """Updates every record on the spreadsheet with the corresponding iata codes for each city"""
        # Get records from the spreadsheet
        # UNCOMMENT THESE LINES TO PERFORM A REQUEST
        # response = requests.get(self.endpoint)
        # response.raise_for_status()
        # save_data(response)

        city_list = get_city_list()

        self.search_engine.get_iata_code(city_list[0])