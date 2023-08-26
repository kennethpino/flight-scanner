class Flight:
    def __init__(self, response):
        self.price = response.json()['data'][0]['price']
        self.city_from = response.json()['data'][0]['cityFrom']
        self.city_to = response.json()['data'][0]['cityTo']
        self.iata_from = response.json()['data'][0]['route'][0]['flyFrom']
        self.iata_to = response.json()['data'][0]['route'][0]['flyTo']
        self.info = f"Low price alert! Only £{self.price} to fly from {self.city_from}-{self.iata_from} to {self.city_to}-{self.iata_to}"

