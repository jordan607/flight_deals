import smtplib
#£
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self, flight_details):
        self.flight = flight_details
        self.my_email = "vishal@outlook.com"
        self.to_mail = "vishal@gmail.com"
        self.password = ""


    def email(self):
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email,password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.to_mail,
                msg=f"Subject: Low Price Alert !!! \n\n Only {self.flight['price']} pounds"
                    f"to fly from  {self.flight['city_From']}-{self.flight['city_Code_From']}"
                    f" to {self.flight['city_TO']}-{self.flight['city_Code_TO']}, "
                    f"from {self.flight['departure_date']} to {self.flight['arrival_date']}",
            )
