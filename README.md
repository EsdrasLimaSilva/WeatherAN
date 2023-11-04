# WeatherAN

this is a simple project to retrieve data from [Weather API](https://www.weatherapi.com/) and send it to a PostgreSQL database.

# Requirements

to run this project you mus have a a account in the [Weather API](https://www.weatherapi.com/) and a up and running a podtgresql database. 

## The SQL scriprt
to be able to run the script correctly, create a table called **city_weather** in the postgres DB with the following SQL script
```sql
CREATE TABLE city_weather(
	id SERIAL PRIMARY KEY,
	city VARCHAR(100),
	humidity INT,
	feelsLike REAL,
	temperature REAL,
	wind REAL,
	dateLocal DATE,
	timeLocal TIME
);
```

# How to run

with the [Requiremnts](#requirements) met, just clone this repository, go to the root folder, and run:
```python
pip install -r requirements.txt
```

you can also create a virtual environemnt and run the code up above if you want it

after that just run (in the root folder)
```python
python3 main.py
```

go to the postgresql shell or pgadmin4 and run the query
```sql
SELECT * FROM city_weather
```

if everything was ok, you'll see one Db tuple with name **Paris**