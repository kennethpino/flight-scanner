import os

from twilio.rest import Client

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_AUTH = os.environ['TWILIO_AUTH']


class MobileMessenger:

    def __init__(self):
        print('Initializing Mobile Messenger.')
        self.t_sid = TWILIO_SID
        self.t_auth = TWILIO_AUTH
        self.client = Client(self.t_sid, self.t_auth)

    def send_sms(self, flight_info, from_, to_):
        # message = self.client.messages.create(body=flight_info, from_=from_, to=to_)
        # print(f'Sending SMS.{message.status}')
        print(f'*** {flight_info}')
