import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, cities):
        self.flight_url =""
        self.apikey = ""
        self.term = cities
        self.IATA_codes = []

    def flight_search(self):
        for i in range(len(self.term)):
            term = self.term[i]
            parameters = {
                "apikey": self.apikey,
                "term": term
            }
            try:
                flight_response = requests.get(self.flight_url, params=parameters)
            except IndexError:
                print("No flights found")
                return None
            else:
                self.IATA_codes.append(flight_response.json()["locations"][0]["code"])
        return self.IATA_codes
