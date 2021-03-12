import requests

#['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheets_url = ""
        self.users_url = ""
        self.sheets_response = []

    def get_sheet_data(self):
        try:
            sheets_response_data = requests.get(self.sheets_url)
        except IndexError:
            print("No data found")
            return None
        else:
            self.sheets_response = sheets_response_data.json()["prices"]
            return self.sheets_response

    def update_IATA_codes(self, IATA_codes):
        for i in range(len(IATA_codes)):
            data = {
                "price": {
                "iataCode": IATA_codes[i]
                }
            }
            try:
                requests.put(url=f"{self.sheets_url}/{self.sheets_response[i]['id']}",json=data)
            except:
                print("unable to update data")



    def get_users(self):
        try:
            response = requests.get(url=self.users_url)
        except IndexError:
            print("unable to get users")
            return None
        else:
            return [users["email"] for users in response.json()["users"]]


