import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connectToDb():
    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def insertValues(
        city,
        humidity,
        dateLocal,
        timeLocal,
        wind,
        feelsLike,
        temperture,

):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(f"""
        insert into city_weather(city, humidity,feelsLike,temperature,wind,dateLocal,timeLocal)
        values ('{city}', {humidity},{feelsLike},{temperture},{wind},'{dateLocal}','{timeLocal}')
    """)
    connection.commit()
    cursor.close()

