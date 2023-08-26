import os

from mobilemessenger import MobileMessenger
from searchengine import SearchEngine
from spreadsheet import SpreadSheet

FROM_MOBILE = '+18159494549'
TO_MOBILE = os.environ['MY_MOBILE']


class Application:

    def __init__(self):
        print('Launching application.')
        self.searchengine = SearchEngine()
        self.spreadsheet = SpreadSheet()
        self.mobilemessenger = MobileMessenger()
        self.spreadsheet.update_iata_codes(self.searchengine)
        self.spreadsheet.get_records()
        self.searchengine.search_for_flights(self.spreadsheet.records)
        print('SMS Disabled. Printing to console for simulation:')
        for flight in self.searchengine.flights:
            self.mobilemessenger.send_sms(flight.info, FROM_MOBILE, TO_MOBILE)


app = Application()
