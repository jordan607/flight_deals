import requests

#['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheets_url = ""
        self.sheets_response = []

    def get_sheet_data(self):
        sheets_response_data = requests.get(self.sheets_url)
        self.sheets_response = sheets_response_data.json()["prices"]
        return self.sheets_response

    def update_IATA_codes(self, IATA_codes):
        for i in range(len(IATA_codes)):
            data = {
                "price": {
                "iataCode": IATA_codes[i]
                }
            }
            response = requests.put(url=f"{self.sheets_url}/{self.sheets_response[i]['id']}",json=data)



