import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, cities):
        self.flight_url ="https://tequila-api.kiwi.com/locations/query"
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

            flight_response = requests.get(self.flight_url, params=parameters)
            self.IATA_codes.append(flight_response.json()["locations"][0]["code"])
        return self.IATA_codes
