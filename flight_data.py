import  requests
import datetime as dt
from pprint import pprint


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.api_key = ""
        self.fly_from = "LON"
        self.fly_to = ""
        self.date_from = (dt.date.today() + dt.timedelta(days = 1)).strftime("%d/%m/%Y"),
        self.date_to = (dt.date.today() + dt.timedelta(days = 180)).strftime("%d/%m/%Y")
        self.flight_type = "round"
        self.max_stopovers = 0
        self.nights_in_dst_from= 7
        self.nights_in_dst_to = 28
        self.sort = "price"
        self.curr = "GBP"
        self.limit = 10
        self.list_of_data = []

        self.flight_url = "https://tequila-api.kiwi.com/v2/search"

    def flight_data(self, destination_list):
        self.parameters = {
            "apikey": self.api_key,
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "nights_in_dst_from":self.nights_in_dst_from,
            "nights_in_dst_to":self.nights_in_dst_to,
            "flight_type": self.flight_type,
            "max_stopovers":self.max_stopovers,
            "sort": self.sort,
            "limit": self.limit,
            "curr": self.curr,
            "fly_days_type":"departure",
            "ret_fly_days_type":"departure"
        }
        for destination in destination_list:
            self.parameters["fly_to"] = destination

            flight_response = requests.get(self.flight_url, params=self.parameters)
            data = flight_response.json()["data"][0]
            city_From = data["cityFrom"]
            city_Code_From = data["cityCodeFrom"]
            city_TO= data["cityTo"]
            city_Code_TO=data["cityCodeTo"]

            price = data["price"]
            departure_date = data["local_departure"].split("T")[0]
            arrival_date = data["route"][1]["local_departure"].split("T")[0]
            city_dict = {"city_TO": city_TO, "price": price, "city_From" : city_From, "city_Code_From" : city_Code_From,
                         "city_Code_TO" : city_Code_TO, "departure_date": departure_date,
                         "arrival_date": arrival_date}
            self.list_of_data.append(city_dict)
        return self.list_of_data


