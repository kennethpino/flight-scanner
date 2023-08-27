import os
import smtplib
from email.message import EmailMessage
from twilio.rest import Client

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_AUTH = os.environ['TWILIO_AUTH']
SENDER = os.environ['SENDER']
RECIPIENT = os.environ['RECIPIENT']
PASSWORD = os.environ['PASSWORD']
SERVER = "smtp.gmail.com"
PORT = 465

class NotificationManager:

    def __init__(self):
        print('Initializing Mobile Messenger.')
        self.t_sid = TWILIO_SID
        self.t_auth = TWILIO_AUTH
        self.client = Client(self.t_sid, self.t_auth)

    def send_sms(self, flight_info, from_, to_):
        print(f'Sending SMS to {to_}')
        # message = self.client.messages.create(body=flight_info, from_=from_, to=to_)
        # print(f'Sending SMS.{message.status}')
        print(f'*** {flight_info}')

    def send_emails(self, flight_info, to_):
        print(f'Sending e-mail to {to_}')
        msg = EmailMessage()
        msg.set_content(flight_info)
        msg['Subject'] = "Latest flight deals!"
        msg['From'] = SENDER
        msg['to'] = to_

        with smtplib.SMTP_SSL(SERVER, PORT) as s:
            s.login(SENDER, PASSWORD)
            s.send_message(msg)

