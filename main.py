from googlespreadhseet import GoogleSpreadSheet


class Application:
    def __init__(self):
        self.flight_wish_list = GoogleSpreadSheet()
        self.flight_wish_list.update_iata_codes()


app = Application()
