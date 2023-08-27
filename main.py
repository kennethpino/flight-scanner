import os

from notificationmanager import NotificationManager
from searchengine import SearchEngine
from datamanager import DataManager

FROM_MOBILE = '+18159494549'
TO_MOBILE = os.environ['MY_MOBILE']


class Application:

    def __init__(self):
        print('Launching application.')
        self.searchengine = SearchEngine()
        self.datamanager = DataManager()
        self.notifications_manager = NotificationManager()
        self.datamanager.update_iata_codes(self.searchengine)
        self.datamanager.get_city_records()
        self.searchengine.search_for_flights(self.datamanager.city_records)
        self.datamanager.get_user_records()
        print('SMS Disabled. Printing to console for simulation:')
        for flight in self.searchengine.flights:
            self.notifications_manager.send_sms(flight.info, FROM_MOBILE, TO_MOBILE)
            for record in self.datamanager.user_records['results']:
                self.notifications_manager.send_emails(flight.info, record['Email'])


app = Application()
