class Flight:

    def __init__(self, response, max_stops):
        self.data = response.json()['data'][0]
        self.price = self.data['price']
        self.city_from = self.data['route'][0]['cityFrom']
        self.city_to = self.data['route'][0]['cityTo']
        self.iata_from = self.data['route'][0]['flyFrom']
        self.iata_to = self.data['route'][0]['flyTo']
        self.out_date = self.data['route'][0]['local_departure'].split("T")[0]
        self.return_date = self.data['route'][1]['local_departure'].split("T")[0]
        self.info = (f'Low price alert! Only £{self.price} to fly from {self.city_from}-{self.iata_from} to '
                     f'{self.city_to}-{self.iata_to} from {self.out_date} '
                     f'to {self.return_date}')
        if max_stops > 0:
            self.stop_overs = 1
            self.via_city = self.data["route"][0]["cityTo"]
            self.info += f'Flight has {self.stop_overs} stop over, via {self.via_city}'
