import os

import requests
from Database import insertValues
from datetime import date, time
from dotenv import load_dotenv

import schedule
import time as tm


def job():
    load_dotenv()  # take environment variables from .env

    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    # making a request
    print("Making the request...")
    response = requests.get(BASE_URL, params={"key": os.getenv("API_KEY"),
                                              "q": "paris"})

    jsonResponse = response.json()

    # getting the strings about date and time
    localDateStr = jsonResponse["location"]["localtime"].split(" ")[0]  # str
    localTimeStr = jsonResponse["location"]["localtime"].split(" ")[1]  # str

    # getting data
    city = jsonResponse["location"]["name"]  # str
    humidity = jsonResponse["current"]["humidity"]  # int
    feelsLike = jsonResponse["current"]["feelslike_c"]  # float
    temperature = jsonResponse["current"]["temp_c"]  # float
    wind = jsonResponse["current"]["wind_kph"]  # float

    # transforming str to date
    splitLocalDateStr = localDateStr.split("-")
    localDate = date(int(splitLocalDateStr[0]),
                     int(splitLocalDateStr[1]),
                     int(splitLocalDateStr[2]))

    # transorming str to time
    splitLocalTimeStr = localTimeStr.split(":")
    localTime = time(int(splitLocalTimeStr[0]), int(splitLocalTimeStr[1]))

    # inserting into the database
    insertValues(
        city=city,
        humidity=humidity,
        dateLocal=localDate,
        timeLocal=localTime,
        wind=wind,
        feelsLike=feelsLike,
        temperture=temperature
    )


job() # calling job immediately

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)


