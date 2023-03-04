import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import smtplib
import time

load_dotenv()

MY_LAT = os.getenv('LAT')
MY_LONG = os.getenv('LONG')


def in_view():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour = datetime.now().hour

    if sunset < hour < sunrise:
        return True


while True:
    time.sleep(60)
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    if in_view() and is_night():
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                email, email, msg='Subject:ISS\n\nISS is overhead. Look up!')
