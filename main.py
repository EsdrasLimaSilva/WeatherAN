import os
import sys

# *************  activating virtual environment ****************
venv_folder = os.path.join(os.path.dirname(sys.argv[0]), 'venv')
activate_this = os.path.join(venv_folder, 'bin', 'activate_this.py')

try:
    exec(open(activate_this).read(), dict(__file__=activate_this))
except FileNotFoundError:
    print("Virtual environment not found.")
    sys.exit(1)

# ************ actual code *****************

import requests
from Database import insertValues
from datetime import date, time
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env


BASE_URL = "http://api.weatherapi.com/v1/current.json"

# making a request
print("Making the request...")
response = requests.get(BASE_URL, params={"key": os.getenv("API_KEY"),
                                          "q": "paris"})

jsonResponse = response.json()

# getting the strings about date and time
localDateStr = jsonResponse["location"]["localtime"].split(" ")[0] #str
localTimeStr = jsonResponse["location"]["localtime"].split(" ")[1] #str

#getting data
city = jsonResponse["location"]["name"] #str
humidity = jsonResponse["current"]["humidity"] #int
feelsLike = jsonResponse["current"]["feelslike_c"] #float
temperature = jsonResponse["current"]["temp_c"] #float
wind = jsonResponse["current"]["wind_kph"] #float


# transforming str to date
splitLocalDateStr = localDateStr.split("-")
localDate = date(int(splitLocalDateStr[0]),
                 int(splitLocalDateStr[1]),
                 int(splitLocalDateStr[2]))

#transorming str to time
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

