from datetime import datetime as dt


class Flight:
    def __init__(self, response):
        self.price = response.json()['data'][0]['price']
        self.city_from = response.json()['data'][0]['cityFrom']
        self.city_to = response.json()['data'][0]['cityTo']
        self.iata_from = response.json()['data'][0]['route'][0]['flyFrom']
        self.iata_to = response.json()['data'][0]['route'][0]['flyTo']
        self.local_departure = response.json()['data'][0]['route'][0]['local_departure'].split("T")[0]
        self.local_arrival = response.json()['data'][0]['route'][0]['local_arrival'].split("T")[0]

        self.info = (f"Low price alert! Only £{self.price} to fly from {self.city_from}-{self.iata_from} to "
                     f"{self.city_to}-{self.iata_to} from {dt.strptime(self.local_departure, '%Y-%m-%d')} "
                     f"to {dt.strptime(self.local_arrival, '%Y-%m-%d')}")
