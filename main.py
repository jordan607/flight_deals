#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

#https://dashboard.sheety.co/projects/6047aac66f4f152d9d235d63/sheets/prices
# https://api.sheety.co/3d4ccf78fe421270fe5ea15bdc02e39f/flightDeals/prices
# tequila-api.kiwi.com/

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from ui import User_Interface

IATA_codes = []


try:
    users_email = User_Interface().interface()
    #Data from sheets
    sheet_data = DataManager()
    get_sheet_data = sheet_data.get_sheet_data()
    #print(get_sheet_data)
    cities = [ get_sheet_data[i]["city"] for i in range(len(get_sheet_data))]

    IATA_codes = FlightSearch(cities).flight_search()

    # sheet_data.update_IATA_codes(IATA_codes)
    flight_details = FlightData().flight_data(IATA_codes)
    #print(flight_details)
    for sheet_comp in get_sheet_data:
        for flight_comp in flight_details:
            if sheet_comp["city"] == flight_comp["city_TO"] and sheet_comp["lowestPrice"]> flight_comp["price"]:
                NotificationManager(flight_comp,users_email).email()
except:
    print("Something went wrong")


