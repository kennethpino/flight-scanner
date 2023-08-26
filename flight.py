class Flight:

    def __init__(self, response):
        self.data = response.json()['data'][0]
        self.price = self.data['price']
        self.city_from = self.data['cityFrom']
        self.city_to = self.data['cityTo']
        self.iata_from = self.data['route'][0]['flyFrom']
        self.iata_to = self.data['route'][0]['flyTo']
        self.local_departure = self.data['route'][0]['local_departure'].split("T")[0]
        self.local_arrival = self.data['route'][0]['local_arrival'].split("T")[0]

        self.info = (f"Low price alert! Only £{self.price} to fly from {self.city_from}-{self.iata_from} to "
                     f"{self.city_to}-{self.iata_to} from {self.local_departure} "
                     f"to {self.local_arrival}")
