import requests

class User_Interface:
  def __init__(self):
    self.first_name = ""
    self.last_name = ""
    self.email = ""
    self.conf_email = ""
    self.user_url = "https://api.sheety.co/3d4ccf78fe421270fe5ea15bdc02e39f/flightDeals/users"


  def interface(self):
    print("Wlcome to JordanFlightClub\n We find best flight deals and email you")
    self.first_name = input("Enter your first name:\n ")
    self.last_name = input("Enter your last name:\n ")
    self.email = input("Enter your Email:\n ")
    self.conf_email = input("Confirm your Email:\n ")

    self.parameters = {
      "user": {
      "firstName":self.first_name,
      "lastName": self.last_name,
      "email": self.email,
      }
    }

    if self.email == self.conf_email:
      print(self.parameters)
      requests.post(self.user_url, json = self.parameters)
      print("You are in the club!")




